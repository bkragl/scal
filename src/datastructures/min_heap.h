// A binary min-heap using a fixed-size array as back-end storage.

class min_heap
{
private:
  uint64_t size;
  uint64_t capacity;
  uint64_t* values;

  void bubble_down (const uint64_t index);
  void bubble_up (const uint64_t index);
  void heapify ();

  // Copy/move constructor/assignment operator not implemented at the moment.
  min_heap (const min_heap& other);
  min_heap& operator= (const min_heap& other);
  min_heap (min_heap&& other) noexcept;
  min_heap& operator= (min_heap&& other) noexcept;
  
public:
  min_heap (const uint64_t size);
  ~min_heap() noexcept;

  void insert (const uint64_t value);
  uint64_t get_min() const;
  void delete_min();
  bool empty () const;
};
