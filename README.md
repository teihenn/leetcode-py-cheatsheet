# leetcode-py-cheatsheet

[![Python Tests](https://github.com/teihenn/leetcode-py-cheatsheet/actions/workflows/ci.yaml/badge.svg)](https://github.com/teihenn/leetcode-py-cheatsheet/actions/workflows/ci.yaml)

Quick reference for common LeetCode Python techniques and patterns.

## Running Tests

This project uses Python's standard library `unittest` for testing and `uv` as the Python package installer and development server.

### Run all tests

```bash
uv run python -m unittest discover test
```

### Run all tests with verbose output

```bash
uv run python -m unittest discover test -v
```

### Run a specific test file

```bash
uv run python -m unittest test/test_anagram.py
```

### Run a specific test class

```bash
uv run python -m unittest test.test_anagram.TestAnagramMethods
```

### Run a specific test method

```bash
uv run python -m unittest test.test_anagram.TestAnagramMethods.test_are_anagrams_sorting
```
