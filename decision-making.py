var1 = 100;
if var1:
    print("1 - Got a true expression value");
    print(var1);

var2 = 0;
if (var2):
    print("2 - Got a true expression value");
    print(var2);
print("Good bye!");

amount = int(input("Enter amount: "));
if ( amount < 1000 ):
    discount = amount*0.05;
    print("Discount: ", discount);

elif amount < 5000:
    discount = amount * 0.1;
    print("Discount: ", discount);

else:
    discount = amount * 0.15;
    print("Discount: ", discount);

print("Net payable: ", amount-discount);

num = int(input("Enter number: "));
if ( num % 2 == 0 ):
    if ( num % 3 == 0):
        print("Divisible by 3 and 2");
    else:
        print("Divisible by 2 not divisible by 3");
else:
    if ( num % 3 == 0):
        print("Divisible by 3 not divisible by 2");
    else:
        print("Not divisible by 2 not divisble by 3");