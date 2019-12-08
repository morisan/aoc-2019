def run_amplifier(phase, input_val):
  mem = open('7.txt').readline().strip().split(',')

  first_input = True

  pc = 0
  instr = mem[pc]
  op = instr if len(instr) < 2 else instr[-2:]
  while (op != '99'):
    modes = instr[:-2]
    m1 = modes[-1] if len(modes) >= 1 else '0'
    m2 = modes[-2] if len(modes) >= 2 else '0'

    op = int(op)
    if op == 1:
      a = int(mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])])
      b = int(mem[pc+2] if m2 == '1' else mem[int(mem[pc+2])])
      mem[int(mem[pc+3])] = a + b
      pc += 4
    elif op == 2:
      a = int(mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])])
      b = int(mem[pc+2] if m2 == '1' else mem[int(mem[pc+2])])
      mem[int(mem[pc+3])] = a * b
      pc += 4
    # Save input to mem
    elif op == 3:
      mem[int(mem[pc+1])] = phase if first_input else input_val
      first_input = False
      pc += 2
    # Output value from mem
    elif op == 4:
      a = mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])]
      pc += 2
      return a
    # jump-if-true
    elif op == 5:
      a = int(mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])])
      b = int(mem[pc+2] if m2 == '1' else mem[int(mem[pc+2])])
      if a != 0:
        pc = b
      else:
        pc += 3
    # jump-if-false
    elif op == 6:
      a = int(mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])])
      b = int(mem[pc+2] if m2 == '1' else mem[int(mem[pc+2])])
      if a == 0:
        pc = b
      else:
        pc += 3
    # less than
    elif op == 7:
      a = int(mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])])
      b = int(mem[pc+2] if m2 == '1' else mem[int(mem[pc+2])])
      mem[int(mem[pc+3])] = 1 if a < b else 0
      pc += 4
    # equals
    elif op == 8:
      a = int(mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])])
      b = int(mem[pc+2] if m2 == '1' else mem[int(mem[pc+2])])
      mem[int(mem[pc+3])] = 1 if a == b else 0
      pc += 4
    else:
      print('whoops!')
      break

    instr = str(mem[pc])
    op = instr if len(instr) < 2 else instr[-2:]


max_signal = 0
phases = [0, 1, 2, 3, 4]
done = False
while not done:
  if (sum(phases) == 20):
    done = True

  unique = list(set(phases))
  if (len(unique) == 5):
    signal = 0
    for p in phases:
      signal = run_amplifier(p, signal)

    if signal > max_signal:
      max_signal = signal

  for i in reversed(range(0,5)):
    if phases[i] < 4:
      phases[i] += 1
      for j in range(i + 1, 5):
        phases[j] = 0
      break

print(max_signal)
