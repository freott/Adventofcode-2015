def run(data: str, *args) -> int:
  nice_count = 0
  for str in data.splitlines():
    vowels_count = 0
    twice = False
    valid = True
    for i, c in enumerate(str):
      prev_c = str[i - 1]
      word = prev_c + c
      print(word)
      if i != 0 and word in ['ab', 'cd', 'pq', 'xy']:
        valid = False
        break
      if c in ['a', 'e', 'i', 'o', 'u']:
        vowels_count += 1
      if i != 0 and prev_c == c:
        twice = True
    if vowels_count > 2 and twice and valid:
      nice_count += 1
      
  print(len(data.splitlines()))
  return nice_count