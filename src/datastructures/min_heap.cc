#include <cinttypes>
#include <iostream>
#include "min_heap.h"

min_heap::min_heap (uint64_t capacity)
  : size(0), capacity(capacity), values(new uint64_t[capacity]) {}

min_heap::~min_heap() noexcept {
  delete[] values;
}

void min_heap::heapify () {
  for (uint64_t i = size-1; i >= 0; --i) {
    bubble_down(i);
  }
}

void min_heap::bubble_down (uint64_t index) {
  uint64_t leftChildIndex = 2*index + 1;
  uint64_t rightChildIndex = 2*index + 2;

  if (leftChildIndex >= size) return; //index is a leaf

  uint64_t minIndex = index;

  if (values[index] > values[leftChildIndex]) {
    minIndex = leftChildIndex;
  }
    
  if ((rightChildIndex < size) &&
      (values[minIndex] > values[rightChildIndex])) {
    minIndex = rightChildIndex;
  }

  if (minIndex != index) {
    //need to swap
    uint64_t temp = values[index];
    values[index] = values[minIndex];
    values[minIndex] = temp;
    bubble_down(minIndex);
  }
}

void min_heap::bubble_up (uint64_t index) {
  if (index == 0) return;

  uint64_t parentIndex = (index-1)/2;

  if (values[parentIndex] > values[index]) {
    uint64_t temp = values[parentIndex];
    values[parentIndex] = values[index];
    values[index] = temp;
    bubble_up(parentIndex);
  }
}

void min_heap::insert (uint64_t value) {
  if (size == capacity) {
    abort();
  }
  values[size] = value;

  bubble_up(size++);
}

uint64_t min_heap::get_min () const {
  return values[0];
}
    
void min_heap::delete_min () {
  if (size == 0) return;
  
  values[0] = values[--size];
  
  bubble_down(0);
}

bool min_heap::empty() const {
  return size == 0;
}
