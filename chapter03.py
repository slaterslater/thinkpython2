# Think Python 2
# Chapter 03, page 26

# takes a string and prints with enough leading space so that last char is in col 70
def right_justify(s):
  print(' '*(70 - len(s)),s)

def do_twice(f,s):
  f(s)
  f(s)

def print_twice(s):
  print(s)
  print(s)

def do_four(f,s):
  do_twice(f,s)  
  do_twice(f,s)  

# Exercise 3.3) print 2x2 and 4x4 grids without using loops 

def print_row(c):
  print('+','- - - - + '*c)

def print_cols(c):
  print('|','        | '*c)

def make_cols(n):
  do_four(print_cols,n)
  print_row(n)  


def two_by_two():
  print_row(2)
  do_twice(make_cols,2)

def four_by_four():
  print_row(4)
  do_four(make_cols, 4)