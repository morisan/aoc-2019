import collections

BLACK = 0
WHITE = 1
LEFT = 0
RIGHT = 1

directions = collections.deque(['U', 'R', 'D', 'L'])
pos = (0, 0)
grid = {}


def move_robot(color, turn):
  global pos
  global grid

  grid[pos] = '#' if color == WHITE else '.'

  if turn == LEFT:
    directions.rotate(1)
  elif turn == RIGHT:
    directions.rotate(-1)

  [x, y] = list(pos)
  d = directions[0]
  if d == 'U':
    pos = (x, y+1)
  elif d == 'R':
    pos = (x+1, y)
  elif d == 'D':
    pos = (x, y-1)
  elif d == 'L':
    pos = (x-1, y)

  return


mem = open('11.txt').readline().strip().split(',')
pc = 0
base = 0
mem += (['0'] * 1000)


def get_val(mode, operand):
    # position
    if mode == '0':
        return float(mem[operand])
    # immediate
    elif mode == '1':
        return float(operand)
    # relative
    elif mode == '2':
        return float(mem[base + operand])
    else:
        print('Invalid mode: ' + mode)


color = None
turn = None

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
        # reset
        color = None
        turn = None

        i = 0 if pos in grid and grid[pos] == '.' else 1

        offset = 0 if m1 == '0' else base
        mem[offset + int(mem[pc+1])] = i
        pc += 2
    # Output value from mem
    elif op == 4:
        a = get_val(m1, int(mem[pc+1]))
        a = int(a)
        pc += 2

        if color is None:
            color = a
        elif turn is None:
            turn = a
            move_robot(color, turn)

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
        cnt = len(grid)

        max_x = 0
        min_x = 0
        max_y = 0
        min_y = 0
        for p, c in grid.items():
          [x, y] = list(p)

          if x > max_x:
            max_x = x
          elif x < min_x:
            min_x = x

          if y > max_y:
            max_y = y
          elif y < min_y:
            min_y = y


        lines = []
        for y in reversed(range(min_y, max_y+1)):
          line = ''
          for x in range(min_x, max_x+1):
            if (x, y) in grid:
              line += grid[(x, y)]
            else:
              line += '#'
          print(line.replace('#', '█').replace('.', ' '))
        break
    else:
        print('Invalid op: ' + str(op))
        break
