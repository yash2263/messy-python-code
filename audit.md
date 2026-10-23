# README Claims Audit

| Claim in README | True? | Evidence |
|---|---|---|
| Improved script gives the same results as the original | Yes | Input Riya 95 / Kabir 70 / Zoya 40 → average 68.33, max 95, min 40, grades A/C/F in both |
| Unused imports removed | Yes | `improved_script.py` has no imports |
| Invalid input no longer crashes | Yes | Typing `abc` for marks re-prompts instead of raising `ValueError` |
| Marks limited to 0–100 | Yes | `read_int(..., 0, 100)` |
| Grade boundaries defined in one place | Yes | `GRADE_BOUNDARIES` constant |
| Original kept unchanged for comparison | Yes | `messy_script.py` |
