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