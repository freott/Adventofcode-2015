def run(data: str, *args) -> int:
  nice_count = 0
  for str in data.splitlines():
    pair = False
    repeat = False
    for i, c in enumerate(str):
      prev_c = str[i - 1]
      word = prev_c + c
      if i > 1 and not repeat and c == str[i - 2]:
          repeat = True
      if i > 0 and not pair and word in str[:i - 1] + '..' + str[i + 1:]:
        pair = True
    if pair and repeat: nice_count += 1
      
  return nice_count