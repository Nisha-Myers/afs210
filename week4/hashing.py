class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
         return key % self.size
        # Insert your hashing function code

    def rehash(self,key):
             return key // self.size
        # Insert your secondary hashing function code

    def put(self,key,data):
        hashvalue = self.hashfunction(key)
        if self.data[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(key)
                if self.data[nextslot] == None:
                    self.data[nextslot] = data
                    self.slots[nextslot] = key
                else:
                        print("I'm so exhaustd...")

        # Insert your code here to store key and data 

    def get(self,key):
        data = None
        position = self.hashfunction(key)
        # Insert your code here to get data by key

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'
# Store remaining input data
print(H.slots)
print(H.data)
print(H[52])

# print the slot values

# print the data values

# print the value for key 52

