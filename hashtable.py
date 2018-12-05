#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        all_buckets = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_buckets.append(value)
        return all_buckets

    def items(self):
        """Returns a list of all items (key-value pairs) in this hash table.
        Running time: O(bl) Where b is buckets and l is length of self.buckets"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Returns the number of key-value entries by traversing its buckets.
        Running time: O(b) Where b is the number of buckets"""
        all_entries = 0
        for bucket in self.buckets:
            all_entries += bucket.length()
        return all_entries

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for bucket_key, bucket_value in bucket.items():
            if bucket_key == key:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for bucket_key, bucket_value in self.buckets[index].items():
            if bucket_key == key:
                return bucket_value
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        #entry = bucket.find(lambda bucket_key_value: bucket_key_value[0] == key)
        if self.contains(key):
            self.delete(key)
            # self.size -= 1
        bucket.prepend((key, value))
        #self.size += 1
        # for bucket_key, bucket_value in bucket.items:
        #     if bucket_key == key:
        #         bucket_value = value
        #         return
        # raise KeyError('Key not found: {}'.format(key))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        bucket = self.buckets[self._bucket_index(key)]
        bucket_item = bucket.find(lambda data: data[0] == key)
        if bucket_item:
            bucket.delete(bucket_item)
            return
        raise KeyError('Key not found: {}'.format(key))
        # Hint: raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
