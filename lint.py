import sys
from pylint.lint import Run

THRESHOLD = 9

run = Run(["factorial.py"],do_exit=False)

score = run.linter.stats["global_note"]

print(score)

if score < THRESHOLD:
    """Linter message."""
    print("Linter failed: Score < threshold value")
    sys.exit(1)

print("something bla")

sys.exit(0)

