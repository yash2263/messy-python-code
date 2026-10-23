# Messy Python Code Improvement

A student-marks script rewritten with AI assistance to be **readable, safe and maintainable**, with the same output.

- `messy_script.py` — the original version (kept unchanged for comparison)
- `improved_script.py` — the cleaned-up version

## What the program does
Asks for a number of students, their names and marks, then prints the class average, highest and lowest marks, and a letter grade (A/B/C/F) for each student.

## What was improved
| Problem in `messy_script.py` | Fix in `improved_script.py` |
|---|---|
| Meaningless names: `f`, `g`, `h`, `l`, `mm`, `mk` | Descriptive names: `average`, `letter_grade`, `students`, `marks` |
| Unused imports (`os`, `sys`, `math`) | Removed |
| Hand-written loops to find max / min / sum | Built-ins `max()`, `min()`, `sum()` |
| Mixed 1-, 2- and 4-space indentation | Consistent PEP 8 formatting |
| Crashes on non-number input (`int("abc")`) | `read_int()` re-asks until input is valid and in range 0–100 |
| Crashes with 0 students (division by zero) | Minimum of 1 student enforced; `average([])` returns 0.0 |
| Grade boundaries hard-coded in an if/elif chain | One `GRADE_BOUNDARIES` table — change a boundary in one place |
| All code at top level | Split into small functions with docstrings and a `main()` guard |
| Unformatted output (`avg 68.33333333`) | Aligned report, average rounded to 2 decimals |
| Prompts with no spacing (`how many students`) | Clear prompts: `How many students? ` |

## Same result, cleaner code
```
--- Class Report ---
Average : 68.33
Highest : 95
Lowest  : 40

--- Grades ---
Riya             95  A
Kabir            70  C
Zoya             40  F
```

## How to run
Requires Python 3.10+.
```bash
python messy_script.py      # original
python improved_script.py   # improved
```
