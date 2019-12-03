def get_hist(wire):
  x = 0
  y = 0
  steps = 0
  hist = {}

  for move in wire:
    direction = move[0]
    distance = int(move[1:])

    for i in range(distance):
      if direction == 'U':
        y += 1
      elif direction == 'D':
        y -= 1
      elif direction == 'R':
        x += 1
      elif direction == 'L':
        x -= 1

      steps += 1
      c = ','.join([str(x), str(y)])
      if c not in hist:
        hist[c] = steps

  return hist

f = open('3.txt')

wire1 = f.readline().strip().split(',')
wire2 = f.readline().strip().split(',')

hist1 = get_hist(wire1)
hist2 = get_hist(wire2)

keys_1 = set(hist1.keys())
keys_2 = set(hist2.keys())
intersection = keys_1 & keys_2

least_steps = 0
for i in intersection:
  total_steps = hist1[i] + hist2[i]
  if least_steps == 0:
    least_steps = total_steps
  elif total_steps < least_steps:
    least_steps = total_steps

print(least_steps)
