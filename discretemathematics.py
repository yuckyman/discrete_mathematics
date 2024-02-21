
# discrete mathematics practice
## also effectively serves as a formula cheat sheet

# set theory

set_a = {1, 3, 5, 7}
set_b = {2, 3, 6}

is_subset = set_b.issubset(set_a) # true if set_b is a subset of set_a
union_set = set_a.union(set_b) # {1, 2, 3, 5, 6, 7}
intersection_set = set_a.intersection(set_b) # {3}
difference_set = set_a.difference(set_b) # {1, 5, 7}

# print("The intersection of set_a and set_b is", intersection_set)
# print("The difference_set of set_a,", set_a, ", and set_b,", set_b, "is", difference_set)



# combinatorics

import math
num_permutations = math.factorial(5) # 5! = 120

# print(num_permutations)

def combinations(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

num_combinations = combinations(8, 3) # 8 choose 3 = 56

# print(num_combinations)


# power set
def generate_subsets(data):
  """Generates all possible subsets of a given set."""
  if not data:
    yield set()  # Yield an empty set
  else:
    element = data.pop()  # Remove an arbitrary element 
    for subset in generate_subsets(data.copy()):  # Work on a copy
      yield subset
      yield subset.union({element})  # Add the element back
    data.add(element)  # Restore the set for the next iteration 

def power_set(data):
  """Generates the power set of a given set."""
  return list(generate_subsets(data))  # Convert result to a list

def count_powerset_elements(data):
  """Calculates the number of sets in the power set of a given set."""
  num_elements = len(data)
  return 2 ** num_elements

# Example usage
my_set = {"c", "o", "m", "p", "u", "t", "e", "r"}
powerset = power_set(my_set)
print(powerset) 

# Example Usage
num_subsets = count_powerset_elements(my_set)
print("The power set of", my_set, "has", num_subsets, "sets")
