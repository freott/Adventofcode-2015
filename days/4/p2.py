import hashlib

def run(data: str, *args) -> int:
  number = 0
  while(True):
    md5_hash = hashlib.md5(f'{data}{number}'.encode()).hexdigest()
    if md5_hash[:6] == '000000': 
      break
    number += 1
  return number