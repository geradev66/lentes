
with open(r'c:\Users\particular\Desktop\desafio_latam\lentes\openapi.json', encoding='utf-8') as f:
    content = f.read()

open_braces = 0
for i, char in enumerate(content):
    if char == '{':
        open_braces += 1
    elif char == '}':
        open_braces -= 1
        if open_braces < 0:
            print(f"Extra closing brace at char {i}")

print(f"Final open braces count: {open_braces}")
