import os
from pathlib import Path
from typing import Set

from ander import cli

TEST_DIR: Path = Path(os.path.dirname(os.path.abspath(__file__)))


def test_extract_duplicated_elements_for_file1_and_file2() -> None:
    filename1: str = str(TEST_DIR / "data/file1.txt")
    filename2: str = str(TEST_DIR / "data/file2.txt")
    result: Set[str] = cli.ander(filename1, filename2)
    assert len(result) == 1
    assert list(result)[0] == "duplicated"


def test_extract_duplicated_elements_for_file2_and_file3() -> None:
    filename2: str = str(TEST_DIR / "data/file2.txt")
    filename3: str = str(TEST_DIR / "data/file3.txt")
    result: Set[str] = cli.ander(filename2, filename3)
    assert len(result) == 2
    assert "duplicated" in result
    assert "23duplicated" in result


def test_extract_duplicated_elements_for_file1_and_file2_and_file3() -> None:
    filename1: str = str(TEST_DIR / "data/file1.txt")
    filename2: str = str(TEST_DIR / "data/file2.txt")
    filename3: str = str(TEST_DIR / "data/file3.txt")
    result: Set[str] = cli.ander(filename1, filename2, filename3)
    assert len(result) == 1
    assert list(result)[0] == "duplicated"
