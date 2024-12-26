from functools import reduce
from itertools import combinations
from operator import mul

presents = []
def read(data: str):
  global presents
  presents = [tuple(map(int, p.split('x'))) for p in data.splitlines()]

def run(data: str, *args):
  read(data)
  result = []
  for dimensions in presents:
    result.append(
      sum([d + d for d in sorted(dimensions)[:2]])
      + reduce(mul, dimensions, 1)
    )
  return sum(result)