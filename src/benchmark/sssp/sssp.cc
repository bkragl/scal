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

#include <iostream>
#include <fstream>

#include "benchmark/common.h"
#include "benchmark/std_glue/std_pipe_api.h"
#include "datastructures/pool.h"
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
DEFINE_bool  (allow_empty_returns, false,
              "does not stop the execution at an empty-dequeue");
DEFINE_string(graph_format, "dimacs",
              "input graph format (dimacs/spray)");
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
                data),  graph(graph){
  }

  void print_summary(std::ostream& out);
protected:
  Graph* graph;
  void bench_func(void);
};


int main(int argc, const char **argv) {
  std::string usage("Single source shortest path (SSSP) benchmark.");
  google::SetUsageMessage(usage);
  google::ParseCommandLineFlags(&argc, const_cast<char***>(&argv), true);

  uint64_t num_threads = FLAGS_threads;
  uint64_t tlsize = scal::human_size_to_pages(FLAGS_prealloc_size.c_str(),
                                              FLAGS_prealloc_size.size());

  // Init the main program as executing thread (may use rnd generator or tl
  // allocs).
  scal::tlalloc_init(tlsize, true /* touch pages */);
  scal::ThreadContext::prepare(num_threads + 1);
  scal::ThreadContext::assign_context();

  Graph* graph;

  std::cout << "reading graph ..." << std::endl;
  if (FLAGS_graph_format == "dimacs") {
    graph = Graph::from_dimacs(FLAGS_graph_file.c_str());
  } else if (FLAGS_graph_format == "simple") {
    graph = Graph::from_simple(FLAGS_graph_file.c_str());
  } else if (FLAGS_graph_format == "spray") {
    graph = Graph::from_spraylist_benchmarks(FLAGS_graph_file.c_str());
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

void SsspBench::bench_func(void) {
  Pool<uint64_t> *ds = static_cast<Pool<uint64_t>*>(data_);
//  uint64_t thread_id = scal::ThreadContext::get().thread_id();
  uint64_t src = 0;
  uint64_t node_idx;
  uint64_t node_distance;

  uint64_t fail = 0;

  graph->nodes[src].distance = 0;

  ds->put(src);

  while (1) {
    //if (!ds->get(&node_distance, &node_idx)) { // list is empty; TODO make sure threads don't quit early
    if (!ds->get(&node_idx)) { // list is empty; TODO make sure threads don't quit early
      fail++;
      if (fail > 20 * num_threads()) { // TODO: really need a better break condition...
        break;
      }
      continue;
    }
    
    fail = 0;

    Node& node = graph->nodes[node_idx];
    //if (node_distance != node.distance) continue; // dead node
    node_distance = node.distance;
    node.times_processed++;

    for (uint64_t i = 0; i < node.num_neighbors; i++) {
      uint64_t neighbor_idx = node.neighbors[i];
      uint64_t weight       = node.weights[i];

      Node& neighbor = graph->nodes[neighbor_idx];
      uint64_t neighbor_distance = neighbor.distance;
      uint64_t new_neighbor_distance = node_distance + weight;

      if (new_neighbor_distance < neighbor_distance) { // found better path to v
        bool cas = __sync_bool_compare_and_swap(&neighbor.distance,
                                                neighbor_distance,
                                                new_neighbor_distance);
        if (cas) {
          ds->put(neighbor_idx);
          //sl_add_val(d->set, dist_node+w, v, TRANSACTIONAL); // add to queue only if CAS is successful
        } else {
          i--; // retry
        }
      } 
    }
  }
}
