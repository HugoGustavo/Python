print("abs(-45)   : ", abs(-45));
print("abs(100.12): ", abs(100.12));
print();

import math;
print("Math.ceil(-45.17) : ", math.ceil(-45.17));
print("Math.ceil(100.12) : ", math.ceil(100.12));
print("Math.ceil(100.72) : ", math.ceil(100.72));
print("Math.ceil(math.pi): ", math.ceil(math.pi));
print();

print("Math.exp(-45.17) : ", math.exp(-45.17));
print("Math.exp(100.12) : ", math.exp(100.12));
print("Math.exp(100.72) : ", math.exp(100.72));
print("Math.exp(math.pi): ", math.exp(math.pi));
print();

print("Math.fabs(-45.17) : ", math.fabs(-45.17));
print("Math.fabs(100.12) : ", math.fabs(100.12));
print("Math.fabs(100.72) : ", math.fabs(100.72));
print("Math.fabs(math.pi): ", math.fabs(math.pi));
print();


print("Math.floor(-45.17)  : ", math.floor(-45.17));
print("Math.floor(100.12)  : ", math.floor(100.12));
print("Math.floor(100.72)  : ", math.floor(100.72));
print("Math.flooar(math.pi): ", math.floor(math.pi));
print();

print("Math.log(100.12) : ", math.log(100.12));
print("Math.log(100.72) : ", math.log(100.72));
print("Math.log(math.pi): ", math.log(math.pi));
print();

print("Math.log10(100.12) : ", math.log10(100.12));
print("Math.log10(100.72) : ", math.log10(100.72));
print("Math.log10(119)    : ", math.log10(119));
print("Math.log10(math.pi): ", math.log10(math.pi));
print();

print("Max(80,100,1000): ", max(80,100,1000));
print("Max(-20,100,400): ", max(-20,100,400));
print("Max(-80,-20,-10): ", max(-80,-20,-10));
print("Max(0,100,-400,200) : ", max(0,100,-400,200));
print();

print("Min(80,100,1000): ", min(80,100,1000));
print("Min(-20,100,400): ", min(-20,100,400));
print("Min(-80,-20,-10): ", min(-80,-20,-10));
print("Min(0, 100,-400): ", min(0,100,-400));
print();

print("Math.modf(100.12) : ", math.modf(100.12));
print("Math.modf(100.72) : ", math.modf(100.72));
print("Math.modf(119)    : ", math.modf(119));
print("Math.modf(math.pi): ", math.modf(math.pi));
print();

print("Math.pow(100,2) : ", math.pow(100,2));
print("Math.pow(100,-2): ", math.pow(100,-2));
print("Math.pow(2, 4)  : ", math.pow(2,4));
print("Math.pow(3, 0)  : ", math.pow(3,0));
print();

print("Round(70.23456)    : ", round(70.23456));
print("Round(56.569,1)    : ", round(56.659,1));
print("Round(80.264,2)    : ", round(80.264,2));
print("Round(100.000056,3): ", round(100.000056,3));
print("Round(-100.000056,3): ", round(-100.000056, 3));
print();

print("Math.sqrt(100)    : ", math.sqrt(100));
print("Math.sqrt(7)      : ", math.sqrt(7));
print("Math.sqrt(math.pi): ", math.sqrt(math.pi));
print();

import random;
print("Returns a random number from range(100)           : ", random.choice(range(100)));
print("Returns random element from lista [1,2,3,5,9]     : ", random.choice([1,2,3,5,9]));
print("Returns random character from string 'Hello World': ", random.choice('Hello World'));
print();

print("Randrange(1,100,2): ", random.randrange(1,100,2));
print("Randrange(100)    : ", random.randrange(100));
print();

print("Random(): ", random.random());
print("Random(): ", random.random());
print();

random.seed();
print("Random number with default seed: ", random.random());
random.seed(10);
print("Random number with int seed: ", random.random());
random.seed("hello", 2);
print("Random number with string seed: ", random.random());
print();

list = [20,16,10,5];
random.shuffle(list);
print("Reshuffled list: ", list);
random.shuffle(list);
print("Reshuffled list: ", list);
print();

print("Random Float Uniform (5,10): ", random.uniform(5,10));
print("Random Float Uniform (7,14): ", random.uniform(7,14));
print();

print("acos(0.64): ", math.acos(0.64));
print("asin(0.64): ", math.asin(0.64));
print("atan(0.64): ", math.atan(0.64));
print("cos(0.64): ", math.cos(0.64));
print("hypot(3,2): ", math.hypot(3,2));
print("hypot(-3,2): ", math.hypot(-3,2));
print("sin(math.pi):" , math.sin(math.pi));
print("tan(math.pi/4): ", math.tan(math.pi/4));
print("degrees(math.pi/2): ", math.degrees(math.pi/2));
print("radians(90.0): ", math.radians(90.0));
print();


