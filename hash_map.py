# Course: CS261 - Data Structures
# Assignment: 5
# Student: Taylor Googe
# Description: HashMap using a Dynamic Array and Linked List.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        TODO: Write this implementation
        """
        arr_len = self.buckets.length()
        for i in range(0, arr_len):
            temp_ll = self.buckets.get_at_index(i)
            # needs to be changed
            temp_ll.head = None

        self.size = 0

    def get(self, key: str) -> object:
        """
        This function takes a key and returns the value associated with that key.
        :param key: Key to be search for
        :return: Value or None
        """
        arr_length = self.buckets.length()
        hash_val = self.hash_function(key) % arr_length

        temp_ll = self.buckets.get_at_index(hash_val)
        contains_key = temp_ll.contains(key)


        if contains_key:
            return contains_key.value
        else:
            return None

    def put(self, key: str, value: object) -> None:
        """
        This function takes a key and value and stores it in the HashMap.
        :param key:
        :param value:
        :return: None
        """

        replace_node = None
        arr_length = self.buckets.length()

        for i in range(0,arr_length):
            temp_ll = self.buckets.get_at_index(i)
            if temp_ll.contains(key):
                replace_node = temp_ll.contains(key)

        if replace_node:
            replace_node.value = value
        else:
            hash_val = self.hash_function(key) % arr_length
            temp_ll = self.buckets.get_at_index(hash_val)
            temp_ll.insert(key, value)
            self.size += 1

    def remove(self, key: str) -> None:
        """
        This function takes a key and removes the first value associated with that ley.
        :param key: Key to be searched for.
        :return: None
        """
        arr_length = self.buckets.length()
        hash_val = self.hash_function(key) % arr_length
        temp_ll = self.buckets.get_at_index(hash_val)

        if temp_ll.contains(key):
            temp_ll.remove(key)
            self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        This function returns whether the passed key is present in the HashMap.
        :param key: Key to be searched for.
        :return: True or False
        """
        arr_length = self.buckets.length()
        hash_val = self.hash_function(key) % arr_length
        temp_ll = self.buckets.get_at_index(hash_val)
        contains_key = temp_ll.contains(key)

        if contains_key:
            return True
        else:
            return False

    def empty_buckets(self) -> int:
        """
        This function returns the number of empty buckets currently in the HashMap.
        :return: Number of buckets (int)
        """
        counter = 0
        arr_len = self.buckets.length()

        for i in range(0,arr_len):
            temp_ll = self.buckets.get_at_index(i)
            if temp_ll.length() == 0:
                counter += 1
        return counter

    def table_load(self) -> float:
        """
        This function returns the current table load of the Hashmap
        :return: Table load (float)
        """
        elems = self.size
        num_buckets = self.buckets.length()

        return elems/ num_buckets

    def resize_table(self, new_capacity: int) -> None:
        """
        This function creates a new Hashmap with the passed capacity and rehashes the elements in the
        current HashMap.
        :param new_capacity: The new capacity of the HashMap(int).
        :return: None
        """

        if new_capacity< 1:
            return

        new_map = HashMap(new_capacity, self.hash_function)
        arr_len = self.buckets.length()


        for i in range(0,arr_len):
            temp_ll = self.buckets.get_at_index(i)

            for node in temp_ll:
                new_map.put(node.key, node.value)



        self.buckets = new_map.buckets
        self.size = new_map.size
        self.capacity = new_map.capacity


    def get_keys(self) -> DynamicArray:
        """
        This function returns a DynamicArray containing all keys currently in the HashMap.
        :return: DynamicArray
        """
        new_arr = DynamicArray()

        arr_len = self.buckets.length()

        for i in range(0, arr_len):
            temp_ll = self.buckets.get_at_index(i)
            for node in temp_ll:
                new_arr.append(node.key)


        return new_arr




# BASIC TESTING
if __name__ == "__main__":
    pass
    #
    # print("\nPDF - empty_buckets example 1")
    # print("-----------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 30)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key4', 40)
    # print(m.empty_buckets(), m.size, m.capacity)
    # #
    # #

    # print("\nPDF - empty_buckets example 2")
    # print("-----------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('key' + str(i), i * 100)
    #     if i % 30 == 0:
    #         print(m.empty_buckets(), m.size, m.capacity)
    # #
    # #
    # print("\nPDF - table_load example 1")
    # print("--------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.table_load())
    # m.put('key1', 10)
    # print(m.table_load())
    # m.put('key2', 20)
    # print(m.table_load())
    # m.put('key1', 30)
    # print(m.table_load())
    #
    #
    # print("\nPDF - table_load example 2")
    # print("--------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(50):
    #     m.put('key' + str(i), i * 100)
    #     if i % 10 == 0:
    #         print(m.table_load(), m.size, m.capacity)
    #
    # print("\nPDF - clear example 1")
    # print("---------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key1', 30)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)
    #
    #
    # print("\nPDF - clear example 2")
    # print("---------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.size, m.capacity)
    # m.resize_table(100)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)
    #
    #
    # print("\nPDF - put example 1")
    # print("-------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('str' + str(i), i * 100)
    #     if i % 25 == 24:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)
    #
    # #
    #
    # print("\nPDF - put example 2")
    # print("-------------------")
    # m = HashMap(40, hash_function_2)
    # for i in range(50):
    #     m.put('str' + str(i // 3), i * 100)
    #     if i % 10 == 9:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)
    # #
    # #
    # print("\nPDF - contains_key example 1")
    # print("----------------------------")
    # m = HashMap(10, hash_function_1)
    # print(m.contains_key('key1'))
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key3', 30)
    # print(m.contains_key('key1'))
    # print(m.contains_key('key4'))
    # print(m.contains_key('key2'))
    # print(m.contains_key('key3'))
    # m.remove('key3')
    # print(m.contains_key('key3'))
    #
    #
    # print("\nPDF - contains_key example 2")
    # print("----------------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 20)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)
    # result = True
    # for key in keys:
    #     # all inserted keys must be present
    #     result &= m.contains_key(str(key))
    #     # NOT inserted keys must be absent
    #     result &= not m.contains_key(str(key + 1))
    # print(result)
    #
    #
    # print("\nPDF - get example 1")
    # print("-------------------")
    # m = HashMap(30, hash_function_1)
    # print(m.get('key'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    #
    #
    # print("\nPDF - get example 2")
    # print("-------------------")
    # m = HashMap(150, hash_function_2)
    # for i in range(200, 300, 7):
    #     m.put(str(i), i * 10)
    # print(m.size, m.capacity)
    # for i in range(200, 300, 21):
    #     print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    #     print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)
    #
    #
    # print("\nPDF - remove example 1")
    # print("----------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.get('key1'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    # m.remove('key1')
    # print(m.get('key1'))
    # m.remove('key4')
    #
    # #
    # print("\nPDF - resize example 1")
    # print("----------------------")
    # m = HashMap(20, hash_function_1)
    # m.put('key1', 10)
    # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    # m.resize_table(30)
    # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    # #
    # #
    # print("\nPDF - resize example 2")
    # print("----------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 13)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)
    #
    # for capacity in range(111, 1000, 117):
    #     m.resize_table(capacity)
    #
    #     m.put('some key', 'some value')
    #     result = m.contains_key('some key')
    #     m.remove('some key')
    #
    #     for key in keys:
    #         result &= m.contains_key(str(key))
    #         result &= not m.contains_key(str(key + 1))
    #     print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))

    #

    # print("\nPDF - get_keys example 1")
    # print("------------------------")
    # m = HashMap(10, hash_function_2)
    # for i in range(100, 200, 10):
    #     m.put(str(i), str(i * 10))
    # print(m.get_keys())
    #
    # m.resize_table(1)
    # print(m.get_keys())
    #
    # m.put('200', '2000')
    # m.remove('100')
    # m.resize_table(2)
    # print(m.get_keys())

    # m = HashMap(10, hash_function_1)
    # t = HashMap(10, hash_function_2)
    # for i in range(50,61):
    #     m.put(str(i), str(i*10))
    #     t.put(str(i), str(i * 10))
    #
    # print("m",m.table_load())
    # print("t", t.table_load())

    # print("m", m.empty_buckets())
    # print("t",t.empty_buckets())


