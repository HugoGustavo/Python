class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name;
        self.salary = salary;
        Employee.empCount +=1;
    
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount);
    
    def displayEmployee(self):
        print ("Name: ", self.name, ", Salary: ", self.salary);

emp1 = Employee("Zara", 2000);
emp2 = Employee("Manni", 5000);
emp2.displayEmployee();
emp2.displayEmployee();
emp1.displayCount();
print();

hasattr(emp1, 'salary');
getattr(emp1, 'salary');
setattr(emp1, 'salary', 7000);
delattr(emp1, 'salary');
print();

emp1 = Employee("Zara", 2000);
emp2 = Employee("Manni", 5000);
print("Employee.__doc__   : ", Employee.__doc__);
print("Employee.__name__  : ", Employee.__name__);
print("Employee.__module__: ", Employee.__module__);
print("Employee.__bases__ : ", Employee.__bases__);
print("Employee.__dict__  : ", Employee.__dict__);
print();


class Point:
    def __init__(self, x=0, y=0):
        self.x = x;
        self.y = y;
    
    def __del__(self):
        class_name = self.__class__.__name__;
        print(class_name, "destroyed");

pt1 = Point();
pt2 = pt1;
pt3 = pt1;
print( id(pt1), id(pt2), id(pt3) );
del (pt1);
del (pt2);
del (pt3);
print();


class Parent:
    parentAttr = 100;
    def __init__(self):
        print("Calling parent constructor");
    
    def parentMethod(self):
        print('Calling parent method');
    
    def setAttr(self, attr):
        Parent.parentAttr = attr;
    
    def getAttr(self):
        print("Parent attribute: ", Parent.parentAttr);
    
    def myMethod(self):
        print('Calling parent method');

class Child(Parent):
    def __init__(self):
        print("Calling child constructor");
    
    def childMethod(self):
        print('Calling child method');
    
    def myMethod(self):
        print('Calling child method');

c = Child();
c.childMethod();
c.parentMethod();
c.setAttr(200);
c.getAttr();
print();

c = Child();
c.myMethod();
print();

class Vector:
    def __init__(self, a, b):
        self.a = a;
        self.b = b;

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b);
    
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b);

v1 = Vector(2,10);
v2 = Vector(5,-2);
print(v1 + v2);
print();


class JustCounter:
    __secretCount = 0;

    def count(self):
        self.__secretCount+=1;
        print(self.__secretCount);

counter = JustCounter();
counter.count();
counter.count();
# print(counter.__secretCount);
print();