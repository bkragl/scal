// Please see the AUTHORS file for details.  Use of this source code is governed
// by a BSD license that can be found in the LICENSE file.

#define __STDC_FORMAT_MACROS 1  // we want PRIu64 and friends

#include <gflags/gflags.h>

#include <iostream>
#include <fstream>

#include "util/scal-time.h"

#include "datastructures/min_heap.h"
#include "benchmark/sssp/graph.h"

DEFINE_bool  (print_summary, true,
              "print execution summary");
DEFINE_string(graph_format, "dimacs",
              "input graph format");
DEFINE_string(graph_file, "",
              "input graph file");
DEFINE_string(distance_file, "",
              "write computed distances to file if specified");
DEFINE_string(summary_file, "",
              "write execution summary to file if specified");

uint64_t start_time;
uint64_t end_time;

inline uint64_t execution_time(void) {
  return end_time - start_time;
}

void print_summary (std::ostream& out) {
  out << "sequential"     << "\t"
      << FLAGS_graph_file << "\t"
      << 1                << "\t"
      << execution_time() << "\t"
      << std::endl;
}

inline uint64_t pack (uint32_t a, uint32_t b) {
  return ((uint64_t)a) << 32 | (uint64_t)b;
}

inline void unpack (const uint64_t& v, uint32_t& a, uint32_t& b) {
  a = (uint32_t)((v & 0xFFFFFFFF00000000LL) >> 32);
  b = (uint32_t)(v & 0xFFFFFFFFLL);
}

void dijkstra(Graph* graph) {
  min_heap queue(graph->num_nodes);

  uint64_t element;
  
  graphint_t src = 0;

  graphint_t node_idx;
  graphint_t node_distance;

  graph->nodes[src].distance = 0;
  queue.insert(pack(0, src));

  start_time = get_utime();
  
  while (!queue.empty()) {
    // queue.Print();
    element = queue.get_min();
    queue.delete_min();

    unpack(element, node_distance, node_idx);

    // std::cout << "processing " << node_idx << "/" << node_distance << std::endl;

    Node& node = graph->nodes[node_idx];
    if (node_distance != node.distance) continue; // dead node
    node.times_processed++;
    
    for (graphint_t i = 0; i < node.num_neighbors; i++) {
      graphint_t neighbor_idx = node.neighbors[i];
      graphint_t weight       = node.weights[i];
      
      Node& neighbor = graph->nodes[neighbor_idx];
      graphint_t neighbor_distance = neighbor.distance;
      graphint_t new_neighbor_distance = node_distance + weight;
      
      // std::cout << "  neighbor " << neighbor_idx << "/" << neighbor_distance << std::endl;

      if (new_neighbor_distance < neighbor_distance) {
        // Found better path to neighbor.
        neighbor.distance = new_neighbor_distance;
        queue.insert(pack(new_neighbor_distance, neighbor_idx));
        // std::cout << "    new dist " << new_neighbor_distance << std::endl;
      }

      // queue.Print();
    }
    
    // std::cout << std::endl;
  }

  for (uint64_t i = 0; i < graph->num_nodes; ++i) {
    if (graph->nodes[i].times_processed != 1) {
      std::cout << "node processed too many times ("
                << graph->nodes[i].times_processed
                << ")" << std::endl;
      break;
    }
  }

  end_time = get_utime();
}


int main(int argc, const char **argv) {
  std::string usage("Single source shortest path (SSSP) benchmark.");
  google::SetUsageMessage(usage);
  google::ParseCommandLineFlags(&argc, const_cast<char***>(&argv), true);

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

  dijkstra(graph);

  if (FLAGS_print_summary) {
    print_summary(std::cout);
  }
  if (!FLAGS_summary_file.empty()) {
    std::ofstream f(FLAGS_summary_file);
    print_summary(f);
    f.close();
  }

  if (!FLAGS_distance_file.empty()) {
    std::cout << "writing distances ..." << std::endl;
    graph->print_distances(FLAGS_distance_file.c_str());
  }
  
  return EXIT_SUCCESS;
}
