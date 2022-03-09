import os
from pathlib import Path
from typing import Set

from ander.cli import ander

TEST_DIR: Path = Path(os.path.dirname(os.path.abspath(__file__)))

def test_extract_duplicated_elements() -> None:
  filename1: str = str(TEST_DIR/"data/file1_left.txt")
  filename2: str = str(TEST_DIR/"data/file1_right.txt")
  result: Set[str] = ander(filename1, filename2)
  assert len(result) == 1
  assert list(result)[0] == "duplicated"

