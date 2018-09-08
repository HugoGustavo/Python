#from string import maketrans;

var1 = 'Hello World!';
var2 = "Python Programming";

print("var1[0]: ", var1[0]);
print("var2[1:5]: ", var2[1:5]);
print();

print("Updated String :- ", var1[:6] + "Python");
print();

a = "Hello";
print(a[1:4]);
print();

print('My name is %s and weight is %d kg!' % ('Zara', 21));
print();

para_str = """ this is a long string tath is made up of
several lines and non-printable characters such as
TAB( \t ) and they will show up that way when displayed.
NEWLINEs within the stirng, whether explicitly given like
this within the bracktes [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str);
print();

print('C:\\nowhere');
print(r'C:\\nowhere');
print();

str = "this is string example....wow!!!";
print("str.capitalize(): ", str.capitalize());
print();

str = "this is string example....wow!!!";
print("str.center(40, 'a'): ", str.center(40, 'a'));
print();

str = "this is string example....wow!!!";
sub = 'i';
print("str.count('i'): ", str.count(sub));
sub = 'exam';
print("str.count('exam', 10, 40): ", str.count(sub, 10, 40));
print();

str = 'this is string example...wow!!!';
suffix = '!!';
print(str.endswith(suffix));
print(str.endswith(suffix,20));
print();

suffix = 'exam';
print(str.endswith(suffix));
print(str.endswith(suffix, 0, 19));
print();

str = "this is\tstring example....wow!!!";
print("Original string: " + str);
print("Default expanded tab: " + str.expandtabs());
print("Double expanded tab: " + str.expandtabs(16));
print();

str1 = "this is string example...wow!!!";
str2 = "exam";
print(str1.find(str2));
print(str1.find(str2, 10));
print(str1.find(str2, 40));
print();

str1 = "this is string example....wow!!!";
str2 = "exam";
print(str1.index(str2));
print(str1.index(str2, 10));
#print(str1.index(str2, 40));
print();

str = "this2016";
print("str.isalnum(): ", str.isalnum());
print("str.isalpha(): ", str.isalpha());
str = "this is string example....wow!!!";
print("str.isalnum(): ", str.isalnum());
print("str.isalpha() ", str.isalpha());
print();

str = "123456";
print(str.isdigit());
str = "this is string example....wow!!!";
print(str.isdigit());
print();

str = "THIS is string example....wow!!!";
print(str.islower());
str = "this is string example...wow!!!";
print(str.islower());
print();

str = "this2016";
print(str.isnumeric());
str = "23443434";
print(str.isnumeric());
print();

str = "          ";
print(str.isspace());

str = "This is string example...wow!!!";
print(str.isspace());
print();

str = "This Is String Example...Wow!!!";
print(str.istitle());

str = "This i string example...wow!!!";
print(str.istitle());
print();

str = 'THIS IS STRING EXAMPLE...WOW!!!';
print(str.isupper());
str = "THIS is string example....wow!!!";
print(str.isupper());
print();

s = "-";
seq = ("a", "b", "c");
print(s.join(seq));
print();

str = "thi is string example....wow!!!";
print("Length of string: ", len(str));
print();

str = "this is string example....wow!!!";
print(str.ljust(50,'*'));
print();

str = "THIS IS STRING EXAMPLE...WOW!!!";
print(str.lower());
print();

str = "         this is string example...wow!!!";
print(str.lstrip());
str = "***************this is string example....wow!!!******";
print(str.lstrip("*"));
print();

intab = "aieou";
outtab = "12345";
trantab = str.maketrans(intab, outtab);
str = "this is string example...wow!!!";
print(str.translate(trantab));
print();

str = "this is a string example....really!!!";
print("Max character: " + max(str));
str = "this is a string example...wow!!!";
print("Max character: " + max(str));
print();

str = "www.tutorialspoint.com";
print("Min character: " + min(str));
str = "TUTORIALSPOINT";
print("Min character: " + min(str));
print();

str = "this is example...wow!!! this is really string";
print(str.replace("is", "was"));
print(str.replace("is", "was", 3));
print();

str = 'this is really a string example...wow!!!';
str2 = "is";

print(str1.rfind(str2));
print(str1.rfind(str2, 0,10));
print(str1.rfind(str2,10,0));
print(str1.find(str2));
print(str1.find(str2, 0,0));
print(str1.find(str2, 10, 0));
print();

str1 = "this is really a string example....wow!!!";
str2 = "is";

print(str1.rindex(str2));
# print(str1.rindex(str2, 10));
print();


str = "this is string example...wow!!!";
print(str.rjust(50, "*"));
print();


str = "          this is string example...wow!!!         ";
print(str.rstrip());
str = "**************************this is string example...wow!!!****";
print(str.rstrip("*"));
print();

str = "this is string example....wow!!!";
print(str.split());
print(str.split('i', 1));
print(str.split('w'));
print();

str = "this is \nstring example....\nwow!!!";
print(str.splitlines());
print();

str = "this is string example....wow!!!";
print (str.startswith('this'));
print(str.startswith('string', 8));
print(str.startswith('this', 2, 4));
print();

str = "*******this is string example....wow!!!*******";
print(str.strip('*'));
print();

str = "this is string example....wow!!!";
print(str.swapcase());
str = "This Is String Example....WOW!!!";
print(str.swapcase());
print();

str = "this is string example...wow!!!";
print(str.title());
print();

intab = "aieou";
outtab = "12345";
trantab = str.maketrans(intab, outtab);
str = "this is string example...wow!!!";
print(str.translate(trantab));
print();

str = "this is string example....wow!!!";
print("str.upper: ", str.upper());
print();

str = "this is string example.... wow!!!";
print("str.zfill: ", str.zfill(40));
print("str.zfill: ", str.zfill(50));
print();