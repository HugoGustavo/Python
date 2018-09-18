def printme(str):
    "This prints a passed string into this function"
    print(str)
    return

printme('This is first call to user defined function!');
printme('Again second call to the same function');
print();

def changeme(mylist):
    "This changes a passed list into this function"
    print('Values inside the function before change: ', mylist);
    mylist[2] = 50;
    print('Values inside the function after change: ', mylist);
    return

mylist = [10,20,30];
changeme(mylist);
print('Values outside the function: ', mylist);
print();

def changeme2(mylist):
    "This changes a passed list into this function"
    mylist = [1,2,3,4];
    print("Value inside the function: ", mylist);
    return;

mylist = [10,20,30];
changeme2(mylist);
print('Values outside the function: ', mylist);
print();

printme(str="My String");
print();

def printinfo(name, age):
    "This prints a passed info into this function"
    print("Name: ", name);
    print("Age : ", age);
    return;

printinfo(age=50, name="miki");
print();

def printinfo2(name, age=35):
    "This prints a passed info this function"
    print("Name: ", name);
    print("Age : ", age);
    return;

printinfo2(age=50, name="miki");
printinfo2(name="miki");
print();

def printinfo3(arg1, *vartuple):
    "This prints a variable passed arguments"
    print("Output is: ");
    print(arg1);

    for var in vartuple:
        print(var);
    return;

printinfo3(10);
printinfo3(70,60,50);
print();

sum = lambda arg1, arg2 : arg1 + arg2
print("Value of total: ", sum(10,20));
print("Value of total: ", sum(20,20));
print();

def sum(arg1, arg2):
    total = arg1 + arg2;
    print('Inside the function: ', total);
    return total;

total = sum(10,20);
print('Outside the function: ', total);
print();

total = 0;
def sum2(arg1, arg2):
    total = arg1 + arg2;
    print("Inside the function local total: ", total);
    return total;

sum2(10, 20);
print("Outside the function global total: ", total);
print();