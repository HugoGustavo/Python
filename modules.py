import sys
def fib(n):
    result = []
    (a,b) = (0,1);
    while( b < n ):
        result.append(b);
        (a,b) = (b, a+b);
    return result;

if ( __name__ == "__main__" ):
    f = fib(100);
    print(f);

print(sys.path)

import math
content = dir(math);
print(content);
print();

import Phone
Phone.Pots();
Phone.Isdn();
Phone.G3();