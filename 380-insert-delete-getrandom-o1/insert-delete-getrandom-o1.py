class RandomizedSet:

    def __init__(self):
        self.list = [] # just a list of values
        self.dict = {} # format: { value : index }

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.list.append(val)
            self.dict[val] = len(self.list)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            x = val
            # if we're removing 'x', and 'z' is last in list
            # find 'x' index
            xindex = self.dict[x]
            # swap 'x' and 'z' on list
            self.list[xindex], self.list[-1] = self.list[-1] , self.list[xindex]
                        # update 'z' index on dictionary
            self.dict[ self.list[xindex] ] = xindex
            # pop 'x' from list
            self.list.pop()

            # del 'x' from dictionary
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()