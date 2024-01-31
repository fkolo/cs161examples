def odd_or_even(num):
    if num % 2 == 1:
        return "odd"
    else:
        return "even"

input_value = int(input('Please enter an integer: '))
print(odd_or_even(input_value))



def distance(x_coord_1, y_coord_1, x_coord_2, y_coord_2):
    """Returns the distance between two points"""
    x_diff = x_coord_1 - x_coord_2
    y_diff = y_coord_1 - y_coord_2
    result = (x_diff ** 2 + y_diff ** 2) ** 0.5
    return result

print(distance(0,4,3,0))




def factorial(num):
    """Return the factorial of a number"""
    result = 1
    for count in range(1, num+1):
        result = result * count
    return result

def combinations(num_possibilites, num_to_choose):
    """
    Return how many ways a certain number of options can be chosen from among
    a certain number of possibilities
    """
    denominator = factorial(num_possibilites - num_to_choose) * factorial(num_to_choose)
    return int(factorial(num_possibilites) / denominator)

print(combinations(10,3))