from pathlib import Path

path = Path('pi_digits.txt')
content = path.read_text()
lines = content.splitlines()
text = ""

for line in lines:
    text += line.lstrip()

print(text)
print(len(text))