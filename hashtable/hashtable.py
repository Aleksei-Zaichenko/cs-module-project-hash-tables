class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity if capacity >= MIN_CAPACITY else MIN_CAPACITY
        self.table = [None] * capacity
        self.numOfOccupiedSlots = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return (self.numOfOccupiedSlots / self.capacity)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash_var = 5381
        for c in key:
            hash_var = (hash_var * 33) + ord(c)#digital representation of c 
        return hash_var

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Your code here
        index = self.hash_index(key)#2

        newNode = HashTableEntry(key, value)
        newNode.set_next(self.table[index])#2
        self.table[index] = newNode

        self.numOfOccupiedSlots += 1
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current = self.table[index]

        if current != None:

            self.numOfOccupiedSlots -= 1

            # if value to be removed is the head of the linked list
            if (current.get_key() == key):
                self.table[index] = current.get_next()
                current = None
                return

            # if value to be removed is not the head of the linked list

            prevNode = current
            while current:
                if (current.get_key() == key):
                    prevNode.set_next(current.get_next())
                    current = None
                    return
                prevNode = current
                current = current.get_next()

        # value to be removed was not found
        print('Warning: the key is not found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current = self.table[index]

        while current:
            if (current.get_key() == key):
                return current.get_value()
            current = current.get_next()

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        if new_capacity >= MIN_CAPACITY:#which is 8
            tempTable = self.table
            self.table = [None] * new_capacity#example 16, 
            self.capacity = new_capacity

            for item in tempTable:#always head 
                current = item
                while current:
                    self.put(current.get_key(),current.get_value())
                    current = current.get_next()
                    

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    
    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
