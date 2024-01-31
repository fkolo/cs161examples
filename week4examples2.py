def sum_three(num_1, num_2, num_3):  # The first line is the "function header"
  sum = num_1 + num_2 + num_3
  print("num_1 = ", num_1)
  print("num_2 = ", num_2)
  print("num_3 = ", num_3)
  return sum


def print_choice_v1(num):
    if num == 1:
        print("one")
        return  # immediately ends the function
    print("not one")


def print_choice_v2(num):
    if num == 1:
        print("one")
    else:
        print("not one")


def sum(num_1, num_2, num_3=0): #num_3 has a default argument assigned
  return num_1 + num_2 + num_3


def func():
    num = 12
    print(num)

num = 5
func()
print(num)


#passing a value into a function to see that it only changes the value within the function
def square_val(val):
  val = val * val
  print(val)

num = 8
square_val(num)
print(num)