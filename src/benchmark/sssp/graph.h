// Copyright (c) 2012-2013, the Scal Project Authors.  All rights reserved.
// Please see the AUTHORS file for details.  Use of this source code is governed
// by a BSD license that can be found in the LICENSE file.

#ifndef SCAL_BENCHMARK_BFS_GRAPH_H
#define SCAL_BENCHMARK_BFS_GRAPH_H

#include <inttypes.h>
#include <limits>

typedef uint32_t graphint_t;

struct Node {
public:
  static const graphint_t no_distance = std::numeric_limits<graphint_t>::max();
  //static const graphint_t no_parent = std::numeric_limits<graphint_t>::max();

  graphint_t num_neighbors;
  graphint_t *neighbors;
#ifndef BFS
  graphint_t *weights;
#endif

  graphint_t distance;
  //graphint_t parent;
  graphint_t times_processed;

  Node () : num_neighbors(0), neighbors(0),
#ifndef BFS
            weights(0),
#endif
            distance(no_distance), times_processed(0) {}
};

struct Graph {
public:
  //static Graph* from_graph_file (const char* graph_file);
  //static Graph* from_mtx_file (const char* graph_file);
  static Graph* from_spraylist_benchmarks (const char* graph_file);
  static Graph* from_dimacs (const char* graph_file);
  static Graph* from_simple (const char* graph_file);

  void print_distances (const char* distance_file);
  void print_distances_corrected (const char* distance_file, const graphint_t cor);
  
  graphint_t num_nodes;
  Node *nodes;

private:
  Graph () {}
  Graph (const Graph &cpy) {}
};

#endif  // SCAL_BENCHMARK_BFS_GRAPH_H
