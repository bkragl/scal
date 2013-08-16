// Copyright (c) 2012-2013, the Scal Project Authors.  All rights reserved.
// Please see the AUTHORS file for details.  Use of this source code is governed
// by a BSD license that can be found in the LICENSE file.

#define __STDC_FORMAT_MACROS 1  // we want PRIu64 and friends
#include <gflags/gflags.h>
#include <stdint.h>

#include "benchmark/std_glue/std_pipe_api.h"
#include "datastructures/elimination_backoff_stack.h"

DEFINE_uint64(collision, 0, "size of the collision array");


EliminationBackoffStack<uint64_t> *ebs;

void* ds_new() {
  uint64_t size_collision = (g_num_threads + 1)/2;
  if (FLAGS_collision != 0) {
    size_collision = FLAGS_collision;
  }

  ebs = new EliminationBackoffStack<uint64_t>(g_num_threads + 1, 
          size_collision );
  return static_cast<void*>(ebs);
}

char* ds_get_stats(void) {
  return ebs->ds_get_stats();
}
