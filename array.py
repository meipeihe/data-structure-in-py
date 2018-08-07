class Array:
    
    def __init__(self, capacity = 10):
        self.data = [None] * capacity
        self.size = 0

    def __str__(self):
        rt = "Size:{0},Capacity:{1}\n".format(self.size, len(self.data))
        rt += "["
        for i in self.data:
            rt += str(i) + ", "
        rt = rt[:-2] + "]"    
        return rt

    def getCapacity(self):
        return len(self.data)    

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0    

    def add(self, index, e):
        if self.size == len(self.data):
            raise Exception("Add failed. Array is full")
        if index < 0 or index > self.size:
            raise Exception("Add failed. Require index >= 0 and index <= size")    
        for i in reversed(range(index, self.size)):
            self.data[i+1] = self.data[i]
        self.data[index] = e
        self.size += 1   
    
    def addFirst(self, e):
        self.add(0, e)

    def addLast(self, e):
        self.add(self.size, e)

    def get(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Get failed. Index is illegal.")
        return self.data[index]

    def set(self, index, e):
        if index < 0 or index >= self.size:
            raise Exception("Set failed. Index is illegal.")
        self.data[index] = e        

    def contains(self, e):
        for i in self.data:
            if i == e:
                return True
        return False        


arr = Array()
print(arr)     
print("Capacity: ", arr.getCapacity())   
print("Size: ", arr.getSize())
print("IsEmpty: ", arr.isEmpty())

arr.add(0,1)
arr.add(0,2)
arr.add(0,3)
arr.add(2,10)
print(arr) 

arr.addFirst(8)

print(arr)

arr.addLast(20)

print(arr)

print("Get: ", arr.get(5))

arr.set(3,55)
print("Set: ", arr)

print("Contains: ", arr.contains(55))
print("Contains: ", arr.contains(52))



