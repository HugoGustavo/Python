import sys;

count = 0;
while ( count < 9 ):
    print("The count is: ", count);
    count = count + 1;
print("Good Bye!");


#var = 1
#while(var == 1):
#    num = int(input("Enter a number: "));
#    print("You entered: ", num);
#print("Good Bye!");
#

count = 0;
while (count < 5):
    print(count, " is less than 5");
    count = count + 1;
else:
    print(count, " is not less than 5");

flag=1;
#while(flag): print ("Given flag is realy true!");
print("Good bye!");

for letter in 'Python':
    print('Current Letter: ', letter);
print();
fruits = [ 'banana', 'apple', 'mango' ]

for fruit in fruits:
    print('Current fruit: ', fruit);
print ("Good bye !");

for index in range(len(fruits)):
    print('Current fruit: ', fruits[index]);
print("Good bye!");

numbers = [11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if ( num % 2 == 0 ):
        print("The list contains an even number");
        break;
else:
    print('The list does not contain even number');

for i in range(1,11):
    for j in range(1,11):
        k = i * j;
        print(k, end=" ")
    print()

for letter in 'Python': # First Example
    if letter == 'h':
        break;
    print('Current Letter: ', letter);

var = 10
while ( var > 0 ):
    print('Current Letter: ', var);
    var = var - 1;
    if ( var == 5):
        break;
print ("Good bye!");

no = int(input('Any number: '));
numbers = [11,33,55,39,55,75,37,21,23,41,13];
for num in numbers:
    if ( num == no ):
        print('Number found in list');
        break;
else:
    print('Number not found in list');

for letter in 'Python':
    if letter == 'h':
        continue;
    print('Current Letter: ', letter);

var = 10;
while ( var > 0 ):
    var = var - 1;
    if ( var == 5 ):
        continue;
    print('Current variable value: ', var);
print("Good bye!");

for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block');
    print('Current Letter: ', letter);
print("Good bye!");

list = [1,2,3,4];
it = iter(list) #this builds an iterator object
print(next(it)) # prints next avaliable element in iterator
for x in it:
    print(x)
#while( True ):
#    try:
#        print(next(it));
#    except StopIteration:
#        print();

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if ( counter > n ):
            return
        yield a
        a, b = b, a+b
        counter += 1
f = fibonacci(5)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit();