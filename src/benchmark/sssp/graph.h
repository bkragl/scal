// Copyright (c) 2012-2013, the Scal Project Authors.  All rights reserved.
// Please see the AUTHORS file for details.  Use of this source code is governed
// by a BSD license that can be found in the LICENSE file.

#ifndef SCAL_BENCHMARK_BFS_GRAPH_H
#define SCAL_BENCHMARK_BFS_GRAPH_H

#include <inttypes.h>
#include <limits>

struct Node {
public:
  static const uint64_t no_distance = std::numeric_limits<uint64_t>::max();
  //static const uint64_t no_parent = std::numeric_limits<uint64_t>::max();

  uint64_t num_neighbors;
  uint64_t *neighbors;
  uint64_t *weights;

  uint64_t distance;
  //uint64_t parent;
  uint64_t times_processed;
};

struct Graph {
public:
  //static Graph* from_graph_file(const char* graph_file);
  //static Graph* from_mtx_file(const char* graph_file);
  static Graph from_spraylist_benchmarks(const char* graph_file);

  void print_distances (const char* weights_file);
  
  uint64_t num_nodes;
  Node *nodes;

private:
  Graph() {}
};

#endif  // SCAL_BENCHMARK_BFS_GRAPH_H
