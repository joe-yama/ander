# ander: A CLI tool to identify elements that are contained in both file

## Basic Usage

```bash
$ cat file1.txt
duplicated
notduplicated

$ cat file2.txt
duplicated
not duplicated

$ ander file1.txt file2.txt
duplicated
```

## Installation

```bash
$ pip intall ander
```

### Requirements

- Python >= 3.6
- Some Python Libraries (see `pyproject.toml`)

## License

This software is released under the MIT License, see LICENSE.
