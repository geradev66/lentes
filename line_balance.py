
with open(r'c:\Users\particular\Desktop\desafio_latam\lentes\openapi.json', encoding='utf-8') as f:
    lines = f.readlines()

total_balance = 0
for i, line in enumerate(lines):
    balance = line.count('{') - line.count('}')
    total_balance += balance
    print(f"Line {i+1}: balance {balance}, total {total_balance}")
