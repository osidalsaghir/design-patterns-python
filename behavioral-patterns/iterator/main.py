# Concrete aggregate class
class MyList:
    def __init__(self):
        self._data = []

    def add_item(self, item):
        self._data.append(item)

    def __iter__(self):
        return MyListIterator(self._data)

# Concrete iterator class
class MyListIterator:
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._data):
            item = self._data[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

# Client code
if __name__ == "__main__":
    my_list = MyList()
    my_list.add_item("Item 1")
    my_list.add_item("Item 2")
    my_list.add_item("Item 3")

    # Iterating over the list using the iterator
    for item in my_list:
        print(item)
