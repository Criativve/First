"""
from dir1 import file2
file2.func()
import mydir

mydir.listing(file2)

"""
class C1():
    def setname(self, who):
        self.name = who

I1 = C1()
I2 = C1()

I1.setname('tristan')
I2.setname('grim')

print(I1.name, I2.name)