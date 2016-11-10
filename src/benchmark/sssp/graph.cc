// Copyright (c) 2012-2013, the Scal Project Authors.  All rights reserved.
// Please see the AUTHORS file for details.  Use of this source code is governed
// by a BSD license that can be found in the LICENSE file.

#include "benchmark/sssp/graph.h"

#include <cassert>

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

Graph* Graph::from_spraylist_benchmarks(const char* graph_file) {
  Graph* g = new Graph();

  uint64_t num_edges;

  FILE* fp = fopen(graph_file, "r");
  fscanf(fp, "# Nodes: %" PRIu64 " Edges: %" PRIu64 "\n", &g->num_nodes, &num_edges);

  g->nodes = new Node[g->num_nodes];
  
  for (uint64_t i = 0; i < g->num_nodes; i++) {
    g->nodes[i].num_neighbors = 0;
    g->nodes[i].distance = Node::no_distance;
    //g->nodes[i].times_processed = 0;
  }

  uint64_t u,v;
  while (fscanf(fp, "%" PRIu64 " %" PRIu64 "\n", &u, &v) == 2) {
    if (u >= g->num_nodes) continue;
    if (v >= g->num_nodes) continue;
    g->nodes[u].num_neighbors++;
  }

  fclose(fp);
  
  for (uint64_t i = 0; i < g->num_nodes; i++) {
    uint64_t num_neighbors = g->nodes[i].num_neighbors;
    if (num_neighbors > 0) {
      g->nodes[i].neighbors = new uint64_t[num_neighbors];
      g->nodes[i].weights   = new uint64_t[num_neighbors];
    }
  }

  fp = fopen(graph_file, "r");
  {
    uint64_t  tmp;
    fscanf(fp, "# Nodes: %" PRIu64 " Edges: %" PRIu64 "\n", &tmp, &num_edges);
  }

  std::vector<uint64_t> idx(g->num_nodes, 0);

  srand(123);
  while (fscanf(fp, "%" PRIu64 " %" PRIu64 "\n", &u, &v) == 2) {
    if (u >= g->num_nodes) continue;
    if (v >= g->num_nodes) continue;
    g->nodes[u].neighbors[idx[u]] = v;
    g->nodes[u].weights  [idx[u]] = rand() % 100;
    idx[u]++;
  }
  
  return g;
}

Graph* Graph::from_dimacs (const char* graph_file) {
  Graph* g = new Graph();
  uint64_t num_edges;

  std::istringstream iss;
  std::string line;
  char c;
  uint64_t u, v, w;

  // Read number of total nodes and edges, as well as number of neighbors for
  // every node.
  {
    std::ifstream infile(graph_file);
    std::string tmp;

    while (std::getline(infile, line) && line[0] == 'c') {}

    assert(line[0] == 'p');

    iss.str(line);
    iss.clear();
    iss >> c >> tmp >> g->num_nodes >> num_edges;
    assert(c == 'p' && tmp == "sp");

    g->nodes = new Node[g->num_nodes];

    while (std::getline(infile, line)) {
      iss.str(line);
      iss.clear();
      iss >> c;

      if (c == 'a') {
        iss >> u >> v;
        assert(0 < u && u <= g->num_nodes);
        assert(0 < v && v <= g->num_nodes);
        g->nodes[u-1].num_neighbors++;
        num_edges--;
      }
    }

    assert (num_edges == 0);
  }

  // Allocate neighbors and weights array for every node.
  for (uint64_t i = 0; i < g->num_nodes; i++) {
    uint64_t num_neighbors = g->nodes[i].num_neighbors;
    if (num_neighbors > 0) {
      g->nodes[i].neighbors = new uint64_t[num_neighbors];
      g->nodes[i].weights   = new uint64_t[num_neighbors];
    }
  }

  // Read edges.
  {
    std::vector<uint64_t> idx(g->num_nodes, 0);
    std::ifstream infile(graph_file);

    while (std::getline(infile, line)) {
      iss.str(line);
      iss.clear();
      iss >> c;
      if (c == 'a') {
        iss >> u >> v >> w;
        g->nodes[u-1].neighbors[idx[u-1]] = v-1;
        g->nodes[u-1].weights  [idx[u-1]] = w;
        idx[u-1]++;
      }
    }
  }

  return g;
}

Graph* Graph::from_simple (const char* graph_file) {
  Graph* g = new Graph();
  uint64_t num_edges;

  uint64_t u, v, w;

  // Read number of total nodes and edges, as well as number of neighbors for
  // every node.
  {
    std::ifstream infile(graph_file);

    infile >> g->num_nodes >> num_edges;
    g->nodes = new Node[g->num_nodes];

    for (uint64_t i = 0; i < num_edges; ++i) {
      infile >> u >> v >> w;
      assert(0 < u && u <= g->num_nodes);
      assert(0 < v && v <= g->num_nodes);
      g->nodes[u-1].num_neighbors++;
    }
  }

  // Allocate neighbors and weights array for every node.
  for (uint64_t i = 0; i < g->num_nodes; i++) {
    uint64_t num_neighbors = g->nodes[i].num_neighbors;
    if (num_neighbors > 0) {
      g->nodes[i].neighbors = new uint64_t[num_neighbors];
      g->nodes[i].weights   = new uint64_t[num_neighbors];
    }
  }

  // Read edges.
  {
    std::vector<uint64_t> idx(g->num_nodes, 0);
    std::ifstream infile(graph_file);

    infile >> g->num_nodes >> num_edges;
    for (uint64_t i = 0; i < num_edges; ++i) {
      infile >> u >> v >> w;
      g->nodes[u-1].neighbors[idx[u-1]] = v-1;
      g->nodes[u-1].weights  [idx[u-1]] = w;
      idx[u-1]++;
    }
  }

  return g;
}

void Graph::print_distances (const char* distance_file) {
  std::ofstream f;
  f.open (distance_file);
  for (uint64_t i = 0; i < num_nodes; ++i) {
    f << nodes[i].distance << std::endl;
  }
  f.close();
}
