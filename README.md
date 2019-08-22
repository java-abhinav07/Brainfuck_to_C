# Brainfuck_to_C

# To do make GUI

# Introduction

Brainfuck is one of the most well-known esoteric programming languages. But it can be hard to understand any code longer that 5 characters. In this kata you have to solve that problem.

Description

In this kata you have to write a function which will do 3 tasks:

Optimize the given Brainfuck code.
Check it for mistakes.
Translate the given Brainfuck programming code into C programming code.
More formally about each of the tasks:

Your function has to remove from the source code all useless command sequences such as: '+-', '<>', '[]'. Also it must erase all characters except +-<>,.[].

If the source code contains unpaired braces, your function should return "Error!" string.
Your function must generate a string of the C programming code as follows: 

Sequences of the X commands + or - must be replaced by \*p += X;\n or \*p -= X;\n.

Sequences of the Y commands > or < must be replaced by p += Y;\n or p -= Y;\n.

. command must be replaced by putchar(\*p);\n.

, command must be replaced by \*p = getchar();\n.

[ command must be replaced by if (\*p) do {\n. ] command must be replaced by } while (\*p);\n.

Each command in the code block must be shifted 2 spaces to the right accordingly to the previous code block.


Input:

+++++[>++++.<-]

Output:

*p += 5;

if (*p) do {

  p += 1;
  
  *p += 4;
  
  putchar(*p);
  
  p -= 1;
  
  *p -= 1;
  
} while (*p);
