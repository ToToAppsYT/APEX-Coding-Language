"""
APEX - A minimal yet expressive programming language
Features: variables, functions, conditionals, loops, lists, and dynamic typing

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
"""

from __future__ import annotations
import re
from typing import Any, Dict, List, Tuple, Optional, Union
from enum import Enum, auto
from dataclasses import dataclass

# ============================================================================
# TOKENS & LEXER
# ============================================================================

class TokenType(Enum):
    # Literals
    NUMBER = auto()
    STRING = auto()
    SYMBOL = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()
    
    # Keywords
    LET = auto()
    FUNC = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    FOR = auto()
    RETURN = auto()
    BREAK = auto()
    CONTINUE = auto()
    
    # Operators
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    PERCENT = auto()
    POWER = auto()
    EQ = auto()
    NEQ = auto()
    LT = auto()
    GT = auto()
    LTE = auto()
    GTE = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    ASSIGN = auto()
    
    # Delimiters
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    COMMA = auto()
    DOT = auto()
    COLON = auto()
    SEMICOLON = auto()
    ARROW = auto()
    
    # Special
    EOF = auto()
    NEWLINE = auto()

@dataclass
class Token:
    type: TokenType
    value: Any
    line: int
    col: int
    
    def __repr__(self):
        return f"Token({self.type.name}, {self.value!r})"

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.line = 1
        self.col = 1
        self.tokens = []
        
    def error(self, msg: str):
        raise SyntaxError(f"Lexer error at line {self.line}, col {self.col}: {msg}")
    
    def peek(self, offset: int = 0) -> Optional[str]:
        p = self.pos + offset
        return self.text[p] if p < len(self.text) else None
    
    def advance(self) -> Optional[str]:
        if self.pos >= len(self.text):
            return None
        char = self.text[self.pos]
        self.pos += 1
        if char == '\n':
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        return char
    
    def skip_whitespace_and_comments(self):
        while self.peek() and self.peek() in ' \t\r':
            self.advance()
        
        # Comments
        if self.peek() == '#':
            while self.peek() and self.peek() != '\n':
                self.advance()
    
    def read_string(self, quote: str) -> str:
        value = ""
        self.advance()  # skip opening quote
        while True:
            char = self.peek()
            if char is None:
                self.error(f"Unterminated string")
            if char == quote:
                self.advance()
                break
            if char == '\\':
                self.advance()
                next_char = self.advance()
                escape_map = {'n': '\n', 't': '\t', 'r': '\r', '\\': '\\', '"': '"', "'": "'"}
                value += escape_map.get(next_char, next_char)
            else:
                value += self.advance()
        return value
    
    def read_number(self) -> Union[int, float]:
        value = ""
        has_dot = False
        while self.peek() and (self.peek().isdigit() or self.peek() == '.'):
            if self.peek() == '.':
                if has_dot:
                    break
                has_dot = True
            value += self.advance()
        return float(value) if has_dot else int(value)
    
    def read_identifier(self) -> str:
        value = ""
        while self.peek() and (self.peek().isalnum() or self.peek() in '_?!'):
            value += self.advance()
        return value
    
    def tokenize(self) -> List[Token]:
        keywords = {
            'let': TokenType.LET, 'func': TokenType.FUNC, 'if': TokenType.IF,
            'else': TokenType.ELSE, 'while': TokenType.WHILE, 'for': TokenType.FOR,
            'return': TokenType.RETURN, 'break': TokenType.BREAK, 'continue': TokenType.CONTINUE,
            'true': TokenType.TRUE, 'false': TokenType.FALSE, 'null': TokenType.NULL,
            'and': TokenType.AND, 'or': TokenType.OR, 'not': TokenType.NOT,
        }
        
        while self.pos < len(self.text):
            self.skip_whitespace_and_comments()
            if self.pos >= len(self.text):
                break
            
            line, col = self.line, self.col
            char = self.peek()
            
            # Newlines
            if char == '\n':
                self.advance()
                self.tokens.append(Token(TokenType.NEWLINE, '\n', line, col))
                continue
            
            # Strings
            if char in '"\'':
                value = self.read_string(char)
                self.tokens.append(Token(TokenType.STRING, value, line, col))
                continue
            
            # Numbers
            if char.isdigit():
                value = self.read_number()
                self.tokens.append(Token(TokenType.NUMBER, value, line, col))
                continue
            
            # Identifiers and keywords
            if char.isalpha() or char == '_':
                ident = self.read_identifier()
                token_type = keywords.get(ident, TokenType.SYMBOL)
                value = True if token_type == TokenType.TRUE else (False if token_type == TokenType.FALSE else (None if token_type == TokenType.NULL else ident))
                self.tokens.append(Token(token_type, value, line, col))
                continue
            
            # Operators and delimiters
            two_char = char + (self.peek(1) or '')
            three_char = two_char + (self.peek(2) or '')
            
            if three_char == '===':
                self.advance(); self.advance(); self.advance()
                self.tokens.append(Token(TokenType.EQ, '===', line, col))
            elif three_char == '!==':
                self.advance(); self.advance(); self.advance()
                self.tokens.append(Token(TokenType.NEQ, '!==', line, col))
            elif two_char == '==':
                self.advance(); self.advance()
                self.tokens.append(Token(TokenType.EQ, '==', line, col))
            elif two_char == '!=':
                self.advance(); self.advance()
                self.tokens.append(Token(TokenType.NEQ, '!=', line, col))
            elif two_char == '<=':
                self.advance(); self.advance()
                self.tokens.append(Token(TokenType.LTE, '<=', line, col))
            elif two_char == '>=':
                self.advance(); self.advance()
                self.tokens.append(Token(TokenType.GTE, '>=', line, col))
            elif two_char == '=>':
                self.advance(); self.advance()
                self.tokens.append(Token(TokenType.ARROW, '=>', line, col))
            elif two_char == '**':
                self.advance(); self.advance()
                self.tokens.append(Token(TokenType.POWER, '**', line, col))
            elif char == '+':
                self.advance()
                self.tokens.append(Token(TokenType.PLUS, '+', line, col))
            elif char == '-':
                self.advance()
                self.tokens.append(Token(TokenType.MINUS, '-', line, col))
            elif char == '*':
                self.advance()
                self.tokens.append(Token(TokenType.STAR, '*', line, col))
            elif char == '/':
                self.advance()
                self.tokens.append(Token(TokenType.SLASH, '/', line, col))
            elif char == '%':
                self.advance()
                self.tokens.append(Token(TokenType.PERCENT, '%', line, col))
            elif char == '=':
                self.advance()
                self.tokens.append(Token(TokenType.ASSIGN, '=', line, col))
            elif char == '<':
                self.advance()
                self.tokens.append(Token(TokenType.LT, '<', line, col))
            elif char == '>':
                self.advance()
                self.tokens.append(Token(TokenType.GT, '>', line, col))
            elif char == '!':
                self.advance()
                self.tokens.append(Token(TokenType.NOT, '!', line, col))
            elif char == '(':
                self.advance()
                self.tokens.append(Token(TokenType.LPAREN, '(', line, col))
            elif char == ')':
                self.advance()
                self.tokens.append(Token(TokenType.RPAREN, ')', line, col))
            elif char == '{':
                self.advance()
                self.tokens.append(Token(TokenType.LBRACE, '{', line, col))
            elif char == '}':
                self.advance()
                self.tokens.append(Token(TokenType.RBRACE, '}', line, col))
            elif char == '[':
                self.advance()
                self.tokens.append(Token(TokenType.LBRACKET, '[', line, col))
            elif char == ']':
                self.advance()
                self.tokens.append(Token(TokenType.RBRACKET, ']', line, col))
            elif char == ',':
                self.advance()
                self.tokens.append(Token(TokenType.COMMA, ',', line, col))
            elif char == '.':
                self.advance()
                self.tokens.append(Token(TokenType.DOT, '.', line, col))
            elif char == ':':
                self.advance()
                self.tokens.append(Token(TokenType.COLON, ':', line, col))
            elif char == ';':
                self.advance()
                self.tokens.append(Token(TokenType.SEMICOLON, ';', line, col))
            else:
                self.error(f"Unexpected character: {char}")
        
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.col))
        return self.tokens

# ============================================================================
# AST NODES
# ============================================================================

@dataclass
class ASTNode:
    pass

@dataclass
class Number(ASTNode):
    value: Union[int, float]

@dataclass
class String(ASTNode):
    value: str

@dataclass
class Boolean(ASTNode):
    value: bool

@dataclass
class Null(ASTNode):
    pass

@dataclass
class Identifier(ASTNode):
    name: str

@dataclass
class List(ASTNode):
    elements: List[ASTNode]

@dataclass
class BinaryOp(ASTNode):
    left: ASTNode
    op: str
    right: ASTNode

@dataclass
class UnaryOp(ASTNode):
    op: str
    operand: ASTNode

@dataclass
class Assignment(ASTNode):
    target: str
    value: ASTNode

@dataclass
class IfStmt(ASTNode):
    condition: ASTNode
    then_body: List[ASTNode]
    else_body: Optional[List[ASTNode]]

@dataclass
class WhileLoop(ASTNode):
    condition: ASTNode
    body: List[ASTNode]

@dataclass
class ForLoop(ASTNode):
    var: str
    iterable: ASTNode
    body: List[ASTNode]

@dataclass
class FunctionDef(ASTNode):
    name: str
    params: List[str]
    body: List[ASTNode]

@dataclass
class FunctionCall(ASTNode):
    name: ASTNode
    args: List[ASTNode]

@dataclass
class ReturnStmt(ASTNode):
    value: Optional[ASTNode]

@dataclass
class BreakStmt(ASTNode):
    pass

@dataclass
class ContinueStmt(ASTNode):
    pass

@dataclass
class IndexAccess(ASTNode):
    obj: ASTNode
    index: ASTNode

@dataclass
class Program(ASTNode):
    statements: List[ASTNode]

# ============================================================================
# PARSER
# ============================================================================

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def error(self, msg: str):
        token = self.current_token()
        raise SyntaxError(f"Parse error at line {token.line}, col {token.col}: {msg}")
    
    def current_token(self) -> Token:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else self.tokens[-1]
    
    def peek(self, offset: int = 0) -> Token:
        p = self.pos + offset
        return self.tokens[p] if p < len(self.tokens) else self.tokens[-1]
    
    def advance(self) -> Token:
        token = self.current_token()
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
        return token
    
    def skip_newlines(self):
        while self.current_token().type == TokenType.NEWLINE:
            self.advance()
    
    def match(self, *types: TokenType) -> bool:
        return self.current_token().type in types
    
    def consume(self, token_type: TokenType, msg: str = "") -> Token:
        if self.current_token().type != token_type:
            self.error(msg or f"Expected {token_type.name}, got {self.current_token().type.name}")
        return self.advance()
    
    def parse(self) -> Program:
        statements = []
        self.skip_newlines()
        while not self.match(TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            self.skip_newlines()
        return Program(statements)
    
    def parse_statement(self) -> Optional[ASTNode]:
        self.skip_newlines()
        
        if self.match(TokenType.LET):
            return self.parse_let()
        elif self.match(TokenType.FUNC):
            return self.parse_function_def()
        elif self.match(TokenType.IF):
            return self.parse_if()
        elif self.match(TokenType.WHILE):
            return self.parse_while()
        elif self.match(TokenType.FOR):
            return self.parse_for()
        elif self.match(TokenType.RETURN):
            return self.parse_return()
        elif self.match(TokenType.BREAK):
            self.advance()
            self.skip_semicolon()
            return BreakStmt()
        elif self.match(TokenType.CONTINUE):
            self.advance()
            self.skip_semicolon()
            return ContinueStmt()
        elif self.match(TokenType.RBRACE, TokenType.EOF):
            return None
        else:
            return self.parse_expression_stmt()
    
    def skip_semicolon(self):
        if self.match(TokenType.SEMICOLON):
            self.advance()
    
    def parse_let(self) -> Assignment:
        self.consume(TokenType.LET)
        self.skip_newlines()
        name_token = self.consume(TokenType.SYMBOL, "Expected variable name")
        self.skip_newlines()
        self.consume(TokenType.ASSIGN, "Expected '=' after variable name")
        self.skip_newlines()
        value = self.parse_expression()
        self.skip_semicolon()
        return Assignment(name_token.value, value)
    
    def parse_function_def(self) -> FunctionDef:
        self.consume(TokenType.FUNC)
        self.skip_newlines()
        name_token = self.consume(TokenType.SYMBOL, "Expected function name")
        self.skip_newlines()
        self.consume(TokenType.LPAREN)
        
        params = []
        if not self.match(TokenType.RPAREN):
            params.append(self.consume(TokenType.SYMBOL).value)
            while self.match(TokenType.COMMA):
                self.advance()
                self.skip_newlines()
                params.append(self.consume(TokenType.SYMBOL).value)
        
        self.consume(TokenType.RPAREN)
        self.skip_newlines()
        self.consume(TokenType.LBRACE)
        self.skip_newlines()
        
        body = self.parse_block()
        
        self.skip_newlines()
        self.consume(TokenType.RBRACE)
        
        return FunctionDef(name_token.value, params, body)
    
    def parse_if(self) -> IfStmt:
        self.consume(TokenType.IF)
        self.skip_newlines()
        self.consume(TokenType.LPAREN)
        condition = self.parse_expression()
        self.consume(TokenType.RPAREN)
        self.skip_newlines()
        self.consume(TokenType.LBRACE)
        self.skip_newlines()
        then_body = self.parse_block()
        self.skip_newlines()
        self.consume(TokenType.RBRACE)
        
        else_body = None
        self.skip_newlines()
        if self.match(TokenType.ELSE):
            self.advance()
            self.skip_newlines()
            self.consume(TokenType.LBRACE)
            self.skip_newlines()
            else_body = self.parse_block()
            self.skip_newlines()
            self.consume(TokenType.RBRACE)
        
        return IfStmt(condition, then_body, else_body)
    
    def parse_while(self) -> WhileLoop:
        self.consume(TokenType.WHILE)
        self.skip_newlines()
        self.consume(TokenType.LPAREN)
        condition = self.parse_expression()
        self.consume(TokenType.RPAREN)
        self.skip_newlines()
        self.consume(TokenType.LBRACE)
        self.skip_newlines()
        body = self.parse_block()
        self.skip_newlines()
        self.consume(TokenType.RBRACE)
        return WhileLoop(condition, body)
    
    def parse_for(self) -> ForLoop:
        self.consume(TokenType.FOR)
        self.skip_newlines()
        self.consume(TokenType.LPAREN)
        var_token = self.consume(TokenType.SYMBOL)
        self.skip_newlines()
        self.consume(TokenType.COLON)
        self.skip_newlines()
        iterable = self.parse_expression()
        self.consume(TokenType.RPAREN)
        self.skip_newlines()
        self.consume(TokenType.LBRACE)
        self.skip_newlines()
        body = self.parse_block()
        self.skip_newlines()
        self.consume(TokenType.RBRACE)
        return ForLoop(var_token.value, iterable, body)
    
    def parse_return(self) -> ReturnStmt:
        self.consume(TokenType.RETURN)
        value = None
        if not self.match(TokenType.SEMICOLON, TokenType.NEWLINE, TokenType.RBRACE, TokenType.EOF):
            value = self.parse_expression()
        self.skip_semicolon()
        return ReturnStmt(value)
    
    def parse_block(self) -> List[ASTNode]:
        statements = []
        while not self.match(TokenType.RBRACE, TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            self.skip_newlines()
        return statements
    
    def parse_expression_stmt(self) -> Optional[ASTNode]:
        expr = self.parse_expression()
        self.skip_semicolon()
        return expr
    
    def parse_expression(self) -> ASTNode:
        return self.parse_assignment()
    
    def parse_assignment(self) -> ASTNode:
        expr = self.parse_or()
        if self.match(TokenType.ASSIGN):
            if not isinstance(expr, Identifier):
                self.error("Invalid assignment target")
            self.advance()
            value = self.parse_assignment()
            return Assignment(expr.name, value)
        return expr
    
    def parse_or(self) -> ASTNode:
        left = self.parse_and()
        while self.match(TokenType.OR):
            op = self.advance().value
            right = self.parse_and()
            left = BinaryOp(left, op, right)
        return left
    
    def parse_and(self) -> ASTNode:
        left = self.parse_equality()
        while self.match(TokenType.AND):
            op = self.advance().value
            right = self.parse_equality()
            left = BinaryOp(left, op, right)
        return left
    
    def parse_equality(self) -> ASTNode:
        left = self.parse_relational()
        while self.match(TokenType.EQ, TokenType.NEQ):
            op = self.advance().value
            right = self.parse_relational()
            left = BinaryOp(left, op, right)
        return left
    
    def parse_relational(self) -> ASTNode:
        left = self.parse_additive()
        while self.match(TokenType.LT, TokenType.GT, TokenType.LTE, TokenType.GTE):
            op = self.advance().value
            right = self.parse_additive()
            left = BinaryOp(left, op, right)
        return left
    
    def parse_additive(self) -> ASTNode:
        left = self.parse_multiplicative()
        while self.match(TokenType.PLUS, TokenType.MINUS):
            op = self.advance().value
            right = self.parse_multiplicative()
            left = BinaryOp(left, op, right)
        return left
    
    def parse_multiplicative(self) -> ASTNode:
        left = self.parse_power()
        while self.match(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT):
            op = self.advance().value
            right = self.parse_power()
            left = BinaryOp(left, op, right)
        return left
    
    def parse_power(self) -> ASTNode:
        left = self.parse_unary()
        if self.match(TokenType.POWER):
            op = self.advance().value
            right = self.parse_power()
            left = BinaryOp(left, op, right)
        return left
    
    def parse_unary(self) -> ASTNode:
        if self.match(TokenType.NOT, TokenType.MINUS, TokenType.PLUS):
            op = self.advance().value
            operand = self.parse_unary()
            return UnaryOp(op, operand)
        return self.parse_postfix()
    
    def parse_postfix(self) -> ASTNode:
        expr = self.parse_primary()
        while True:
            if self.match(TokenType.LBRACKET):
                self.advance()
                index = self.parse_expression()
                self.consume(TokenType.RBRACKET)
                expr = IndexAccess(expr, index)
            elif self.match(TokenType.LPAREN):
                self.advance()
                args = []
                if not self.match(TokenType.RPAREN):
                    args.append(self.parse_expression())
                    while self.match(TokenType.COMMA):
                        self.advance()
                        self.skip_newlines()
                        args.append(self.parse_expression())
                self.consume(TokenType.RPAREN)
                expr = FunctionCall(expr, args)
            else:
                break
        return expr
    
    def parse_primary(self) -> ASTNode:
        if self.match(TokenType.NUMBER):
            return Number(self.advance().value)
        elif self.match(TokenType.STRING):
            return String(self.advance().value)
        elif self.match(TokenType.TRUE):
            self.advance()
            return Boolean(True)
        elif self.match(TokenType.FALSE):
            self.advance()
            return Boolean(False)
        elif self.match(TokenType.NULL):
            self.advance()
            return Null()
        elif self.match(TokenType.SYMBOL):
            return Identifier(self.advance().value)
        elif self.match(TokenType.LBRACKET):
            return self.parse_list()
        elif self.match(TokenType.LPAREN):
            self.advance()
            expr = self.parse_expression()
            self.consume(TokenType.RPAREN)
            return expr
        else:
            self.error(f"Unexpected token: {self.current_token().type.name}")

    def parse_list(self) -> List:
        self.consume(TokenType.LBRACKET)
        elements = []
        if not self.match(TokenType.RBRACKET):
            elements.append(self.parse_expression())
            while self.match(TokenType.COMMA):
                self.advance()
                self.skip_newlines()
                if self.match(TokenType.RBRACKET):
                    break
                elements.append(self.parse_expression())
        self.consume(TokenType.RBRACKET)
        return List(elements)

# ============================================================================
# INTERPRETER
# ============================================================================

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass

class ApexFunction:
    def __init__(self, params, body, closure):
        self.params = params
        self.body = body
        self.closure = closure
    
    def __repr__(self):
        return f"<function ({', '.join(self.params)})>"

class Interpreter:
    def __init__(self):
        self.globals = {}
        self.locals_stack = [{}]
        self.setup_builtins()
    
    def setup_builtins(self):
        self.globals['print'] = self.builtin_print
        self.globals['len'] = self.builtin_len
        self.globals['range'] = self.builtin_range
        self.globals['str'] = self.builtin_str
        self.globals['int'] = self.builtin_int
        self.globals['float'] = self.builtin_float
        self.globals['push'] = self.builtin_push
        self.globals['pop'] = self.builtin_pop
        self.globals['type'] = self.builtin_type
    
    def builtin_print(self, *args):
        print(' '.join(str(arg) for arg in args))
        return None
    
    def builtin_len(self, obj):
        if isinstance(obj, (list, str)):
            return len(obj)
        self.error(f"len() argument must be a list or string")
    
    def builtin_range(self, *args):
        if len(args) == 1:
            return list(range(int(args[0])))
        elif len(args) == 2:
            return list(range(int(args[0]), int(args[1])))
        elif len(args) == 3:
            return list(range(int(args[0]), int(args[1]), int(args[2])))
        self.error("range() takes 1-3 arguments")
    
    def builtin_str(self, obj):
        return str(obj)
    
    def builtin_int(self, obj):
        return int(float(obj))
    
    def builtin_float(self, obj):
        return float(obj)
    
    def builtin_push(self, lst, item):
        lst.append(item)
        return None
    
    def builtin_pop(self, lst):
        return lst.pop() if lst else None
    
    def builtin_type(self, obj):
        if isinstance(obj, bool):
            return "boolean"
        elif isinstance(obj, int):
            return "integer"
        elif isinstance(obj, float):
            return "float"
        elif isinstance(obj, str):
            return "string"
        elif isinstance(obj, list):
            return "list"
        elif obj is None:
            return "null"
        elif isinstance(obj, ApexFunction):
            return "function"
        return "unknown"
    
    def error(self, msg: str):
        raise RuntimeError(f"Runtime error: {msg}")
    
    def get_var(self, name: str):
        for scope in reversed(self.locals_stack):
            if name in scope:
                return scope[name]
        if name in self.globals:
            return self.globals[name]
        self.error(f"Undefined variable: {name}")
    
    def set_var(self, name: str, value):
        self.locals_stack[-1][name] = value
    
    def eval(self, node: ASTNode) -> Any:
        if isinstance(node, Program):
            result = None
            for stmt in node.statements:
                result = self.eval(stmt)
            return result
        
        elif isinstance(node, Number):
            return node.value
        
        elif isinstance(node, String):
            return node.value
        
        elif isinstance(node, Boolean):
            return node.value
        
        elif isinstance(node, Null):
            return None
        
        elif isinstance(node, List):
            return [self.eval(elem) for elem in node.elements]
        
        elif isinstance(node, Identifier):
            return self.get_var(node.name)
        
        elif isinstance(node, BinaryOp):
            left = self.eval(node.left)
            right = self.eval(node.right)
            
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                if right == 0:
                    self.error("Division by zero")
                return left / right
            elif node.op == '%':
                return left % right
            elif node.op == '**':
                return left ** right
            elif node.op in ('==', '==='):
                return left == right
            elif node.op in ('!=', '!=='):
                return left != right
            elif node.op == '<':
                return left < right
            elif node.op == '>':
                return left > right
            elif node.op == '<=':
                return left <= right
            elif node.op == '>=':
                return left >= right
            elif node.op == 'and':
                return left and right
            elif node.op == 'or':
                return left or right
        
        elif isinstance(node, UnaryOp):
            operand = self.eval(node.operand)
            if node.op == '-':
                return -operand
            elif node.op == '+':
                return +operand
            elif node.op == 'not' or node.op == '!':
                return not operand
        
        elif isinstance(node, Assignment):
            value = self.eval(node.value)
            self.set_var(node.target, value)
            return value
        
        elif isinstance(node, IfStmt):
            condition = self.eval(node.condition)
            if condition:
                result = None
                for stmt in node.then_body:
                    result = self.eval(stmt)
                return result
            elif node.else_body:
                result = None
                for stmt in node.else_body:
                    result = self.eval(stmt)
                return result
            return None
        
        elif isinstance(node, WhileLoop):
            result = None
            try:
                while self.eval(node.condition):
                    try:
                        for stmt in node.body:
                            result = self.eval(stmt)
                    except ContinueException:
                        continue
            except BreakException:
                pass
            return result
        
        elif isinstance(node, ForLoop):
            iterable = self.eval(node.iterable)
            result = None
            try:
                for item in iterable:
                    self.set_var(node.var, item)
                    try:
                        for stmt in node.body:
                            result = self.eval(stmt)
                    except ContinueException:
                        continue
            except BreakException:
                pass
            return result
        
        elif isinstance(node, FunctionDef):
            func = ApexFunction(node.params, node.body, self.locals_stack[-1].copy())
            self.set_var(node.name, func)
            return func
        
        elif isinstance(node, FunctionCall):
            func = self.eval(node.name)
            args = [self.eval(arg) for arg in node.args]
            
            if callable(func):
                return func(*args)
            elif isinstance(func, ApexFunction):
                if len(args) != len(func.params):
                    self.error(f"Function expects {len(func.params)} arguments, got {len(args)}")
                
                self.locals_stack.append({})
                for param, arg in zip(func.params, args):
                    self.set_var(param, arg)
                
                try:
                    result = None
                    for stmt in func.body:
                        result = self.eval(stmt)
                    return result
                except ReturnValue as ret:
                    return ret.value
                finally:
                    self.locals_stack.pop()
            else:
                self.error(f"Object is not callable")
        
        elif isinstance(node, ReturnStmt):
            value = self.eval(node.value) if node.value else None
            raise ReturnValue(value)
        
        elif isinstance(node, BreakStmt):
            raise BreakException()
        
        elif isinstance(node, ContinueStmt):
            raise ContinueException()
        
        elif isinstance(node, IndexAccess):
            obj = self.eval(node.obj)
            index = self.eval(node.index)
            return obj[int(index)]
        
        else:
            self.error(f"Unknown node type: {type(node).__name__}")

# ============================================================================
# MAIN REPL
# ============================================================================

def main():
    interpreter = Interpreter()
    
    print("🔷 APEX Programming Language 🔷")
    print("Type 'quit' to exit\n")
    
    while True:
        try:
            line = input("apex> ")
            if line.lower() == 'quit':
                break
            
            if not line.strip():
                continue
            
            lexer = Lexer(line)
            tokens = lexer.tokenize()
            
            parser = Parser(tokens)
            ast = parser.parse()
            
            result = interpreter.eval(ast)
            
            if result is not None:
                print(result)
        
        except (SyntaxError, RuntimeError) as e:
            print(f"❌ {e}")
        except KeyboardInterrupt:
            print("\n^C")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
