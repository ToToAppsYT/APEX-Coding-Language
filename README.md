# APEX Programming Language

A simple yet expressive dynamically-typed interpreted programming language written in Python.

```
🔷 APEX Programming Language 🔷
```

## Quick Start

### Running the Interactive REPL

```bash
python3 lang.py
```

```
apex> let x = 10;
apex> print(x * 2);
20
apex> func add(a, b) { return a + b; }
apex> add(5, 3);
8
```

### Running from Python

```python
from lang import *

code = '''
let numbers = [1, 2, 3, 4, 5];
for (n: numbers) {
    print(n * n);
}
'''

lexer = Lexer(code)
tokens = lexer.tokenize()
parser = Parser(tokens)
ast = parser.parse()
interpreter = Interpreter()
interpreter.eval(ast)
```

## Language Features

✨ **Core Features**
- Variables with dynamic typing
- Functions with lexical scoping
- Control flow (if/else)
- Loops (while, for-in)
- Lists and strings
- Recursion support
- Built-in functions (print, len, range, type, etc.)

📦 **What's Included**
- `lang.py` - Full interpreter implementation
- `DOCUMENTATION.md` - Complete language reference
- `examples.apex` - Example programs
- `README.md` - This file

## Quick Language Tour

### Variables
```apex
let name = "Alice";
let age = 30;
let scores = [95, 87, 92];
let active = true;
```

### Control Flow
```apex
if (age >= 18) {
    print("Adult");
} else {
    print("Minor");
}
```

### Functions
```apex
func multiply(x, y) {
    return x * y;
}

let result = multiply(6, 7);  # 42
```

### Loops
```apex
for (i: range(5)) {
    print(i);  # 0 1 2 3 4
}

let sum = 0;
for (num: [1, 2, 3, 4, 5]) {
    let sum = sum + num;
}
print(sum);  # 15
```

### Recursion
```apex
func factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

print(factorial(5));  # 120
```

### Built-in Functions
```apex
print("Hello", "World");      # Output: Hello World
len([1, 2, 3, 4, 5]);         # 5
type(42);                      # "integer"
str(42);                       # "42"
range(5);                      # [0, 1, 2, 3, 4]
```

## Example Programs

### FizzBuzz
```apex
func fizzbuzz(n) {
    for (i: range(1, n + 1)) {
        let output = "";
        if (i % 3 == 0) { let output = "Fizz"; }
        if (i % 5 == 0) { let output = output + "Buzz"; }
        if (output == "") {
            print(i);
        } else {
            print(output);
        }
    }
}

fizzbuzz(15);
```

### Fibonacci
```apex
func fib(n) {
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

for (i: range(10)) {
    print(fib(i));
}
```

### List Processing
```apex
let numbers = [1, 2, 3, 4, 5];
let squared = [];

for (n: numbers) {
    push(squared, n * n);
}

print(squared);  # [1, 4, 9, 16, 25]
```

## Syntax Reference

### Keywords
- `let` - Variable declaration
- `func` - Function definition
- `if`, `else` - Conditional
- `while` - While loop
- `for` - For-in loop
- `return` - Return from function
- `break` - Break from loop
- `continue` - Skip iteration
- `true`, `false`, `null` - Literals
- `and`, `or`, `not` - Logical operators

### Operators
```
Arithmetic:    +  -  *  /  %  **
Comparison:    ==  !=  <  >  <=  >=
Logical:       and  or  not
Assignment:    =
Indexing:      []
Function call: ()
```

### Data Types
- **Numbers**: `42`, `3.14`
- **Strings**: `"hello"`, `'world'`
- **Booleans**: `true`, `false`
- **Lists**: `[1, 2, 3]`
- **Null**: `null`

## Architecture

The APEX interpreter follows a classic three-stage design:

```
Source Code
    ↓
Lexer (tokenization)
    ↓
Parser (AST construction)
    ↓
Interpreter (tree-walking evaluation)
    ↓
Results
```

### Key Components

1. **Lexer** (`lang.py`)
   - Tokenizes source code
   - Handles strings, numbers, identifiers, operators
   - Tracks line/column for error reporting

2. **Parser** (`lang.py`)
   - Builds Abstract Syntax Tree (AST)
   - Implements operator precedence
   - Generates detailed error messages

3. **Interpreter** (`lang.py`)
   - Tree-walking interpreter
   - Maintains variable scopes
   - Manages function execution

## Error Messages

APEX provides helpful error messages:

```
❌ Lexer error at line 5, col 10: Unterminated string
❌ Parse error at line 3, col 8: Expected '=' after variable name
❌ Runtime error: Undefined variable: foo
❌ Runtime error: Division by zero
```

## Limitations

- No import/module system
- No exception handling (try/catch)
- No OOP (classes, objects)
- No dictionaries or sets
- No regex support
- No file I/O built-ins
- No async/await
- Interpreted (slower than compiled)

## File Structure

```
.
├── lang.py              # Complete interpreter
├── README.md            # This file
├── DOCUMENTATION.md     # Full language reference
└── examples.apex        # Example programs
```

## Usage

### As a Script Interpreter

```bash
# Interactive REPL
python3 lang.py

# Or embed in Python
python3 -c "from lang import *; ..."
```

### Extending the Language

Add new built-in functions in `Interpreter.setup_builtins()`:

```python
def builtin_uppercase(self, text):
    return text.upper()

self.globals['uppercase'] = self.builtin_uppercase
```

## Performance

- APEX is an interpreted language (~1000x slower than compiled C)
- Suitable for learning, scripting, and prototyping
- Not recommended for performance-critical applications
- Recursion depth limited by Python stack size

## Contributing

Feel free to extend APEX with:
- New built-in functions
- Additional operators
- Language features
- Optimizations

## License

MIT License

Copyright (c) 2026 ToToAppsYT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

**Created as a demonstration of language design principles.**

Enjoy coding in APEX! 🔷
