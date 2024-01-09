import sys
from pylint import lint

THRESHOLD = 5

run = lint.Run(["factorial.py"])

score = run.linter.stats["global_note"]

if score < THRESHOLD:
    """Linter message."""
    print("Linter failed: Score < threshold value")

    sys.exit(1)

sys.exit(0)