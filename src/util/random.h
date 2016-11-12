// Copyright (c) 2012-2013, the Scal Project Authors.  All rights reserved.
// Please see the AUTHORS file for details.  Use of this source code is governed
// by a BSD license that can be found in the LICENSE file.

#ifndef SCAL_UTIL_RANDOM_H_
#define SCAL_UTIL_RANDOM_H_

#include <inttypes.h>

#include <chrono>
#include <random>

#include "util/platform.h"

namespace scal {

const uint32_t kRandMax = 2147483647;

uint64_t pseudorand();
uint64_t pseudorandrange(uint32_t min, uint32_t max);
void srand(uint32_t seed);


inline uint64_t hwrand() {
  return (Rdtsc() >> 6);
}


// Fisher Yates shuffle.
// Do not use the simple linear contruential PRNG.
template<typename T>
void shuffle(T* items, size_t len, uint64_t seed = 0) {
  if (seed == 0) {
    std::random_device rd;
    seed = rd();
  }
  std::mt19937_64 rng(seed);
  for (size_t i = (len - 1); i > 0; --i) {
    std::uniform_int_distribution<size_t> dist(0, i);
    size_t swap_idx = dist(rng);
    T tmp = items[swap_idx];
    items[swap_idx] = items[i];
    items[i] = tmp;
  }
}

}  // namespace scal

#endif  // SCAL_UTIL_RANDOM_H_
