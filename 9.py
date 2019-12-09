mem = open('9.txt').readline().strip().split(',')
pc = 0
base = 0

mem += (['0'] * 1000)

def get_val(mode, operand):
  # position
  if   mode == '0':
    return float(mem[operand])
  # immediate
  elif mode == '1':
    return float(operand)
  # relative
  elif mode == '2':
    return float(mem[base + operand])
  else:
    print('Invalid mode: ' + mode)

while (True):
  instr = str(int(mem[pc]))
  op = instr if len(instr) < 2 else instr[-2:]
  modes = instr[:-2]
  m1 = modes[-1] if len(modes) >= 1 else '0'
  m2 = modes[-2] if len(modes) >= 2 else '0'
  m3 = modes[-3] if len(modes) >= 3 else '0'

  op = int(op)
  if op == 1:
    a = get_val(m1, int(mem[pc+1]))
    b = get_val(m2, int(mem[pc+2]))
    offset = 0 if m3 == '0' else base
    mem[offset + int(mem[pc+3])] = a + b
    pc += 4
  elif op == 2:
    a = get_val(m1, int(mem[pc+1]))
    b = get_val(m2, int(mem[pc+2]))
    offset = 0 if m3 == '0' else base
    mem[offset + int(mem[pc+3])] = a * b
    pc += 4
  # Save input to mem
  elif op == 3:
    offset = 0 if m1 == '0' else base
    mem[offset + int(mem[pc+1])] = input('Input: ').strip()
    pc += 2
  # Output value from mem
  elif op == 4:
    a = get_val(m1, int(mem[pc+1]))
    print(int(a))
    pc += 2
  # jump-if-true
  elif op == 5:
    a = get_val(m1, int(mem[pc+1]))
    b = get_val(m2, int(mem[pc+2]))
    if a != 0.0:
      pc = int(b)
    else:
      pc += 3
  # jump-if-false
  elif op == 6:
    a = get_val(m1, int(mem[pc+1]))
    b = get_val(m2, int(mem[pc+2]))
    if a == 0.0:
      pc = int(b)
    else:
      pc += 3
  # less than
  elif op == 7:
    a = get_val(m1, int(mem[pc+1]))
    b = get_val(m2, int(mem[pc+2]))
    offset = 0 if m3 == '0' else base
    mem[offset + int(mem[pc+3])] = 1 if a < b else 0
    pc += 4
  # equals
  elif op == 8:
    a = get_val(m1, int(mem[pc+1]))
    b = get_val(m2, int(mem[pc+2]))
    offset = 0 if m3 == '0' else base
    mem[offset + int(mem[pc+3])] = 1 if a == b else 0
    pc += 4
  # relative base offset
  elif op == 9:
    a = get_val(m1, int(mem[pc+1]))
    base += int(a)
    pc += 2
  elif op == 99:
    break
  else:
    print('Invalid op: ' + str(op))
    break
