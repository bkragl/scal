// Copyright (c) 2012-2013, the Scal Project Authors.  All rights reserved.
// Please see the AUTHORS file for details.  Use of this source code is governed
// by a BSD license that can be found in the LICENSE file.

#include "benchmark/sssp/graph.h"

#include <algorithm>
#include <cstddef>
#include <cstdlib>
#include <string>
#include <vector>

#include "util/malloc.h"

Graph Graph::from_spraylist_benchmarks(const char* graph_file) {
  Graph g;

  uint64_t num_edges;

  FILE* fp = fopen(graph_file, "r");
  fscanf(fp, "# Nodes: %" PRIu64 " Edges: %" PRIu64 "\n", &g.num_nodes, &num_edges);

  g.nodes = new Node[g.num_nodes];
  
  for (uint64_t i = 0; i < g.num_nodes; i++) {
    g.nodes[i].num_neighbors = 0;
    g.nodes[i].distance = Node::no_distance;
    //g.nodes[i].times_processed = 0;
  }

  uint64_t u,v;
  while (fscanf(fp, "%" PRIu64 " %" PRIu64 "\n", &u, &v) == 2) {
    g.nodes[u].num_neighbors++;
  }

  fclose(fp);
  
  for (uint64_t i = 0; i < g.num_nodes; i++) {
    g.nodes[i].neighbors = new uint64_t[g.nodes[i].num_neighbors];
    g.nodes[i].weights   = new uint64_t[g.nodes[i].num_neighbors];
  }
   
  fp = fopen(graph_file, "r");
  uint64_t  tmp;
  fscanf(fp, "# Nodes: %" PRIu64 " Edges: %" PRIu64 "\n", &tmp, &num_edges);

  uint64_t  idx[g.num_nodes];
  for (uint64_t i = 0; i < g.num_nodes; i++) {
    idx[i] = 0;
  }

  while (fscanf(fp, "%" PRIu64 " %" PRIu64 "\n", &u, &v) == 2) {
    g.nodes[u].neighbors[idx[u]] = v;
    g.nodes[u].weights[idx[u]] = rand() % 100;
    idx[u]++;
  }
  
  return g;
}
