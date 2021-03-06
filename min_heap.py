# Course: CS261 - Data Structures
# Assignment: 5
# Student: Taylor Googe
# Description: Minheap implementation using a dynamic array.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def has_left_child(self, node, da_length):
        if 2 * node + 1 >= da_length:
            return False
        else:
            return True

    def has_right_child(self, node, da_length):
        if 2 * node + 2 >= da_length:
            return False
        else:
            return True

    def add_helper(self, node, parent):
        """
        Helper function for add(). This function calls itself until the MinHeap property
        is fully satisfied.
        :param node: The node to be added.
        :param parent: Parent of the added node.
        :return: None
        """
        if self.heap.get_at_index(node) >= self.heap.get_at_index(parent) or node == 0:
            return
        else:

            next_loc = parent
            next_parent = int((next_loc - 1) / 2)
            self.heap.swap(node, parent)
            return self.add_helper(next_loc, next_parent)

    def add(self, node: object) -> None:
        """
        This function creates a new node and adds to the MinHeap.
        :param node: Node to be added to the MinHeap
        :return: None
        """
        self.heap.append(node)
        node_loc = self.heap.length()

        if node_loc == 1:
            pass
        else:
            node_loc = node_loc - 1
            node_parent = int((node_loc - 1) / 2)
            if self.heap.get_at_index(node_loc) < self.heap.get_at_index(node_parent):
                self.add_helper(node_loc, node_parent)
            else:
                return

    def get_min(self) -> object:
        """
        This function returns the root (smallest) node in the MinHeap.
        :return: Value of the smallest node.
        """
        if self.heap.length() == 0:
            raise MinHeapException
        else:
            return self.heap.get_at_index(0)

    def remove_min_helper(self, node=0):
        """
        This function is a helper function for remove_min(). This function removes the smallest
        node and restores the MinHeap property.
        :param node: Node to be removed.
        :return: None
        """

        l_child = 2 * node + 1
        r_child = 2 * node + 2

        if self.heap.length() == 2:
            if self.heap.get_at_index(1) < (self.heap.get_at_index(0)):
                self.heap.swap(0, 1)
            else:
                pass
        else:
            if l_child < self.heap.length() and r_child < self.heap.length():
                if self.heap.get_at_index(l_child) < self.heap.get_at_index(r_child):
                    self.heap.swap(node, l_child)
                    return self.remove_min_helper(l_child)
                else:
                    self.heap.swap(node, r_child)
                    return self.remove_min_helper(r_child)
            elif l_child == self.heap.length() - 1:  # last changes
                pass
            elif r_child == self.heap.length():
                self.heap.swap(node, l_child)
                return self.remove_min_helper(l_child)
            else:
                return

    def remove_min(self) -> object:
        """
        This function removes the smallest node and restores the MinHeap property.
        :return: Value of the returned node.
        """
        if self.heap.length() == 0:
            raise MinHeapException
        else:
            removed_node = self.heap.get_at_index(0)
            self.heap.swap(0, self.heap.length() - 1)
            self.heap.pop()
            self.remove_min_helper()
            return removed_node

    def build_heap_helper(self, da, non_leaf):
        """
        This function is a helper function for build_heap(). This function takes a dynamic array
        and builds a heap that satisfies the MinHeap property.
        :param da: Dynamic Array
        :param non_leaf: The non-leaf node currently being heapified.
        :return: None
        """

        if non_leaf >= 0:
            if self.has_right_child(non_leaf, da.length()) is True and self.has_left_child(non_leaf, da.length()) is True:
                if da.get_at_index(2 * non_leaf + 1) < da.get_at_index(2 * non_leaf + 2):
                    swap = 2 * non_leaf + 1
                else:
                    swap = 2 * non_leaf + 2

                if da.get_at_index(non_leaf) > da.get_at_index(swap):
                    da.swap(non_leaf, swap)
                self.build_heap_helper(da, non_leaf - 1)
            elif self.has_left_child(non_leaf, da.length()) is True:
                if da.get_at_index(non_leaf) > da.get_at_index(2 * non_leaf + 1):
                    da.swap(non_leaf, 2 * non_leaf + 1)
                self.build_heap_helper(da, non_leaf - 1)

    def build_heap(self, da: DynamicArray) -> None:
        """
        This function takes a DynamicArray object and builds a heap that satisfies the MinHeap
        property.
        :param da: Dynamic Array
        :return: None
        """

        non_leaf = int((da.length() / 2) - 1)
        da_copy = DynamicArray()

        for i in range(0, da.length()):
            temp_val = da.get_at_index(i)
            da_copy.append(temp_val)

        self.build_heap_helper(da_copy, non_leaf)

        self.heap = da_copy
