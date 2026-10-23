"""Student marks report - cleaned-up version of messy_script.py.

Reads student names and marks, then prints the class average, highest and
lowest marks, and a letter grade for every student.
"""

GRADE_BOUNDARIES = [(90, "A"), (75, "B"), (50, "C")]
FAIL_GRADE = "F"


def average(marks: list[int]) -> float:
    """Return the mean of the marks (0.0 for an empty list)."""
    return sum(marks) / len(marks) if marks else 0.0


def letter_grade(mark: int) -> str:
    """Return the letter grade for a single mark."""
    for boundary, grade in GRADE_BOUNDARIES:
        if mark >= boundary:
            return grade
    return FAIL_GRADE


def read_int(prompt: str, low: int = 0, high: int | None = None) -> int:
    """Keep asking until the user types a valid whole number in range."""
    while True:
        try:
            value = int(input(prompt))
            if value < low or (high is not None and value > high):
                raise ValueError
            return value
        except ValueError:
            limit = f"{low}-{high}" if high is not None else f">= {low}"
            print(f"  Please enter a whole number ({limit}).")


def collect_students() -> list[tuple[str, int]]:
    count = read_int("How many students? ", low=1)
    students = []
    for i in range(1, count + 1):
        name = input(f"Name of student {i}: ").strip() or f"Student {i}"
        mark = read_int(f"Marks for {name} (0-100): ", 0, 100)
        students.append((name, mark))
    return students


def print_report(students: list[tuple[str, int]]) -> None:
    marks = [mark for _, mark in students]
    print("\n--- Class Report ---")
    print(f"Average : {average(marks):.2f}")
    print(f"Highest : {max(marks)}")
    print(f"Lowest  : {min(marks)}")
    print("\n--- Grades ---")
    for name, mark in students:
        print(f"{name:<15} {mark:>3}  {letter_grade(mark)}")


def main() -> None:
    print_report(collect_students())


if __name__ == "__main__":
    main()
