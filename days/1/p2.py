def run(data: str, *args) -> int:
  position = 0
  for i, char in enumerate(data):
    if position < 0: return i
    if char == '(': position += 1
    else: position -= 1
  pass