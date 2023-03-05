"""
Write a Python function called max_num()to find the maximum of three numbers.
Write a Python function called mult_list() to multiply all the numbers in a list.
Write a Python function called rev_string() to reverse a string.
Write a Python function called num_within() to check whether a number falls in a given range.
The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
The function accepts the number n, the number of rows to print
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
"""
#1
def max_num(a,b,c):
  return max([a,b,c])
print(max_num(1,2,3))
print(max_num(3,6,9))
print(max_num(24,43,13))

#2
def mult_list(list):
  if len(list) == 0:
    return 0
  prod = list[0]
  if len(list) > 1:
    for i in list[1:]:
      prod = prod * i
  return prod

print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([7,43]))
  
#3
def rev_string(my_str):
  return my_str[::-1]

print(rev_string(""))
print(rev_string("hello world"))
print(rev_string("sea string"))
  
#4
def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(0,2,4))     
print(num_within(3,6,9))     
print(num_within(13,7,21))

#triangle
triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]

      length = len(row_prev)+1
      for i in range(length):
     
        if i == 0:
          row.append(1)
 
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])

        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)

pascal(2)
pascal(5)