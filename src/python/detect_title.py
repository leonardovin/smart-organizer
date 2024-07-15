import re

def detect_title(text):
    # Simple heuristic: the first line with a certain length and/or pattern
    lines = text.split("\n")
    for line in lines:
        if re.match(r'^[A-Z][a-z]* .*', line) and len(line) > 5:
            return line.strip()
    return None
