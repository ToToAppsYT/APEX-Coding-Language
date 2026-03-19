# APEX Quick Reference

**MIT License** - Copyright (c) 2026 ToToAppsYT

---

## Basics

```apex
# Comments start with #
let x = 10;                  # Variable declaration
let name = "Alice";          # String
let active = true;           # Boolean
let items = [1, 2, 3];       # List
let nothing = null;          # Null
```

## Operators

```apex
# Arithmetic
x + 5    x - 5    x * 5    x / 5    x % 5    x ** 5

# Comparison
x == 5   x != 5   x < 5    x > 5    x <= 5   x >= 5

# Logical
a and b   a or b   not a

# String concatenation
"Hello" + " " + "World"

# List indexing
list[0]   list[1]   list[2]

# Assignment
let x = 10;
let x = x + 5;
```

## Control Flow

```apex
# If-Else
if (condition) {
    # code
} else if (other_condition) {
    # code
} else {
    # code
}

# While loop
while (condition) {
    # code
}

# For loop
for (item: items) {
    # code
}

# Break and Continue
break;      # Exit loop
continue;   # Skip to next iteration
```

## Functions

```apex
# Define function
func add(x, y) {
    return x + y;
}

# Call function
let result = add(5, 3);

# Recursive function
func factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
```

## Built-in Functions

```apex
print(...args)           # Print to console
len(list_or_string)      # Get length
range(n)                 # [0, 1, ..., n-1]
range(start, end)        # [start, ..., end-1]
range(start, end, step)  # With step
str(obj)                 # Convert to string
int(obj)                 # Convert to integer
float(obj)               # Convert to float
type(obj)                # Get type as string
push(list, item)         # Add to list
pop(list)                # Remove from list
```

## Type Names (from type())

```apex
type(42)              # "integer"
type(3.14)            # "float"
type("hello")         # "string"
type(true)            # "boolean"
type([1, 2])          # "list"
type(null)            # "null"
type(func_object)     # "function"
```

## Data Type Conversions

```apex
str(42)              # "42"
int("42")            # 42
int(3.14)            # 3
float(42)            # 42.0
float("3.14")        # 3.14
```

## Common Patterns

### Sum a list
```apex
let total = 0;
for (num: numbers) {
    let total = total + num;
}
```

### Double each item
```apex
let doubled = [];
for (num: numbers) {
    push(doubled, num * 2);
}
```

### Count up to N
```apex
let i = 0;
while (i < 10) {
    print(i);
    let i = i + 1;
}
```

### FizzBuzz
```apex
for (i: range(1, 101)) {
    let output = "";
    if (i % 3 == 0) { let output = "Fizz"; }
    if (i % 5 == 0) { let output = output + "Buzz"; }
    print(output == "" ? i : output);
}
```

## Operator Precedence (highest to lowest)

| Precedence | Operators | Associativity |
|-----------|-----------|---------------|
| 1 | `()` `[]` | Left |
| 2 | `-` `+` `not` (unary) | Right |
| 3 | `**` | Right |
| 4 | `*` `/` `%` | Left |
| 5 | `+` `-` | Left |
| 6 | `<` `>` `<=` `>=` | Left |
| 7 | `==` `!=` `===` `!==` | Left |
| 8 | `and` | Left |
| 9 | `or` | Left |
| 10 | `=` | Right |

## Keywords

```
let       func      if        else      while     
for       return    break     continue  true      
false     null      and       or        not
```

## Running APEX

### Interactive REPL
```bash
python3 lang.py
```

### Run code from Python
```python
from lang import *

code = 'let x = 10; print(x);'
lexer = Lexer(code)
tokens = lexer.tokenize()
parser = Parser(tokens)
ast = parser.parse()
interpreter = Interpreter()
interpreter.eval(ast)
```

## String Escape Sequences

```apex
"\n"     # Newline
"\t"     # Tab
"\r"     # Carriage return
"\\"     # Backslash
"\""     # Double quote
"\'"     # Single quote
```

## Common Mistakes

❌ **Wrong**
```apex
let 123 = x;           # Variable name can't start with number
if x > 5               # Missing parentheses
func square x { ... }  # Missing parentheses
```

✅ **Correct**
```apex
let var123 = x;
if (x > 5) { ... }
func square(x) { ... }
```

## Tips & Tricks

1. **Use meaningful variable names**
   ```apex
   let total_price = 100;   # Good
   let tp = 100;            # Not as clear
   ```

2. **Add helper functions**
   ```apex
   func is_even(n) { return n % 2 == 0; }
   func is_positive(n) { return n > 0; }
   ```

3. **Print for debugging**
   ```apex
   let x = 10;
   print("Debug: x =", x);
   ```

4. **Break complex conditions**
   ```apex
   let is_valid = x > 0 and x < 100 and y > 0 and y < 100;
   if (is_valid) { ... }
   ```

5. **Use range() for counting**
   ```apex
   for (i: range(5)) { print(i); }     # 0, 1, 2, 3, 4
   for (i: range(1, 6)) { print(i); }  # 1, 2, 3, 4, 5
   ```

---

**Version**: 1.0 | **Language**: APEX | **Created**: 2026
