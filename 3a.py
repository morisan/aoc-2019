def get_hist(wire):
  x = 0
  y = 0
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

      c = ','.join([str(x), str(y)])
      hist[c] = 1

  return hist

f = open('3.txt')

wire1 = f.readline().strip().split(',')
wire2 = f.readline().strip().split(',')

hist1 = get_hist(wire1)
hist2 = get_hist(wire2)

keys_1 = set(hist1.keys())
keys_2 = set(hist2.keys())
intersection = keys_1 & keys_2

m_dist = 0
for i in intersection:
  c = i.split(',')
  m_dist_new = abs(int(c[0])) + abs(int(c[1]))
  if m_dist == 0:
    m_dist = m_dist_new
  elif m_dist > m_dist_new:
    m_dist = m_dist_new

print(abs(m_dist))
