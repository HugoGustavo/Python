def KelvinToFahrenheit(Temperature):
    assert(Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273));
print(int(KelvinToFahrenheit(505.78)));
# print(KelvinToFahrenheit(-5))

try:
    fh = open("testfile", "w");
    fh.write("This is my test file for exception handling!");
except IOError:
    print("Error: can't find file or read data");
else:
    print("Written content in the file successfully");
    fh.close();

print()

try:
    fh = open("testfile", "w");
    fh.write("This is my test file for exception handling!");
finally:
    print("Error: can't find file or read data");
    fh.close()

try:
    fh = open("testfile", "w");
    try:
        fh.write("This is my test file for exception handling!!");
    finally:
        print("Going to close the file");
        fh.close()
except IOError:
    print("Error: can't find file or read data");

print();

def temp_convert(var):
    try:
        return int(var);
    except ValueError as Argument:
        print("The argument does not contain numbers ", Argument);

temp_convert("xyz");
print();
def functionName(level):
    if ( level < 1):
        raise Exception(level);
    return level;

try:
    l = functionName(-10);
    print("level = ", l);
except Exception as e:
    print("error in level argument ", e.args[0]);

print();

class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.args = arg;

try :
    raise NetworkError("Bad hostname");
except NetworkError as e:
    print(e.args);