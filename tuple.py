tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1,2,3,4,5);
print("tup1[0]  : ", tup1[0]);
print("tup2[1:5]: ", tup2[1:5]);
print();

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

tup3 = tup1 + tup2;
print(tup3);

tup = ('physics', 'chemistry', 1997, 2000);
print(tup)
del (tup);
#print("After deleting tup: ", tup);
print();


tuple1, tuple2 = (123, 'xyz'), (456,'abc')
#print( cmp(tuple1, tuple2) );
#print( cmp(tuple2, tuple1) );
tuple3 = tuple2 + (786,);
#print( cmp(tuple2, tuple3) );

tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
print ('First tuple length: ', len(tuple1));
print ('Second tuple length: ', len(tuple2));
print();

tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (456,700,200)
print ("Max value element: ", max(tuple1));
print ("Max value element: ", max(tuple2));
print();

tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (46,700,200)
print("Min value element: ", min(tuple1));
print("Min value element: ", min(tuple2));
print();

list1 = ['maths', 'che', 'phy', 'bio']
tuple1 = tuple(list1)
print("tuple elements: ", tuple1)
print();