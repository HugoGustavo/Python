counter = 100 # An integer assignment
miles = 1000.0 # A float point
name = "John" # A string

print(counter);
print(miles);
print(name);

a = b = c = 1;

a, b, c = 1, 2, "john"

print(a);
print(b);
print(c);

var1 = 1;
var2 = 10;

print(var1,var2);

# del var1, var2;
# print(var1,var2);

str = "Hello World!";
print(str);
print(str[0]);
print(str[2:5]);
print(str[2:])
print(str * 2)
print(str + "TEST")

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john'];

print("\nLista de Objetos");
print(list);
print(list[0]);
print(list[1:3]);
print(list[2:]);
print(tinylist*2);
print(list + tinylist);

print("\nTuplas");
tuple = ( 'abcd', 786, 2.23, 'john', 70.2 )
tinytuple = (123, 'john');
print(tuple);
print(tuple[0]);
print(tuple[1:3]);
print(tuple[2:]);
print(tinytuple*2);
print(tuple+tinytuple);

print("\nDicionario");
dict = {}
dict['one'] = "This is one";
dict[2] = "This is two";

tinydict = {
    'name':'john',
    'code':6734,
    'dept': 'sales'
}

print(dict['one']);
print(dict[2]);
print(tinydict);
print(tinydict.keys());
print(tinydict.values());