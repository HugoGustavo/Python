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