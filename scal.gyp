{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'libscal',
      'type': 'static_library',
      'sources': [
        'src/util/atomic_value128.h',
        'src/util/atomic_value64_base.h',
        'src/util/atomic_value64_no_offset.h',
        'src/util/atomic_value64_offset.h',
        'src/util/atomic_value.h',
        'src/util/atomic_value_new.h',
        'src/util/allocation.h',
        'src/util/allocation.cc',
        'src/util/barrier.h',
        'src/util/bitmap.h',
        'src/util/malloc-compat.h',
        'src/util/operation_logger.h',
        'src/util/platform.h',
        'src/util/random.h',
        'src/util/random.cc',
        'src/util/threadlocals.h',
        'src/util/threadlocals.cc',
        'src/util/time.h',
        'src/util/workloads.h',
        'src/util/workloads.cc',
      ],
    },
    {
      'target_name': 'computational-load',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'sources': [
        'src/benchmark/common.h',
        'src/benchmark/common.cc',
        'src/util/allocation.h',
        'src/util/allocation.cc',
        'src/util/threadlocals.h',
        'src/util/threadlocals.cc',
        'src/util/workloads.h',
        'src/util/workloads.cc',
        'src/benchmark/computational-load/computational-load.cc',
      ],
    },
    
    ### Benchmarks ###
    {
      'target_name': 'mm-harness',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'sources': [
        'src/benchmark/common.h',
        'src/benchmark/common.cc',
        'src/util/allocation.h',
        'src/util/allocation.cc',
        'src/util/threadlocals.h',
        'src/util/threadlocals.cc',
        'src/util/workloads.h',
        'src/util/workloads.cc',
        'src/benchmark/mm/mm.cc',
      ],
    },
    {
      'target_name': 'prodcon-base',
      'type': 'static_library',
      'libraries': [ '<@(default_libraries)' ],
      'sources': [
        'src/benchmark/common.h',
        'src/benchmark/common.cc',
        'src/util/allocation.h',
        'src/util/allocation.cc',
        'src/util/threadlocals.h',
        'src/util/threadlocals.cc',
        'src/util/workloads.h',
        'src/util/workloads.cc',
        'src/benchmark/prodcon/prodcon.cc',
      ],
    },
    {
      'target_name': 'seqalt-base',
      'type': 'static_library',
      'sources': [
        'src/benchmark/common.cc',
        'src/benchmark/seqalt/seqalt.cc',
      ],
    },
    {
      'target_name': 'sssp-base',
      'type': 'static_library',
      'sources': [
        'src/benchmark/common.cc',
        'src/benchmark/sssp/graph.cc',
        'src/benchmark/sssp/sssp.cc',
      ],
    },
    {
      'target_name': 'sssp-base-prealloc',
      'type': 'static_library',
      'defines': [ 'SSSP_PREALLOC' ],
      'sources': [
        'src/benchmark/common.cc',
        'src/benchmark/sssp/graph.cc',
        'src/benchmark/sssp/sssp.cc',
      ],
    },
    {
      'target_name': 'bfs-base',
      'type': 'static_library',
      'defines': [ 'BFS' ],
      'sources': [
        'src/benchmark/common.cc',
        'src/benchmark/sssp/graph.cc',
        'src/benchmark/sssp/sssp.cc',
      ],
    },
    {
      'target_name': 'sssp-sequential',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'sources': [
        'src/benchmark/sssp/sequential.cc',
        'src/benchmark/sssp/graph.cc',
        'src/datastructures/min_heap.cc',
      ],
    },
    
    ### Producer-Consumer (prodcon) ###
    {
      'target_name': 'prodcon-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ms',
      ],
    },
    {
      'target_name': 'prodcon-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:treiber',
      ],
    },
    {
      'target_name': 'prodcon-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:kstack',
      ],
    },
    {
      'target_name': 'prodcon-ll-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ll-kstack',
      ],
    },
    {
      'target_name': 'prodcon-dds-1random-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:dds-1random-ms',
      ],
    },
    {
      'target_name': 'prodcon-dds-partrr-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:dds-partrr-ms',
      ],
    },
    {
      'target_name': 'prodcon-dds-partrr-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:dds-partrr-treiber',
      ],
    },
    {
      'target_name': 'prodcon-dds-1random-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:dds-1random-treiber',
      ],
    },
    {
      'target_name': 'prodcon-fc',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:fc',
      ],
    },
    {
      'target_name': 'prodcon-rd',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:rd',
      ],
    },
    {
      'target_name': 'prodcon-sq',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:sq',
      ],
    },
    {
      'target_name': 'prodcon-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:us-kfifo',
      ],
    },
    {
      'target_name': 'prodcon-bs-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:bs-kfifo',
      ],
    },
    {
      'target_name': 'prodcon-ll-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ll-us-kfifo',
      ],
    },
    {
      'target_name': 'prodcon-ll-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ll-dds-ms',
      ],
    },
    {
      'target_name': 'prodcon-ll-dds-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ll-dds-treiber',
      ],
    },
    {
      'target_name': 'prodcon-ll-dds-ms-nonlinempty',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ll-dds-ms-nonlinempty',
      ],
    },
    {
      'target_name': 'prodcon-ll-dds-treiber-nonlinempty',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ll-dds-treiber-nonlinempty',
      ],
    },
    {
      'target_name': 'prodcon-ll-dyn-dds-ms-nonlinempty',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ll-dyn-dds-ms-nonlinempty',
      ],
    },
    {
      'target_name': 'prodcon-ll-dyn-dds-treiber-nonlinempty',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ll-dyn-dds-treiber-nonlinempty',
      ],
    },
    {
      'target_name': 'prodcon-ll-dyn-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ll-dyn-dds-ms',
      ],
    },
    #{
    #  'target_name': 'prodcon-wf-queue',
    #  'type': 'executable',
    #  'libraries': [ '<@(default_libraries)' ],
    #  'dependencies': [
    #    'libscal',
    #    'prodcon-base',
    #    'glue.gyp:wf-queue',
    #  ],
    #},
    {
      'target_name': 'prodcon-ll-dyn-dds-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ll-dyn-dds-treiber',
      ],
    },
    {
      'target_name': 'prodcon-lcrq',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:lcrq',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-cas-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:hc-ts-cas-stack',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-stutter-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:hc-ts-stutter-stack',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-interval-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:hc-ts-interval-stack',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-atomic-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:hc-ts-atomic-stack',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-hardware-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:hc-ts-hardware-stack',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-cas-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:hc-ts-cas-queue',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-stutter-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:hc-ts-stutter-queue',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-interval-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:hc-ts-interval-queue',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-atomic-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:hc-ts-atomic-queue',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-hardware-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:hc-ts-hardware-queue',
      ],
    },
    {
      'target_name': 'prodcon-ts-cas-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ts-cas-deque',
      ],
    },
    {
      'target_name': 'prodcon-ts-stutter-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ts-stutter-deque',
      ],
    },
    {
      'target_name': 'prodcon-ts-interval-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ts-interval-deque',
      ],
    },
    {
      'target_name': 'prodcon-ts-atomic-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ts-atomic-deque',
      ],
    },
    {
      'target_name': 'prodcon-ts-hardware-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:ts-hardware-deque',
      ],
    },
    {
      'target_name': 'prodcon-rts-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:rts-queue',
      ],
    },
    {
      'target_name': 'prodcon-cts-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:cts-queue',
      ],
    },
    {
      'target_name': 'prodcon-eb-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:eb-stack',
      ],
    },
    {
      'target_name': 'prodcon-lb-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:lb-stack',
      ],
    },
    {
      'target_name': 'prodcon-lb-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:lb-queue',
      ],
    },
    {
      'target_name': 'prodcon-lru-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:lru-dds-ms',
      ],
    },
    {
      'target_name': 'prodcon-lru-dds-treiber-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gyp:lru-dds-treiber-stack',
      ],
    },

    ### Sequential Alternation (seqalt) ###
    {
      'target_name': 'seqalt-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:ms',
      ],
    },
    {
      'target_name': 'seqalt-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:treiber',
      ],
    },
    {
      'target_name': 'seqalt-dds-partrr-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:dds-partrr-ms',
      ],
    },
    {
      'target_name': 'seqalt-dds-partrr-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:dds-partrr-treiber',
      ],
    },
    {
      'target_name': 'seqalt-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:kstack',
      ],
    },
    {
      'target_name': 'seqalt-ll-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:ll-kstack',
      ],
    },
    {
      'target_name': 'seqalt-dds-1random-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:dds-1random-ms',
      ],
    },
    {
      'target_name': 'seqalt-dds-1random-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:dds-1random-treiber',
      ],
    },
    {
      'target_name': 'seqalt-fc',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:fc',
      ],
    },
    {
      'target_name': 'seqalt-rd',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:rd',
      ],
    },
    {
      'target_name': 'seqalt-sq',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:sq',
      ],
    },
    {
      'target_name': 'seqalt-bs-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:bs-kfifo',
      ],
    },
    {
      'target_name': 'seqalt-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:us-kfifo',
      ],
    },
    {
      'target_name': 'seqalt-ll-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:ll-us-kfifo',
      ],
    },
    {
      'target_name': 'seqalt-ll-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:ll-dds-ms',
      ],
    },
    {
      'target_name': 'seqalt-ll-dds-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:ll-dds-treiber',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-cas-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:hc-ts-cas-stack',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-stutter-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:hc-ts-stutter-stack',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-interval-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:hc-ts-interval-stack',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-atomic-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:hc-ts-atomic-stack',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-hardware-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:hc-ts-hardware-stack',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-cas-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:hc-ts-cas-queue',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-stutter-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:hc-ts-stutter-queue',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-interval-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:hc-ts-interval-queue',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-atomic-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:hc-ts-atomic-queue',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-hardware-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:hc-ts-hardware-queue',
      ],
    },
    {
      'target_name': 'seqalt-ts-cas-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:ts-cas-deque',
      ],
    },
    {
      'target_name': 'seqalt-ts-stutter-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:ts-stutter-deque',
      ],
    },
    {
      'target_name': 'seqalt-ts-interval-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:ts-interval-deque',
      ],
    },
    {
      'target_name': 'seqalt-ts-atomic-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:ts-atomic-deque',
      ],
    },
    {
      'target_name': 'seqalt-ts-hardware-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:ts-hardware-deque',
      ],
    },
    {
      'target_name': 'seqalt-rts-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:rts-queue',
      ],
    },
    {
      'target_name': 'seqalt-cts-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:cts-queue',
      ],
    },
    {
      'target_name': 'seqalt-eb-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:eb-stack',
      ],
    },
    {
      'target_name': 'seqalt-lb-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:lb-stack',
      ],
    },
    {
      'target_name': 'seqalt-lb-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:lb-queue',
      ],
    },
    #{
    #  'target_name': 'seqalt-wf-queue',
    #  'type': 'executable',
    #  'libraries': [ '<@(default_libraries)' ],
    #  'dependencies': [
    #    'libscal',
    #    'seqalt-base',
    #    'glue.gyp:wf-queue',
    #  ],
    #},
    {
      'target_name': 'seqalt-lru-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:lru-dds-ms',
      ],
    },
    {
      'target_name': 'seqalt-lru-dds-treiber-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:lru-dds-treiber-stack',
      ],
    },
    {
      'target_name': 'seqalt-ll-dyn-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:ll-dyn-dds-ms',
      ],
    },
    {
      'target_name': 'seqalt-ll-dyn-dds-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:ll-dyn-dds-treiber',
      ],
    },
    {
      'target_name': 'seqalt-lcrq',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gyp:lcrq',
      ],
    },

    ### Single source shortest path (sssp) ###
    {
      'target_name': 'sssp-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:ms',
      ],
    },
    {
      'target_name': 'sssp-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:treiber',
      ],
    },
    {
      'target_name': 'sssp-dds-partrr-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:dds-partrr-ms',
      ],
    },
    {
      'target_name': 'sssp-dds-partrr-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:dds-partrr-treiber',
      ],
    },
    {
      'target_name': 'sssp-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:kstack',
      ],
    },
    {
      'target_name': 'sssp-ll-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:ll-kstack',
      ],
    },
    {
      'target_name': 'sssp-dds-1random-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:dds-1random-ms',
      ],
    },
    {
      'target_name': 'sssp-dds-1random-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:dds-1random-treiber',
      ],
    },
    {
      'target_name': 'sssp-fc',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:fc',
      ],
    },
    {
      'target_name': 'sssp-rd',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:rd',
      ],
    },
    {
      'target_name': 'sssp-sq',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:sq',
      ],
    },
    {
      'target_name': 'sssp-bs-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:bs-kfifo',
      ],
    },
    {
      'target_name': 'sssp-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:us-kfifo',
      ],
    },
    {
      'target_name': 'sssp-ll-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:ll-us-kfifo',
      ],
    },
    {
      'target_name': 'sssp-ll-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:ll-dds-ms',
      ],
    },
    {
      'target_name': 'sssp-ll-dds-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:ll-dds-treiber',
      ],
    },
    {
      'target_name': 'sssp-hc-ts-cas-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:hc-ts-cas-stack',
      ],
    },
    {
      'target_name': 'sssp-hc-ts-stutter-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:hc-ts-stutter-stack',
      ],
    },
    {
      'target_name': 'sssp-hc-ts-interval-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:hc-ts-interval-stack',
      ],
    },
    {
      'target_name': 'sssp-hc-ts-atomic-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:hc-ts-atomic-stack',
      ],
    },
    {
      'target_name': 'sssp-hc-ts-hardware-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:hc-ts-hardware-stack',
      ],
    },
    {
      'target_name': 'sssp-hc-ts-cas-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:hc-ts-cas-queue',
      ],
    },
    {
      'target_name': 'sssp-hc-ts-stutter-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:hc-ts-stutter-queue',
      ],
    },
    {
      'target_name': 'sssp-hc-ts-interval-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:hc-ts-interval-queue',
      ],
    },
    {
      'target_name': 'sssp-hc-ts-atomic-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:hc-ts-atomic-queue',
      ],
    },
    {
      'target_name': 'sssp-hc-ts-hardware-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:hc-ts-hardware-queue',
      ],
    },
    {
      'target_name': 'sssp-ts-cas-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:ts-cas-deque',
      ],
    },
    {
      'target_name': 'sssp-ts-stutter-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:ts-stutter-deque',
      ],
    },
    {
      'target_name': 'sssp-ts-interval-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:ts-interval-deque',
      ],
    },
    {
      'target_name': 'sssp-ts-atomic-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:ts-atomic-deque',
      ],
    },
    {
      'target_name': 'sssp-ts-hardware-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:ts-hardware-deque',
      ],
    },
    {
      'target_name': 'sssp-rts-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:rts-queue',
      ],
    },
    {
      'target_name': 'sssp-cts-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:cts-queue',
      ],
    },
    {
      'target_name': 'sssp-eb-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:eb-stack',
      ],
    },
    {
      'target_name': 'sssp-lb-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:lb-stack',
      ],
    },
    {
      'target_name': 'sssp-lb-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:lb-queue',
      ],
    },
    #{
    #  'target_name': 'sssp-wf-queue',
    #  'type': 'executable',
    #  'libraries': [ '<@(default_libraries)' ],
    #  'dependencies': [
    #    'libscal',
    #    'sssp-base',
    #    'glue.gyp:wf-queue',
    #  ],
    #},
    {
      'target_name': 'sssp-lru-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:lru-dds-ms',
      ],
    },
    {
      'target_name': 'sssp-lru-dds-treiber-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:lru-dds-treiber-stack',
      ],
    },
    {
      'target_name': 'sssp-ll-dyn-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:ll-dyn-dds-ms',
      ],
    },
    {
      'target_name': 'sssp-ll-dyn-dds-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:ll-dyn-dds-treiber',
      ],
    },
    {
      'target_name': 'sssp-lcrq',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base',
        'glue.gyp:lcrq',
      ],
    },
    {
      'target_name': 'sssp-lb-priority-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'sssp-base-prealloc',
        'glue.gyp:lb-priority-queue',
      ],
    },

    ### Breadth-first search (bfs) ###
    {
      'target_name': 'bfs-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:ms',
      ],
    },
    {
      'target_name': 'bfs-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:treiber',
      ],
    },
    {
      'target_name': 'bfs-dds-partrr-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:dds-partrr-ms',
      ],
    },
    {
      'target_name': 'bfs-dds-partrr-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:dds-partrr-treiber',
      ],
    },
    {
      'target_name': 'bfs-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:kstack',
      ],
    },
    {
      'target_name': 'bfs-ll-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:ll-kstack',
      ],
    },
    {
      'target_name': 'bfs-dds-1random-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:dds-1random-ms',
      ],
    },
    {
      'target_name': 'bfs-dds-1random-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:dds-1random-treiber',
      ],
    },
    {
      'target_name': 'bfs-fc',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:fc',
      ],
    },
    {
      'target_name': 'bfs-rd',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:rd',
      ],
    },
    {
      'target_name': 'bfs-sq',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:sq',
      ],
    },
    {
      'target_name': 'bfs-bs-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:bs-kfifo',
      ],
    },
    {
      'target_name': 'bfs-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:us-kfifo',
      ],
    },
    {
      'target_name': 'bfs-ll-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:ll-us-kfifo',
      ],
    },
    {
      'target_name': 'bfs-ll-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:ll-dds-ms',
      ],
    },
    {
      'target_name': 'bfs-ll-dds-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:ll-dds-treiber',
      ],
    },
    {
      'target_name': 'bfs-hc-ts-cas-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:hc-ts-cas-stack',
      ],
    },
    {
      'target_name': 'bfs-hc-ts-stutter-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:hc-ts-stutter-stack',
      ],
    },
    {
      'target_name': 'bfs-hc-ts-interval-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:hc-ts-interval-stack',
      ],
    },
    {
      'target_name': 'bfs-hc-ts-atomic-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:hc-ts-atomic-stack',
      ],
    },
    {
      'target_name': 'bfs-hc-ts-hardware-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:hc-ts-hardware-stack',
      ],
    },
    {
      'target_name': 'bfs-hc-ts-cas-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:hc-ts-cas-queue',
      ],
    },
    {
      'target_name': 'bfs-hc-ts-stutter-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:hc-ts-stutter-queue',
      ],
    },
    {
      'target_name': 'bfs-hc-ts-interval-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:hc-ts-interval-queue',
      ],
    },
    {
      'target_name': 'bfs-hc-ts-atomic-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:hc-ts-atomic-queue',
      ],
    },
    {
      'target_name': 'bfs-hc-ts-hardware-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:hc-ts-hardware-queue',
      ],
    },
    {
      'target_name': 'bfs-ts-cas-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:ts-cas-deque',
      ],
    },
    {
      'target_name': 'bfs-ts-stutter-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:ts-stutter-deque',
      ],
    },
    {
      'target_name': 'bfs-ts-interval-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:ts-interval-deque',
      ],
    },
    {
      'target_name': 'bfs-ts-atomic-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:ts-atomic-deque',
      ],
    },
    {
      'target_name': 'bfs-ts-hardware-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:ts-hardware-deque',
      ],
    },
    {
      'target_name': 'bfs-rts-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:rts-queue',
      ],
    },
    {
      'target_name': 'bfs-cts-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:cts-queue',
      ],
    },
    {
      'target_name': 'bfs-eb-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:eb-stack',
      ],
    },
    {
      'target_name': 'bfs-lb-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:lb-stack',
      ],
    },
    {
      'target_name': 'bfs-lb-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:lb-queue',
      ],
    },
    #{
    #  'target_name': 'bfs-wf-queue',
    #  'type': 'executable',
    #  'libraries': [ '<@(default_libraries)' ],
    #  'dependencies': [
    #    'libscal',
    #    'bfs-base',
    #    'glue.gyp:wf-queue',
    #  ],
    #},
    {
      'target_name': 'bfs-lru-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:lru-dds-ms',
      ],
    },
    {
      'target_name': 'bfs-lru-dds-treiber-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:lru-dds-treiber-stack',
      ],
    },
    {
      'target_name': 'bfs-ll-dyn-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:ll-dyn-dds-ms',
      ],
    },
    {
      'target_name': 'bfs-ll-dyn-dds-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:ll-dyn-dds-treiber',
      ],
    },
    {
      'target_name': 'bfs-lcrq',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'bfs-base',
        'glue.gyp:lcrq',
      ],
    },
    # {
    #   'target_name': 'bfs-lb-priority-queue',
    #   'type': 'executable',
    #   'libraries': [ '<@(default_libraries)' ],
    #   'dependencies': [
    #     'libscal',
    #     'bfs-base-prealloc',
    #     'glue.gyp:lb-priority-queue',
    #   ],
    # }
  ]
}
