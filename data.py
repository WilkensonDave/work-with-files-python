from pathlib import Path
import json

numbers = [1, 3, 4, 6, 2, 8, 9, 4]

path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)