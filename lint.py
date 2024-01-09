import sys
from pylint.lint import Run

THRESHOLD = 9

print("something bla")

run = Run(["factorial.py"])

score = run.linter.stats["global_note"]

print(score)

if score < THRESHOLD:
    """Linter message."""
    print("Linter failed: Score < threshold value")
    sys.exit(1)
sys.exit(0)

