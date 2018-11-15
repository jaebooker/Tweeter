mylist = LinkedList()

mylist.append('a')
mylist.append('b')
mylist.append('c')

mylist.head.data  # => 'a'
mylist.tail.data  # => 'c'
mylist.find(lambda data: data > 'b')  # => 'c'
mylist.delete('a')
mylist.head.data  # => 'b'

myList = LinkedList()

myList.append('a')
myList.append('b')
myList.append('c')
myList.append('d')

myList.head.data
myList.tail.data
print(myList.find(lambda data: data > 'b'))
myList.delete('a')
myList.head.data
