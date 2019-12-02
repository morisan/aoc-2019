def get_ans(noun, verb):
  lines = open('2.txt').readlines()[0].strip().split(',')
  for i in range(0, len(lines)):
    lines[i] = int(lines[i])

  lines[1] = noun
  lines[2] = verb

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

  ans = lines[0]
  return ans

for noun in range(0, 100):
  for verb in range(0, 100):
    if get_ans(noun, verb) == 19690720:
      ans = 100 * noun + verb
      print(ans)
