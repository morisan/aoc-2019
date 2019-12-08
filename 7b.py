first = [True, True, True, True, True]
pcs = [0, 0, 0, 0, 0]
mems = [False, False, False, False, False]
def run_amplifier(phase, input_val, amp_num):
  if not mems[amp_num]:
    mems[amp_num] = open('7.txt').readline().strip().split(',')
  mem = mems[amp_num]

  while (True):
    pc = pcs[amp_num]
    instr = mem[pc]
    op = instr if len(instr) < 2 else instr[-2:]
    modes = instr[:-2]
    m1 = modes[-1] if len(modes) >= 1 else '0'
    m2 = modes[-2] if len(modes) >= 2 else '0'

    op = int(op)
    if op == 1:
      a = int(mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])])
      b = int(mem[pc+2] if m2 == '1' else mem[int(mem[pc+2])])
      mem[int(mem[pc+3])] = a + b
      pcs[amp_num] += 4
    elif op == 2:
      a = int(mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])])
      b = int(mem[pc+2] if m2 == '1' else mem[int(mem[pc+2])])
      mem[int(mem[pc+3])] = a * b
      pcs[amp_num] += 4
    # Save input to mem
    elif op == 3:
      mem[int(mem[pc+1])] = phase if first[amp_num] else input_val
      first[amp_num] = False
      pcs[amp_num] += 2
    # Output value from mem
    elif op == 4:
      a = mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])]
      pcs[amp_num] += 2
      return a
    # jump-if-true
    elif op == 5:
      a = int(mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])])
      b = int(mem[pc+2] if m2 == '1' else mem[int(mem[pc+2])])
      if a != 0:
        pcs[amp_num] = b
      else:
        pcs[amp_num] += 3
    # jump-if-false
    elif op == 6:
      a = int(mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])])
      b = int(mem[pc+2] if m2 == '1' else mem[int(mem[pc+2])])
      if a == 0:
        pcs[amp_num] = b
      else:
        pcs[amp_num] += 3
    # less than
    elif op == 7:
      a = int(mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])])
      b = int(mem[pc+2] if m2 == '1' else mem[int(mem[pc+2])])
      mem[int(mem[pc+3])] = 1 if a < b else 0
      pcs[amp_num] += 4
    # equals
    elif op == 8:
      a = int(mem[pc+1] if m1 == '1' else mem[int(mem[pc+1])])
      b = int(mem[pc+2] if m2 == '1' else mem[int(mem[pc+2])])
      mem[int(mem[pc+3])] = 1 if a == b else 0
      pcs[amp_num] += 4
    elif op == 99:
      return 'HALT'
    else:
      print('whoops!')
      break

max_signal = 0
phases = [5, 6, 7, 8, 9]
done = False
while not done:
  done = sum(phases) == 45

  first = [True, True, True, True, True]
  pcs = [0, 0, 0, 0, 0]
  mems = [False, False, False, False, False]

  unique = list(set(phases))
  if (len(unique) == 5):
    halt = False
    signal = 0
    while not halt:
      for amp_num, p in enumerate(phases):
        res = run_amplifier(p, signal, amp_num)
        if res == 'HALT':
          halt = True
          break
        else:
          signal = res

    signal = int(signal)
    if signal > max_signal:
      max_signal = signal

  for i in reversed(range(0, 5)):
    if phases[i] < 9:
      phases[i] += 1
      for j in range(i + 1, 5):
        phases[j] = 5
      break

print(max_signal)
