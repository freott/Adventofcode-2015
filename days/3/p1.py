dd = { 
  '^': [-1, 0],
  '>': [0, 1], 
  'v': [1, 0], 
  '<': [0, -1]
}
def run(data: str, *args) -> int:
  pos = (0, 0)
  houses = { pos: 1 }
  for dir in data:
    pos = (pos[0] + dd[dir][0], pos[1] + dd[dir][1])
    houses.setdefault(pos, 0)
    houses[pos] += 1
    
  return len([v for v in houses.values() if v > 0])