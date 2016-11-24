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

Graph* Graph::from_dimacs (const char* graph_file) {
  Graph* g = new Graph();
  graphint_t num_edges;

  std::istringstream iss;
  std::string line;
  char c;
  graphint_t u, v, w;

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
  for (graphint_t i = 0; i < g->num_nodes; i++) {
    graphint_t num_neighbors = g->nodes[i].num_neighbors;
    if (num_neighbors > 0) {
      g->nodes[i].neighbors = new graphint_t[num_neighbors];
#ifndef BFS
      g->nodes[i].weights   = new graphint_t[num_neighbors];
#endif
    }
  }

  // Read edges.
  {
    std::vector<graphint_t> idx(g->num_nodes, 0);
    std::ifstream infile(graph_file);

    while (std::getline(infile, line)) {
      iss.str(line);
      iss.clear();
      iss >> c;
      if (c == 'a') {
        iss >> u >> v >> w;
        g->nodes[u-1].neighbors[idx[u-1]] = v-1;
#ifndef BFS
        g->nodes[u-1].weights  [idx[u-1]] = w;
#endif
        idx[u-1]++;
      }
    }
  }

  return g;
}

Graph* Graph::from_simple (const char* graph_file) {
  Graph* g = new Graph();
  graphint_t num_edges;

  graphint_t u, v, w;

  // Read number of total nodes and edges, as well as number of neighbors for
  // every node.
  {
    std::ifstream infile(graph_file);

    infile >> g->num_nodes >> num_edges;
    g->nodes = new Node[g->num_nodes];

    for (graphint_t i = 0; i < num_edges; ++i) {
      infile >> u >> v >> w;
      assert(0 < u && u <= g->num_nodes);
      assert(0 < v && v <= g->num_nodes);
      g->nodes[u-1].num_neighbors++;
    }
  }

  // Allocate neighbors and weights array for every node.
  for (graphint_t i = 0; i < g->num_nodes; i++) {
    graphint_t num_neighbors = g->nodes[i].num_neighbors;
    if (num_neighbors > 0) {
      g->nodes[i].neighbors = new graphint_t[num_neighbors];
#ifndef BFS
      g->nodes[i].weights   = new graphint_t[num_neighbors];
#endif
    }
  }

  // Read edges.
  {
    std::vector<graphint_t> idx(g->num_nodes, 0);
    std::ifstream infile(graph_file);

    infile >> g->num_nodes >> num_edges;
    for (graphint_t i = 0; i < num_edges; ++i) {
      infile >> u >> v >> w;
      g->nodes[u-1].neighbors[idx[u-1]] = v-1;
#ifndef BFS
      g->nodes[u-1].weights  [idx[u-1]] = w;
#endif
      idx[u-1]++;
    }
  }

  return g;
}

void Graph::print_distances (const char* distance_file) {
  print_distances_corrected(distance_file, 0);
}

void Graph::print_distances_corrected (const char* distance_file, const graphint_t cor) {
  std::ofstream f;
  f.open (distance_file);
  for (graphint_t i = 0; i < num_nodes; ++i) {
    if (nodes[i].distance == Node::no_distance) {
      f << "∞";
    } else {
      f << nodes[i].distance - cor;
    }
    f << std::endl;
  }
  f.close();
}
