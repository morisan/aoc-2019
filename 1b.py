lines = open('1.txt').readlines()

def calc_fuel(mass):
  fuel = int(int(mass)/3) - 2
  return 0 if fuel <= 0 else fuel + calc_fuel(fuel)

res = 0
for mass in lines:
  res += calc_fuel(mass)

print(res)
