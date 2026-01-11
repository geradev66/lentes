import json
import sys

try:
    with open(r'c:\Users\particular\Desktop\desafio_latam\lentes\openapi.json', encoding='utf-8') as f:
        content = f.read()
        print(f"File length: {len(content)} chars")
        print(f"Last 50 chars: {repr(content[-50:])}")
        json.loads(content)
        print("JSON is valid")
except json.JSONDecodeError as e:
    print(f"JSON Error: {e}")
    print(f"Line {e.lineno}, Column {e.colno}")
    lines = content.splitlines()
    if 0 <= e.lineno - 1 < len(lines):
        print(f"Line content: {lines[e.lineno - 1]}")
except Exception as e:
    print(f"Error: {e}")
