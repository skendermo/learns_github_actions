import sys
from pylint import lint

THRESHOLD = 9

run = lint.Run(["factorial.py"])

score = run.linter.stats["global_note"]

print(score)

if score < THRESHOLD:
    """Linter message."""
    print("Linter failed: Score < threshold value")
    sys.exit(1)

print("something")

