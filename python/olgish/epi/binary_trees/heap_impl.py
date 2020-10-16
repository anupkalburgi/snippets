'''
Array is used for representing the heap
Heaps have to be fixed size always ?

given a list construct heap tree
Algo
1. allocate a new array of the input size and initilize it to something ? 
    - if do what would that be, supoorting negative numbers ? 
    - if we put a none, then we it increases the code complexity
    - if do not allocate then the formula for parent and child wont work

    Go with allocating the array and then checking for none

    The way we metigate this is by having to initilize a class, and then a count and maxCapactity , and this is bit odd, this will force use to have a Array defined
    and then everytime we have to heapify, we do it from count to the top

2. add element to the very end of the array - alloc[-1] = elm
     j = len(alloc) - 1
    while alloc[parent] < alloc[j]:
        swap(alloc[parent], alloc[j])
        j = l_floor(parent / 2)

'''

class Heap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.count = 0
        self.elements = [-1] * max_size # this will work only for the positive elements

    def insert(self, value):
        assert self.count <= self.max_size , "full capacity , cannot be added top the heap"
        self.count = self.count + 1
        self.elements[self.count-1] = value
        self.shift_up(self.count - 1)
    
    def shift_up(self, ndx):
        pndx = ndx // 2
        if self.elements[pndx] < self.elements[ndx]:
            self.elements[pndx], self.elements[ndx] = self.elements[ndx] , self.elements[pndx]
            self.shift_up(pndx)


    def extract(self):
        assert self.count >= 0 , "there should be some element to delete it" 
        top_val = self.elements[0]
        self.shift_down()
        self.count = self.count - 1
        return top_val

    def shift_down(self):
        ndx = 0
        while ndx < self.count -1:
            l = (2 * ndx + 1)
            r = (2 * ndx + 2)
            lch, rch = self.elements[l] , self.elements[r]
            if lch > rch:
                self.elements[ndx] =  self.elements[l]
                ndx = l
            else:
                self.elements[ndx] =  self.elements[r]
                ndx = r



heap = Heap(10)
heap.insert(6)
print(heap.elements)        
heap.insert(5)
print(heap.elements)        
heap.insert(4)
print(heap.elements)        
heap.insert(3)
print(heap.elements)        
print(heap.extract())
print(heap.elements)

