lines = open('2.txt').readlines()[0].strip().split(',')
for i in range(0, len(lines)):
  lines[i] = int(lines[i])

lines[1] = 12
lines[2] = 2

pc = 0
op = lines[pc]
while (op != 99):

  if op == 1:
    a = lines[lines[pc+1]]
    b = lines[lines[pc+2]]
    lines[lines[pc+3]] = a + b
    pc += 4
  elif op == 2:
    a = lines[lines[pc+1]]
    b = lines[lines[pc+2]]
    lines[lines[pc+3]] = a * b
    pc += 4
  else:
    pc += 1

  op = lines[pc]

print(lines[0])
