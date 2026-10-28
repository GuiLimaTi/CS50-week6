# CS50x Week 6 – Python

Problem sets from Week 6 of Harvard's CS50x, rewriting earlier C programs in Python and processing CSV and text data.

**Language:** Python · **Course:** [CS50x](https://cs50.harvard.edu/x/) · **Status:** Completed (2026)

## Overview

This week marked the move from C to Python. I re-implemented earlier problems in fewer lines and built a DNA profiling program that reads CSV and text files.

## Projects

| Project | File | Description | Key concepts |
|---|---|---|---|
| Hello | `hello.py` | Greets the user by name | Input and output in Python |
| Mario | `mario.py` | Prints a pyramid of a chosen height | Loops, input validation |
| Cash | `cash.py` | Calculates the minimum number of coins for change | Greedy algorithm, avoiding float errors |
| Readability | `readability.py` | Estimates a text's reading grade level (Coleman–Liau index) | String processing |
| DNA | `dna.py` | Identifies a person by matching DNA STR counts against a CSV database | `csv` module, dictionaries, `sys.argv` |

## How to run

```bash
python dna.py databases/large.csv sequences/5.txt
```

The DNA databases and sequences come from the CS50 problem set distribution files.

## What I learned

- How much faster it is to express logic in Python than in C
- Reading and comparing data from CSV and text files
- Using lists and dictionaries to organise data
- Handling command-line arguments in Python

## Academic honesty

These solutions were written by me as part of CS50x. If you're taking the course, please follow CS50's [academic honesty policy](https://cs50.harvard.edu/x/honesty/) and write your own code.

---

**Guilherme Lima** · Aspiring IT Support Technician · [LinkedIn](https://www.linkedin.com/in/glimaalmeida) · [GitHub](https://github.com/GuiLimaTi)
