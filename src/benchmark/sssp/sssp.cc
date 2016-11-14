// Please see the AUTHORS file for details.  Use of this source code is governed
// by a BSD license that can be found in the LICENSE file.

#define __STDC_FORMAT_MACROS 1  // we want PRIu64 and friends

#include <gflags/gflags.h>
#include <pthread.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include <atomic>
#include <iostream>
#include <fstream>

#include "benchmark/common.h"
#include "benchmark/std_glue/std_pipe_api.h"
#include "datastructures/pool.h"
#include "util/allocation.h"
#include "util/malloc.h"
#include "util/operation_logger.h"
#include "util/random.h"
#include "util/threadlocals.h"
#include "util/scal-time.h"
#include "util/workloads.h"

#include "benchmark/sssp/graph.h"

DEFINE_string(prealloc_size, "1g",
              "tread local space that is initialized");
DEFINE_uint64(threads, 1,
              "number of threads");
DEFINE_bool  (print_summary, true,
              "print execution summary");
DEFINE_bool  (log_operations, false,
              "log invocation/response/linearization of all operations");
DEFINE_string(graph_format, "dimacs",
              "input graph format");
DEFINE_string(graph_file, "",
              "input graph file");
DEFINE_string(distance_file, "",
              "write computed distances to file if specified");
DEFINE_string(summary_file, "",
              "write execution summary to file if specified");
DEFINE_string(tag, "sssp",
              "tag printed in summary (e.g., to identify used data structure");

class SsspBench : public scal::Benchmark {
public:
  SsspBench(uint64_t num_threads,
            uint64_t thread_prealloc_size,
            void *data,
            Graph* graph)
    : Benchmark(num_threads,
                thread_prealloc_size,
                data),
      graph(graph), idle_threads(0) {}

  void print_summary(std::ostream& out);
protected:
  Graph* graph;
  std::atomic<uint64_t> idle_threads;
  void bench_func(void);
};

uint64_t g_num_threads;

int main(int argc, const char **argv) {
  std::string usage("Single source shortest path (SSSP) benchmark.");
  google::SetUsageMessage(usage);
  google::ParseCommandLineFlags(&argc, const_cast<char***>(&argv), true);

  uint64_t num_threads = FLAGS_threads;
  uint64_t tlsize = scal::human_size_to_pages(FLAGS_prealloc_size.c_str(),
                                              FLAGS_prealloc_size.size());

  // Init the main program as executing thread (may use rnd generator or tl
  // allocs).
  g_num_threads = FLAGS_threads;
  scal::tlalloc_init(tlsize, true /* touch pages */);
  scal::ThreadContext::prepare(num_threads + 1);
  scal::ThreadContext::assign_context();

  Graph* graph;

  std::cout << "reading graph ..." << std::endl;
  if (FLAGS_graph_format == "dimacs") {
    graph = Graph::from_dimacs(FLAGS_graph_file.c_str());
  } else if (FLAGS_graph_format == "simple") {
    graph = Graph::from_simple(FLAGS_graph_file.c_str());
  } else {
    std::cerr << "Unknown graph format" << std::endl;
    abort();
  }
  std::cout << "done" << std::endl;

  void *ds = ds_new();

  SsspBench benchmark(
    num_threads,
    tlsize,
    ds,
    graph);
  benchmark.run();

  if (FLAGS_print_summary) {
    benchmark.print_summary(std::cout);
  }
  if (!FLAGS_summary_file.empty()) {
    std::ofstream f(FLAGS_summary_file);
    benchmark.print_summary(f);
    f.close();
  }

  if (!FLAGS_distance_file.empty()) {
    std::cout << "writing distances ..." << std::endl;
    graph->print_distances(FLAGS_distance_file.c_str());
  }
  
  return EXIT_SUCCESS;
}

void SsspBench::print_summary (std::ostream& out) {
  out << FLAGS_tag << "\t"
      << FLAGS_graph_file << "\t"
      << num_threads()    << "\t"
      << execution_time() << "\t"
      << std::endl;
}

inline uint64_t pack (uint32_t a, uint32_t b) {
  uint64_t* p = scal::tlget<uint64_t, 0>();
  *p = ((uint64_t)a) << 32 | b;
  return reinterpret_cast<uint64_t>(p);
}

inline void unpack (const uint64_t& v, uint32_t& a, uint32_t& b) {
  uint64_t* p = reinterpret_cast<uint64_t*>(v);
  a = (uint32_t)((*p & 0xFFFFFFFF00000000LL) >> 32);
  b = (uint32_t)(*p & 0xFFFFFFFFLL);
}

void SsspBench::bench_func(void) {
  // uint64_t thread_id = scal::ThreadContext::get().thread_id();
  
  Pool<uint64_t> *ds = static_cast<Pool<uint64_t>*>(data_);
  uint64_t element;
  
  graphint_t src = 0;

  graphint_t node_idx;
  graphint_t node_distance;

#if 0
  uint64_t idle_threads_read;
  uint64_t fail_cnt = 0;
  uint64_t nodes_processed = 0;
#endif

  uint64_t fail = 0;

  graph->nodes[src].distance = 1;
  ds->put(pack(1, src));

  while (1) {
#if 0
    if (!ds->get(&element)) {
      // Keep threads alive until there is really no work left (i.e., every
      // thread failed to extract a node).
      idle_threads++;
      fail_cnt++;
      while ((idle_threads_read = idle_threads.load()) < num_threads() &&
             !ds->get(&element)) {
        fail_cnt++;
      }
      if (idle_threads_read == num_threads()) break;
      idle_threads--;
    }
#endif

    // "Keep alive" code from SprayList
    if (!ds->get(&element)) { // list is empty; TODO make sure threads don't quit early
      fail++;
      if (fail > 20 * num_threads()) { // TODO: really need a better break condition...
        break;
      }
      continue;
    }
    fail = 0;

    // nodes_processed++;
    unpack(element, node_distance, node_idx);

    Node& node = graph->nodes[node_idx];
    if (node_distance != node.distance) continue; // dead node
    // node.times_processed++;

    for (graphint_t i = 0; i < node.num_neighbors; i++) {
      graphint_t neighbor_idx = node.neighbors[i];
      graphint_t weight       = node.weights[i];

      Node& neighbor = graph->nodes[neighbor_idx];
      graphint_t neighbor_distance = neighbor.distance;
      graphint_t new_neighbor_distance = node_distance + weight;

      while (new_neighbor_distance < neighbor_distance) {
        // Found better path to neighbor.
        graphint_t cas_distance = __sync_val_compare_and_swap(&neighbor.distance,
                                                              neighbor_distance,
                                                              new_neighbor_distance);
        if (cas_distance == neighbor_distance) {
          // We were successful in writing our distance and are done.
          ds->put(pack(new_neighbor_distance, neighbor_idx));
          break;
        } else {
          // Somebody else wrote to neighbor_distance before us. If it is worse
          // than our distance we'll try writing again.
          neighbor_distance = cas_distance;
        }
      } 
    }
  }

  // std::cout << "thread " << thread_id << ": "
  //           << fail_cnt << " fail / "
  //           << nodes_processed << " processed"
  //           << std::endl;
}
