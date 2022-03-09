import fire
from typing import Set

def ander(filename1:str, filename2:str, verbose:bool=False) -> None:
  with open(filename1) as f1, open(filename2) as f2:
    set1: Set[str] = set([ s.strip() for s in f1.readlines() ])
    set2: Set[str] = set([ s.strip() for s in f2.readlines() ])
  res_set: Set[str] = set1.intersection(set2)
  for s in res_set: 
    print(s)
  if verbose:
    print(f"#Intersected elements: {len(res_set):,d}")
  return

def main() -> int:
  fire.Fire(ander)
  return 0

if __name__ == '__main__':
  main()
