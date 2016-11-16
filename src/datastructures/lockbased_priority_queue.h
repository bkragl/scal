// Copyright (c) 2012-2013, the Scal Project Authors.  All rights reserved.
// Please see the AUTHORS file for details.  Use of this source code is governed
// by a BSD license that can be found in the LICENSE file.

#ifndef SCAL_DATASTRUCTURES_LOCKBASED_PRIORITY_QUEUE_
#define SCAL_DATASTRUCTURES_LOCKBASED_PRIORITY_QUEUE_

#include "datastructures/queue.h"
#include "datastructures/min_heap.h"
#include "util/malloc.h"
#include "util/platform.h"

class LockBasedPriorityQueue : Queue<uint64_t> {
public:
  LockBasedPriorityQueue (uint64_t capacity) : heap(capacity) {
    global_lock_ = scal::get<pthread_mutex_t>(kPtrAlignment);
    int rc = pthread_mutex_init(global_lock_, NULL);
    check_error("pthread_mutex_init", rc);
    // enqueue_cond_ = scal::get<pthread_cond_t>(kPtrAlignment);
    // rc = pthread_cond_init(enqueue_cond_, NULL);
    // check_error("pthread_cond_init", rc);
  }

  bool enqueue (uint64_t item) {
    lock();
    heap.insert(item);
    // rc = pthread_cond_broadcast(enqueue_cond_);
    // check_error("pthread_cond_broadcast", rc);
    unlock();
    return true;
  }

  bool dequeue (uint64_t *item) {
    lock();
    if (heap.empty()) {
      unlock();
      return false;
    }
    *item = heap.get_min();
    heap.delete_min();
    unlock();
    return true;
  }

private:
  static const uint8_t kPtrAlignment = scal::kCachePrefetch;

  min_heap heap;
  
  pthread_mutex_t *global_lock_;
  // pthread_cond_t *enqueue_cond_;

  inline void lock () {
    int rc = pthread_mutex_lock(global_lock_);
    check_error("pthread_mutex_lock", rc);
  }

  inline void unlock () {
    int rc = pthread_mutex_unlock(global_lock_);
    check_error("pthread_mutex_unlock", rc);
  }
  
  inline void check_error(const char *std, int rc) {
    if (rc != 0) {
      char err[256];
      char *tmp = strerror_r(rc, err, 256);
      fprintf(stderr, "error: %s: %s %s\n", std, err, tmp);
      abort();
    }
  }
};


// template<typename T>
// bool LockBasedQueue<T>::dequeue_blocking(T *item) {
//   int rc;
//   while (true) {
//     rc = pthread_mutex_lock(global_lock_);
//     check_error("pthread_mutex_lock", rc);
//     while (head_ == tail_) {
//       pthread_cond_wait(enqueue_cond_, global_lock_);
//     }
//     assert(head_ != tail_);
//     *item = head_->next->value;
//     head_ = head_->next;
//     rc = pthread_mutex_unlock(global_lock_);
//     check_error("pthread_mutex_unlock", rc);
//     return true;
//   }
// }

// template<typename T>
// bool LockBasedQueue<T>::dequeue_timeout(T *item, uint64_t timeout_ms) {
//   int rc;
//   struct timeval tp;
//   struct timespec ts;
//   uint64_t tmp_nsec;

//   rc = gettimeofday(&tp, NULL);
//   check_error("gettimeofday", rc);
//   ts.tv_sec = tp.tv_sec;
//   ts.tv_nsec = tp.tv_usec * 1000;
//   tmp_nsec = ts.tv_nsec;
//   tmp_nsec += timeout_ms * 1000000;
//   if (tmp_nsec >= 1000000000) {
//     ts.tv_sec += tmp_nsec / 1000000000;
//     ts.tv_nsec = tmp_nsec % 1000000000;
//   } else {
//     ts.tv_nsec = tmp_nsec;
//   }

//   while (true) {
//     rc =pthread_mutex_lock(global_lock_);
//     check_error("pthread_mutex_lock", rc);
//     while (head_ == tail_) {
//       rc = pthread_cond_timedwait(enqueue_cond_, global_lock_, &ts);
//       if (rc == ETIMEDOUT) {
//         rc = pthread_mutex_unlock(global_lock_);
//         check_error("pthread_mutex_unlock", rc);
//         return false;
//       }
//       check_error("pthread_cond_timedwait", rc);
//     }
//     assert(head_ != tail_);
//     *item = head_->next->value;
//     head_ = head_->next;
//     rc = pthread_mutex_unlock(global_lock_);
//     check_error("pthread_mutex_unlock", rc);
//     return true;
//   }
// }

#endif  // SCAL_DATASTRUCTURES_LOCKBASED_PRIORITY_QUEUE_
