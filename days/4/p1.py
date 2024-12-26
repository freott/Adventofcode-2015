import hashlib


def run(data: str, *args) -> int:
  number = 0
  print(number)
  while(True):
    md5_hash = hashlib.md5(f'{data}{number}'.encode()).hexdigest()
    if md5_hash[:5] == '00000': 
      print(f'{data}{number}')
      print(md5_hash)
      print(number)
      break
    number += 1
  return number