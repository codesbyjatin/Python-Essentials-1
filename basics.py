#Python – a tool, not a reptile

#Python – the language of today and tomorrow

#Python was created by Guido van Rossum in 1991.
#He was a fan of the comedy show Monty Python's Flying Circus.
#He chose the name “Python” because it sounded short, unique, and fun, not because of the snake.

'''What makes a language?

We can say that each language (machine or natural, it doesn't matter) consists of the following elements:
1. Alphabet → symbols  
2. Lexis → words  
3. Syntax → rules for writing  
4. Semantics → meaning or set of rules'''


#function_name(argument)

print("Hisssssss...") # print() is a built-in function that outputs the specified message to the screen.
#You can use print() many times. Each print() shows output on a new line.
#Text (strings) in Python must be inside quotes — either " " or ' '.




#Python Indentation
'''
Indentation refers to the spaces at the beginning of a code line.
Python uses indentation to indicate a block of code.
Python usually uses 4 spaces for indentation.
'''

if 5>3:
    print("5 is greater than 3")



#Comments
'''Comments are notes in the code that help explain the program and are not executed by Python.'''

# This is a single-line comment
print("Hisssssss...")

'''this is 
a multi-line 
comment
'''


#Python Escape and Newline Characters'''
'''  
| Escape | Meaning      |
| ------ | ------------ |
| `\n`   | New line     |
| `\t`   | Tab          |
| `\\`   | Backslash    |
| `\'`   | Single quote |
| `\"`   | Double quote |
'''

print(" \\ \"Python\"  \n  \tis  \n  \'fun\'  \\  ")


#Using multiple arguments

print("Python","is","easy") #print() can take multiple arguments separated by commas.
print("Sum =", 5 + 3) # By default, print() separates arguments with a space
print("python"); print("is"); print("fun")#You can write multiple statements on one line by separating them with ; but it's generally not recommended for readability. and it will print each statement on a new line by default.



'''Keyword Arguments in Python
Keyword arguments are arguments passed using parameter names.
In print(), common keyword arguments are sep and end.'''

'''
| Keyword argument | Purpose                             |
| ---------------- | ----------------------------------- |
| `sep`            | changes separator between arguments |
| `end`            | changes what is printed at the end  |
'''

print("2026", "03", "14", sep="-", end=" DONE")
#2026-03-14 DONE

#If you want to print multiple words on the same line, you can use the end parameter:
print("\n python", end=" "); print("is",end=" "); print("fun", end=" ")



#Variables – data-shaped boxes
'''
x = 5 (𝐱 is variable)	; (𝟓 is literal)
Variables are containers for storing data values.
A variable is created the moment you first assign a value to it.
'''

#Variable Names
'''
Rules for Python variables:
    
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''
#Multi Words Variable Names
'''
Camel Case - Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case - Each word starts with a capital letter:
MyVariableName = "John"

Snake Case - Each word is separated by an underscore character:
my_variable_name = "John"
'''

#Keywords
'''
Keywords are reserved words that have a special meaning in Python and cannot be used as variable names.

| Category              | Keywords                            | Example               |
| --------------------- | ----------------------------------- | --------------------- |
| Boolean values        | `True`, `False`, `None`             | `x = True`            |
| Conditions            | `if`, `elif`, `else`                | `if x > 5:`           |
| Loops                 | `for`, `while`, `break`, `continue` | `for i in range(5):`  |
| Logical operators     | `and`, `or`, `not`                  | `if a > 1 and b > 1:` |
| Functions             | `def`, `return`, `lambda`           | `def add():`          |
| Classes               | `class`                             | `class Car:`          |
| Imports               | `import`, `from`, `as`              | `import math`         |
| Error handling        | `try`, `except`, `finally`, `raise` | `try:`                |
| Variables scope       | `global`, `nonlocal`                | `global x`            |
| Special statements    | `pass`, `del`, `assert`             | `pass`                |
| Async programming     | `async`, `await`                    | `async def func():`   |
| Generators            | `yield`                             | `yield x`             |
| Context manager       | `with`                              | `with open(file)`     |
| Identity / membership | `is`, `in`                          | `if x in list:`       |

'''

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
a = b = c = "Orange"
print(a)
print(b)
print(c)


x = 10   # global variable
def show():
    y = 5   # local variable
    print("Local:", y)
    print("Global:", x)
show()