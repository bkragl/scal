#!/bin/bash

# Generic script to run experiments

if [[ $# -ne 4 ]]; then
    echo "Usage: $0 algo graph_file ds_file cores"
    echo ""
    echo "algo:       the algorithm to run (sssp, bfs, ...)"
    echo "graph_file: input graph file"
    echo "ds_file:    file that lists Scal data structures to use"
    echo "cores:      space separated (and quoted) list of cores to use"
    exit 1
fi

VERSION="Release"

algo="$1"

graph_file="$2"
graph_format="simple"

ds_file="$3"

if [[ -n "$4" ]]; then
    cores="$4"
else
    cores="5 10 15 20 40 60 80"
fi

for i in 1; do
    for ds in `cat ${ds_file}`; do
        for threads in ${cores}; do
            ex="../build/out/${VERSION}/${algo}-${ds}"
            tag=`basename "$ex"`
            benchmark=`basename $graph_file`
            distance_file="${tag}_${benchmark}_${threads}_${i}.dist"
            summary_file="${tag}_${benchmark}_${threads}_${i}.out"

            echo ""
            echo "${tag}_${benchmark}_${threads}_${i}"

            timeout -k 30s 20m \
            "$ex" -tag="$tag" \
                -threads $threads \
                -prealloc_size=1200m \
                -reuse_memory=false \
                -graph_format="$graph_format" \
                -graph_file="$graph_file" \
                -summary_file="$summary_file" \
                -distance_file="$distance_file"
        done
    done
done
