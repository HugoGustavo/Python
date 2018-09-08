import re

line = "Cats are smarter tha dogs";

mathObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I);

if(mathObj):
    print("matchObj.group() : ", mathObj.group());
    print("matchObj.group(1): ", mathObj.group(1));
    print("matchObj.group(2): ", mathObj.group(2));
else:
    print("No match!");
print();

line = "Cats are smarter than dogs";

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I);
if(searchObj):
    print("searchObj.group() : ", searchObj.group());
    print("searchObj.group(1): ", searchObj.group(1));
    print("searchObj.group(2): ", searchObj.group(2));
else:
    print("Nothing found!!!");
print();

phone = "2004-959-559 # This is Phone Number";
num = re.sub(r'#.*$', "", phone);
print("Phone Num: ", num);

num = re.sub(r'\D', "", phone);
print("Phone Num: ", num);
print();