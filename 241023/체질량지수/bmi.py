from math import floor

h, w = map(int, input().split())

bmi = 10000*w / h**2

print(f"{floor(bmi):.0f}")
if bmi > 25:
    print("Obesity")