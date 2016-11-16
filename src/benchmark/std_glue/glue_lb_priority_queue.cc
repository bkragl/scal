// Copyright (c) 2012-2013, the Scal Project Authors.  All rights reserved.
// Please see the AUTHORS file for details.  Use of this source code is governed
// by a BSD license that can be found in the LICENSE file.

#include <gflags/gflags.h>

#include "benchmark/std_glue/std_pipe_api.h"
#include "datastructures/lockbased_priority_queue.h"

// DEFINE_uint64(dequeue_mode, 0, "different APIs for empty dequeue: "
//                                "non-blocking (0), blocking (1), timeout (2)");
// DEFINE_uint64(dequeue_timeout, 100, "dequeue timeout in ms");

extern volatile uint64_t queue_prealloc_size;

void* ds_new(void) {
  return new LockBasedPriorityQueue(queue_prealloc_size);
}

char* ds_get_stats(void) {
  return NULL;
}
