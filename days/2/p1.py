from itertools import combinations

presents = []
def read(data: str):
  global presents
  presents = [tuple(map(int, p.split('x'))) for p in data.splitlines()]

def run(data: str, *args):
  read(data)
  result = []
  for dimensions in presents:
    areas = [a * b for a, b in combinations(dimensions, 2)]
    result.append(sum([a * 2 for a in areas]) + min(areas))
  return sum(result)