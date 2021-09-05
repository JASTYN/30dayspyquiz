class Student:
    
    count = 0
    def _init_(self, n,a):
        self._name =n
        self._age = a
        self._class_.count+=1
    def getAge(self):
        return self._age
    def getCount(self):
        return self._class_.count
    def _str_(self):
        return"Name: " + self.name + "\nAge: " + str(self.age)
#a = Student("Mickey mouse", 90)
a.getCount()
