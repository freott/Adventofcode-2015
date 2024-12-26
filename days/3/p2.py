dd = { 
  '^': [-1, 0],
  '>': [0, 1], 
  'v': [1, 0], 
  '<': [0, -1]
}
def run(data: str, *args) -> int:
  houses = {
    (0,0): 1
  }
  pos = {
    'santa': (0, 0),
    'robot': (0, 0)
  }
  for i, dir in enumerate(data):
    actor = 'santa' if i % 2 == 0 else 'robot'

    pos[actor] = (
      pos[actor][0] + dd[dir][0], 
      pos[actor][1] + dd[dir][1]
    )
    
    houses.setdefault(pos[actor], 0)
    houses[pos[actor]] += 1
    
  return len([v for v in houses.values() if v > 0])