fo = open("foo.txt", "wb");
print("Name of the file: ", fo.name);
print("Closed or not: ", fo.closed);
print("Opening mode: ", fo.mode);
fo.close();

fo = open("foo.txt", "w");
fo.write("Python is a great language.\nYeah its.great!!\n");
fo.close();
print();

fo = open("foo.txt", "r+");
str = fo.read(10);
print("Read String is: ", str);
fo.close();
print();

fo = open("foo.txt", "r+");
str = fo.read(10);
print("Read String is: ", str);

position = fo.tell();
print("Current file position: ", position);

position = fo.seek(0,0);
str = fo.read(10);
print("Again read String is: ", str);
fo.close();
print();

import os
os.rename("foo.txt", "foo_rename.txt");
print();

os.remove("foo_rename.txt");
print();

os.mkdir("teste");
print();

os.chdir("C:\\Users\\hugog\\eclipse-workspace\\python\\teste");
print();

import os
print(os.getcwd());
print();

os.chdir("C:\\Users\\hugog\\eclipse-workspace\\python\\");
os.rmdir("C:\\Users\\hugog\\eclipse-workspace\\python\\teste");
