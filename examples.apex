# APEX Programming Language - Example Programs
# MIT License
# Copyright (c) 2026 ToToAppsYT
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

# ========== EXAMPLE 1: Variables and Basic Operations ==========
let name = "APEX";
let version = 1.0;
let is_awesome = true;

print("Welcome to", name, "v" + str(version));
print("Awesome?", is_awesome);


# ========== EXAMPLE 2: Control Flow ==========
let number = 42;

if (number > 50) {
    print("Greater than 50");
} else if (number == 42) {
    print("The answer to everything!");
} else {
    print("Less than 50");
}


# ========== EXAMPLE 3: Loops ==========
# While loop
let count = 0;
while (count < 3) {
    print("Count:", count);
    let count = count + 1;
}

# For loop
print("For loop from 0 to 4:");
for (i: range(5)) {
    print("i =", i);
}


# ========== EXAMPLE 4: Functions ==========
func add(x, y) {
    return x + y;
}

func greet(name) {
    print("Hello, " + name + "!");
    return 42;
}

let sum = add(10, 20);
print("10 + 20 =", sum);

let result = greet("World");
print("Function returned:", result);


# ========== EXAMPLE 5: Lists ==========
let numbers = [1, 2, 3, 4, 5];
print("List:", numbers);
print("Length:", len(numbers));
print("First element:", numbers[0]);
print("Last element:", numbers[len(numbers) - 1]);

# List operations
let fruits = [];
push(fruits, "apple");
push(fruits, "banana");
print("Fruits:", fruits);


# ========== EXAMPLE 6: String Operations ==========
let str1 = "Hello";
let str2 = " World";
let combined = str1 + str2;
print(combined);
print("Length of message:", len(combined));
print("First character:", combined[0]);


# ========== EXAMPLE 7: Factorial (Recursion) ==========
func factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

print("5! =", factorial(5));
print("10! =", factorial(10));


# ========== EXAMPLE 8: Fibonacci ==========
func fibonacci(n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

print("Fibonacci sequence:");
for (i: range(8)) {
    print("fib(" + str(i) + ") =", fibonacci(i));
}


# ========== EXAMPLE 9: Boolean Logic ==========
let x = 10;
let y = 20;

if (x < y and y > 15) {
    print("Both conditions are true");
}

if (x > 15 or y > 15) {
    print("At least one condition is true");
}

if (not (x == y)) {
    print("x and y are different");
}


# ========== EXAMPLE 10: Fizzbuzz ==========
func fizzbuzz(n) {
    for (i: range(1, n + 1)) {
        let msg = "";
        if (i % 3 == 0) {
            let msg = "Fizz";
        }
        if (i % 5 == 0) {
            let msg = msg + "Buzz";
        }
        if (msg == "") {
            print(i);
        } else {
            print(msg);
        }
    }
}

print("FizzBuzz 1-15:");
fizzbuzz(15);


# ========== EXAMPLE 11: List Iteration ==========
let squares = [];
for (i: range(1, 6)) {
    push(squares, i * i);
}
print("Squares 1-5:", squares);


# ========== EXAMPLE 12: Type System ==========
let num = 42;
let text = "hello";
let lst = [1, 2, 3];
let flag = true;
let nothing = null;

print("Type of 42:", type(num));
print("Type of 'hello':", type(text));
print("Type of [1,2,3]:", type(lst));
print("Type of true:", type(flag));
print("Type of null:", type(nothing));
print("Type of print:", type(print));
