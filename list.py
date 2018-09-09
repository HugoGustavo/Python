list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1,2,3,4,5];
list3 = ["a", "b", "c", "d"];

print("list1[0]  : ", list1[0]);
print("list2[1:5]: ", list1[1:5]);

list1 = ['physics', 'chemistry', 1997, 2000];
print("Value avaliable at index 2: ", list1[2]);
list1[2] = 2001;
print("New value available at index 2 :", list1[2]);
print();

list1 = ['physics', 'chemistry', 1997, 2000];
print(list1);
del(list1[2]);
print("After deleting value at index 2 : ", list1);

list1, list2 = [123,'xyz'], [456, 'abc'];

#print (cmp(list1, list2));
#print (cmp(list2, lista1));
#list3 = list2 + [786];
#print (cmp(list2, list2));
print();

list1 = ['physics', 'chemistry', 'maths'];
print(len(list1));

list2=range(5);
print(len(list2));
print();

list1, list2 = ['C++', 'Java', 'Python'], [456,700,200];
print("Max value element: ", max(list1));
print("Max value element: ", max(list2));
print();

list1, list2 = ['C++', 'Java', 'Python'], [456,700,200];
print("min value element: ", min(list1));
print("min value element: ", min(list2));
print();

aTuple = (123,'C++', 'Java', 'Python');
list1 = list(aTuple);
print("List elements: ", list1);
str = "Hello World";
list1 = list(str);
print("List elements: ", list2);

list1 = ['C++', 'Java', 'Python'];
list1.append('C#');
print('updated list: ', list1);
print();

aList = [123,'xyz','zara','abc',123];
print("Count for 123: ", aList.count(123));
print("Count for zara: ", aList.count('zara'));
print();

list1 = ['physics', 'chemistry', 'maths'];
list2 = list(range(5));
list1.extend(list2);
print('Extend List: ', list1);
print();

list1 = ['physics', 'chemistry', 'maths'];
print('Index of chemistry ', list1.index('chemistry'));
#print('Index of C# ', list1.index('C#'));
print();

list1 = ['physics', 'chemistry', 'maths'];
list1.insert(1, 'Biology');
print('Final list: ', list1);
print();

list1 = ['physics', 'Biology', 'chemistry', 'maths'];
list1.pop();
print("list now: ", list1);

list1.pop(1)
print('list now: ', list1);
print();

list1 = ['physics', 'Biology', 'chemistry', 'maths'];
list1.remove('Biology');
print('list now: ', list1);
list1.remove('maths');
print('list now: ', list1);
print();

list1 = ['physics', 'Biology', 'chemistry', 'maths'];
list1.reverse();
print('list now: ', list1);
print();

list1 = ['physics', 'Biology', 'chemistry', 'maths'];
list1.sort();
print('list now: ', list1);
print();