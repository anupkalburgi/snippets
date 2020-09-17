class MaxHeap:
    def __init__(self, maxSize):
        self.elements = []
        self.maxSize = maxSize
        self.count = 0
    
    '''
    there is a general formula for this
    parent = i -1 // 2 
    left_child = 2*i + 1
    right_child = 2*i + 2

    '''
    def extract(self):
        # Remove the 0th element and then have to adjust the rest, push down
        ret_value = self.elements[0]        
        self._shiftDown()
        print(f'remove {ret_value}')
        print(self.elements)
        return ret_value
    
    def _shiftDown(self):
        # copy the very last element to the the 0th index and then move that element down
        #and dec the count
        self.elements[0] = self.elements[self.count]
        self.elements.pop()
        self.count = self.count - 1
        # print(self.elements)
        ndx = 0
        left_child = (ndx * 2) + 1
        right_child = (ndx * 2) + 2
        # check that we are not crossing the array bounds and then if we one of the chid is bigger than the root
        while left_child <= self.count and right_child <= self.count and self.elements[ndx] < max(self.elements[left_child], self.elements[right_child]):
            # if the left_child is bigger
            if self.elements[left_child] > self.elements[right_child]:
                self.elements[left_child] , self.elements[ndx] = self.elements[ndx] , self.elements[left_child]
                ndx = left_child
                left_child = (2 * ndx) + 1
                right_child = (2 * ndx) + 2
                print( "l", ndx, left_child, right_child)
            else: # right child is greater
                self.elements[right_child], self.elements[ndx] = self.elements[ndx], self.elements[right_child]
                ndx = right_child
                left_child = (2 * ndx) + 1
                right_child = (2 * ndx) + 2
                print( "r", ndx, left_child, right_child)



    def insert(self, num):
        # insert the element at the very end and then move up the tree
        self.elements.append(num)
        self.count = len(self.elements) - 1
        self._shiftup()

    def _shiftup(self):
        #will have to be shifting up from the very end always, may be not let me find out
        ndx = self.count
        parent = (self.count - 1 ) // 2
        while parent >= 0 and self.elements[parent] < self.elements[ndx] : 
            # swap parent and ndx
            tmp = self.elements[ndx]
            self.elements[ndx] = self.elements[parent]
            self.elements[parent] = tmp
            ndx  = parent
            parent = (parent - 1) // 2

    def __str__(self):
        return str(self.elements)

    # def validate(self, parameter_list):
    #   Here i will have to check the if the heap property is held up right
    #     pass

    def capacity(self):
        return self.count
maxHeap = MaxHeap(10)
# print(maxHeap) ## empty
maxHeap.insert(100)
# print(maxHeap) ## 
maxHeap.insert(84)
# print(maxHeap) ## 
maxHeap.insert(71)
# print(maxHeap) ##  
maxHeap.insert(60)
# print(maxHeap) ## 
maxHeap.insert(23)
# print(maxHeap) ##
maxHeap.insert(12)
# print(maxHeap) ## 
maxHeap.insert(29)
# print(maxHeap) ## 
maxHeap.insert(1)
# print(maxHeap) ## 
maxHeap.insert(37)
# print(maxHeap) ## 
maxHeap.insert(4)
# print(maxHeap) ## 

maxHeap.insert(91)
print(maxHeap) ## 

print("------------------------------------------------------------")
maxHeap.extract()
# print(maxHeap) ##

maxHeap.extract()
# print(maxHeap) ##