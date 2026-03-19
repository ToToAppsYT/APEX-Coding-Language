# APEX Programming Language - Documentation

**MIT License**

Copyright (c) 2026 ToToAppsYT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

---

## Overview

**APEX** is a dynamically-typed, interpreted programming language designed with simplicity and expressiveness in mind. It supports variables, functions, control flow, loops, lists, and dynamic typing.

## Features

- **Dynamic Typing**: Variables can hold any type
- **First-Class Functions**: Functions are values that can be passed around
- **Lexical Scoping**: Functions create their own scope
- **List Operations**: Built-in list support with indexing
- **String Operations**: String concatenation and indexing
- **Control Flow**: if/else statements
- **Loops**: while and for-in loops with break/continue
- **Recursion**: Full support for recursive functions
- **Built-in Functions**: print, len, range, type, and more

---

## Syntax Guide

### 1. Comments

Comments start with `#` and continue to the end of the line:

```apex
# This is a comment
let x = 42; # Inline comment
```

### 2. Variables

Declare variables using the `let` keyword:

```apex
let name = "Alice";
let age = 30;
let is_active = true;
let data = null;
```

### 3. Data Types

**Numbers** (Integer and Float):
```apex
let int_num = 42;
let float_num = 3.14;
```

**Strings** (with escape sequences):
```apex
let text = "Hello, World!";
let escaped = "Line 1\nLine 2\tTabbed";
```

**Booleans**:
```apex
let flag = true;
let empty = false;
```

**Null**:
```apex
let nothing = null;
```

**Lists**:
```apex
let numbers = [1, 2, 3, 4, 5];
let mixed = [42, "hello", true];
let empty_list = [];
```

### 4. Operators

**Arithmetic**:
```apex
let sum = 10 + 5;        # 15
let diff = 10 - 5;       # 5
let product = 10 * 5;    # 50
let quotient = 10 / 5;   # 2.0
let remainder = 10 % 3;  # 1
let power = 2 ** 8;      # 256
```

**Comparison**:
```apex
10 == 10    # true
10 != 5     # true
10 < 20     # true
10 > 5      # true
10 <= 10    # true
10 >= 10    # true
```

**Logical**:
```apex
true and false    # false
true or false     # true
not true          # false
```

**String Concatenation**:
```apex
"Hello" + " " + "World"    # "Hello World"
"Value: " + str(42)        # "Value: 42"
```

**List Indexing**:
```apex
let lst = [10, 20, 30];
lst[0]        # 10
lst[1]        # 20
lst[2]        # 30
lst[-1]       # Error (negative indices not supported)
```

### 5. Control Flow

**If-Else Statements**:
```apex
if (x > 10) {
    print("x is greater than 10");
} else if (x == 10) {
    print("x equals 10");
} else {
    print("x is less than 10");
}
```

### 6. Loops

**While Loop**:
```apex
let i = 0;
while (i < 5) {
    print(i);
    let i = i + 1;
}
```

**For-In Loop**:
```apex
for (item: [1, 2, 3]) {
    print(item);
}

for (i: range(5)) {
    print(i);    # Prints 0, 1, 2, 3, 4
}
```

**Break and Continue**:
```apex
for (i: range(10)) {
    if (i == 5) {
        break;    # Exit the loop
    }
    if (i == 2) {
        continue;  # Skip to next iteration
    }
    print(i);
}
```

### 7. Functions

**Function Definition**:
```apex
func add(x, y) {
    return x + y;
}

func greet(name) {
    print("Hello, " + name + "!");
}
```

**Function Calls**:
```apex
let sum = add(5, 3);           # 8
greet("World");                # Prints: Hello, World!
let len_val = len([1, 2, 3]);  # 3
```

**Recursive Functions**:
```apex
func factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

print(factorial(5));  # 120
```

**Early Return**:
```apex
func check(x) {
    if (x < 0) {
        return "negative";
    }
    if (x == 0) {
        return "zero";
    }
    return "positive";
}
```

### 8. Built-in Functions

**print(...args)**
Prints arguments separated by spaces:
```apex
print("Hello", "World", 42);  # Output: Hello World 42
```

**len(obj)**
Returns the length of a list or string:
```apex
len([1, 2, 3])       # 3
len("Hello")         # 5
```

**range(n)** / **range(start, end)** / **range(start, end, step)**
Creates a list of numbers:
```apex
range(5)             # [0, 1, 2, 3, 4]
range(2, 5)          # [2, 3, 4]
range(0, 10, 2)      # [0, 2, 4, 6, 8]
```

**str(obj)**
Converts to string:
```apex
str(42)              # "42"
str([1, 2, 3])       # "[1, 2, 3]"
```

**int(obj)**
Converts to integer:
```apex
int(3.14)            # 3
int("42")            # 42
```

**float(obj)**
Converts to float:
```apex
float(42)            # 42.0
float("3.14")        # 3.14
```

**type(obj)**
Returns the type of an object:
```apex
type(42)             # "integer"
type("hello")        # "string"
type([1, 2])         # "list"
type(true)           # "boolean"
type(null)           # "null"
```

**push(list, item)**
Adds an item to a list:
```apex
let lst = [1, 2];
push(lst, 3);
print(lst);          # [1, 2, 3]
```

**pop(list)**
Removes and returns the last item:
```apex
let lst = [1, 2, 3];
let last = pop(lst);  # last = 3, lst = [1, 2]
```

---

## Code Examples

### Example 1: FizzBuzz

```apex
func fizzbuzz(n) {
    for (i: range(1, n + 1)) {
        let output = "";
        if (i % 3 == 0) {
            let output = "Fizz";
        }
        if (i % 5 == 0) {
            let output = output + "Buzz";
        }
        if (output == "") {
            print(i);
        } else {
            print(output);
        }
    }
}

fizzbuzz(15);
```

### Example 2: List Sum

```apex
func sum_list(numbers) {
    let total = 0;
    for (num: numbers) {
        let total = total + num;
    }
    return total;
}

let nums = [1, 2, 3, 4, 5];
print("Sum:", sum_list(nums));  # Sum: 15
```

### Example 3: Nested Functions and Closures

```apex
func make_counter() {
    let count = 0;
    func increment() {
        let count = count + 1;
        return count;
    }
    return increment;
}

let counter = make_counter();
print(counter());  # 1
print(counter());  # 2
print(counter());  # 3
```

### Example 4: Higher-Order Functions

```apex
func apply_twice(func_obj, x) {
    return func_obj(func_obj(x));
}

func double(n) {
    return n * 2;
}

print(apply_twice(double, 5));  # 20
```

---

## Error Handling

The APEX interpreter will report errors with line and column information:

```
❌ Parse error at line 5, col 10: Expected '=' after variable name
❌ Runtime error: Division by zero
❌ Runtime error: Undefined variable: foo
```

---

## Performance Notes

- APEX is an interpreted language, so performance is slower than compiled languages
- Recursive functions may hit stack limits on very deep recursion
- No tail-call optimization is performed
- Lists are stored as Python lists internally

---

## Limitations

- No import/module system
- No exception handling (try/catch)
- No object-oriented features (classes, objects, methods)
- No dictionaries or hashmaps
- No regular expressions
- No file I/O
- Functions have no default parameters
- No lambda expressions (anonymous functions)
- No generator/iterator protocol

---

## Running APEX Programs

### Interactive REPL

Run the interpreter to start an interactive shell:

```bash
python3 lang.py
```

Then type APEX code directly:

```
apex> let x = 10;
apex> print(x * 2);
20
```

### Running from String

```python
from lang import *

code = '''
let message = "Hello from APEX!";
print(message);
'''

lexer = Lexer(code)
tokens = lexer.tokenize()
parser = Parser(tokens)
ast = parser.parse()
interpreter = Interpreter()
interpreter.eval(ast)
```

---

## Language Implementation Details

### Architecture

1. **Lexer**: Tokenizes source code into tokens
2. **Parser**: Builds an Abstract Syntax Tree (AST) from tokens
3. **Interpreter**: Evaluates the AST directly (tree-walking interpreter)

### Operator Precedence (highest to lowest)

1. Primary (literals, identifiers, parentheses)
2. Postfix (function calls, indexing)
3. Unary (-, +, not)
4. Power (**)
5. Multiplicative (*, /, %)
6. Additive (+, -)
7. Relational (<, >, <=, >=)
8. Equality (==, !=, ===, !==)
9. Logical AND (and)
10. Logical OR (or)
11. Assignment (=)

---

## Future Ideas

- Module/import system
- Tail-call optimization
- Type hints and static checking
- Async/await support
- Pattern matching
- Destructuring assignments
- Dictionary/map type
- Set type
- Exception handling
- Decorator syntax
- Slice notation [start:end:step]
- Multiple return values (tuples)
- Keyword arguments
- Variable arguments (*args, **kwargs)
