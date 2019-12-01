lines = open('1.txt').readlines()

res = 0
for mass in lines:
  res += int(int(mass)/3) - 2

print(res)
