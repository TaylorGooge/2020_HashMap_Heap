These files are part of the portfolio project for Oregon State University's
Data Structures course from Fall 2020.
**************

a5_include.py was provided by the class is not my handiwork. It contains the base dynamic array class used in min_heap.py and the Linked List class used by hash_map.py

hash_map.py
***************
Contains two simple hash functions pre-written that can be altered in the hash_function_1 or hash_function_2 methods.

This program implements a HashMap utilizing a linked list as a data structure. A new hash map can be instantiated in the following way:
map = HashMap(x, hash_function) where X is the number of buckets to be included in the Map.

The HashMap class contains methods to clear the hashmap; get a value associated with a key; store a key, value pair; remove a key, value pair; search to determine whether the map contains a key; empty the hash map buckets; compute the current table load; resize the current table; and return keys.

min_heap.py
***************
This program builds a min heap using a dynamic array as a data structure. A new heap can be instantiated in the following way: 

array = DynamicArray[val1, val2, ...valk]
heap = MinHeap(array)

The MinHeap class contains methods to determine if the heap is empty; children of nodes; add node; get min node; remove min node; and build a heap from an array.