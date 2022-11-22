# --------------- iterators -------------
# create an iterator
class Numbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a = self.a + 1
        return x
    
myclass = Numbers()

myiter = iter(myclass);

print(next(myiter))

arr1 = [10,2,3,4,5];
it1 = iter(arr1);

print(next(it1))

