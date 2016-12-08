#!/bin/bash

VERSION="Release"
DIR="../build/out/${VERSION}"

graph_format="simple"

mkdir -p "bfs-sequential"

for graph_file in /home/bkragl/dimacs/*.gr; do
    benchmark=`basename $graph_file`
    "${DIR}/bfs-sequential" \
        -graph_format="$graph_format" \
        -graph_file="$graph_file" \
        -summary_file="bfs-sequential/${benchmark}.out" \
        -distance_file="bfs-sequential/${benchmark}.bfs.dist"
done
