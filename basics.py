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


#Python Operators in Python

'''Operators are symbols used to perform operations on values.

1️⃣ Arithmetic Operators
Operator	Meaning	     Example
+	        Addition	 5 + 2 = 7
-	       Subtraction	 5 - 2 = 3
*	     Multiplication	 5 * 2 = 10
/	       Division	     5 / 2 = 2.5
//  	Floor division	 5 // 2 = 2
%	       Modulus	     5 % 2 = 1
**	        Power	     2 ** 3 = 8

2️⃣ Assignment Operators
Operator	Example
=	        x = 5
+=	        x += 2
-=	        x -= 2
*=	        x *= 2
/=	        x /= 2
%=	        x %= 2
//=	        x //= 2
**=	        x **= 2

3️⃣ Comparison Operators
Operator	Meaning	          Example
==	        Equal	          x == y
!=	        Not equal         x != y
>	        Greater than	  x > y
<	        Less than	      x < y
>=	        Greater or equal  x >= y
<=	        Less or equal	  x <= y

4️⃣ Logical Operators
Operator	Meaning	    Example
and	        Both true	x > 1 and y > 1
or	        One true	x > 1 or y > 1
not	        Opposite	not(x > 1)

5️⃣ Identity Operators
Operator	Meaning	     Example
is	        Same object	 x is y
is not	    Not same	 x is not y

6️⃣ Membership Operators
Operator	Meaning	                Example
in	        Present in sequence	    'a' in "apple"
not in	    Not present	            'b' not in "apple"

7️⃣ Bitwise Operators
Operator	Meaning	                Example
&	        AND	                    5 & 3
|	        OR	                    5 | 3
^	        XOR	                    5 ^ 3
~	        NOT	                    ~5
<<	        Left shift	            5 << 1
>>	        Right shift	            5 >> 1
'''

# Shortcut operators
'''
| Expression                | Shortcut operator      |
| ------------------------- | ---------------------- |
|  i = i + 2 * j            |  i += 2 * j            |
|  var = var / 2            |  var /= 2              |
|  rem = rem % 10           |  rem %= 10             |
|  j = j - (i + var + rem)  |  j -= (i + var + rem)  |
|  x = x ** 2               |  x **= 2               |
'''
