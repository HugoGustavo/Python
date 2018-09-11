dict1 = {
    'Name':'Zara',
    'Age':7,
    'Class':'First'
}

print("dict1['Name']: ", dict1['Name']);
print("dict1['Age']: ", dict1['Age']);
print();

dict1 = {
    'Name':'Zara',
    'Age':7,
    'Class':'First'
}
dict1['Age']=8
dict1['School']="DPS School"
print("dict1['Age']: ", dict1['Age']);
print("dict1['School']: ", dict1['School']);
print();

dict1 = {
    'Name':'Zara',
    'Age':7,
    'Class':'First'
}

del dict1['Name'];
dict1.clear();
del dict1;
#print ("dict1['Age']: ", dict1['Age']);
#print ("dict1['School']: ", dict1['School']);
print();

dict1 = {
    'Name':'Zara',
    'Age':7,
    'Name':'Manni'
};
print("dict1['Name']: ", dict1['Name']);
print();

# dict1 = {
#    ['Name']:'Zara',
#    'Age':7
# }
# print("dict1['Name']: ", dict1['Name']);

dict1 = {
    'Name':'Manni',
    'Age':7,
    'Class':'First'
};
print("Length: %d" % len(dict1));
print();

dict1 = {
    'Name':'Manni',
    'Age':7,
    'Class':'First'
};
print("Equivalent String : %s" % str(dict1));
print();

dict1 = {
    'Name':'Manni',
    'Age':7,
    'Class':'First'
};
print("Variable Type: %s" % type(dict1));
print();

dict1 = {
    'Name':'Zara',
    'Age':7
}
print("Start Len: ", len(dict1));
dict1.clear();
print("End Len: ", len(dict1));
print();

dict11 = {
    'Name':'Manni',
    'Age':7,
    'Class':'First'
}
dict12 = dict11.copy();
print("New Dictionary: ", dict12);
print();

seq = ('name', 'age', 'sex');
dict1 = dict.fromkeys(seq);
print("New Dictionary: ", str(dict1));
dict1 = dict.fromkeys(seq, 10);
print("New Dictionary: ", str(dict1));
print();

dict1 = {
    'Name':'Zara',
    'Age':27
}

print('Value: ', dict1.get('Age'));
print('Value: ', dict1.get('Sex', "NA"));
print();

dict1 = {
    'Name':'Zara',
    'Age':7
}
# Os metodos abaixo foram retirados do python 3
#print('Value: ', dict1.has_key('Age'));
#print('Value: ', dict1.has_key('Sex'));
print('Value: ', dict1.items());
print();

dict1 = {
    'Name':'Zara',
    'Age':7
}
print('Value: ', dict1.keys());
print();

dict1 = {
    'Name':'Zara',
    'Age':7
}
print('Value: ', dict1.setdefault('Age', None));
print('Value: ', dict1.setdefault('Sex', None));
print(dict1);
print();

dict1 = {
    'Name':'Zara',
    'Age':7
}
dict2 = {
    'Sex':'female'
}

dict1.update(dict2);
print('Updated dict: ', dict1);
print();

dict1 = {
    'Sex':'female',
    'Age':7,
    'Name':'Zara'
}
print('Values: ', list(dict1.values()));
print();