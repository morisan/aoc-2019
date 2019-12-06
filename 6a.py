lines = open('6.txt').readlines()

mapping = {}
for l in lines:
  [node, orbit] = list(l.strip().split(')'))

  if node in mapping:
    mapping[node].append(orbit)
  else:
    mapping[node] = [orbit]

def cnt_orbits(node, level=0):
  cnt = 0
  if node in mapping:
    children = mapping[node]
    for c in children:
      cnt += cnt_orbits(c, level + 1)

  return level + cnt

print(cnt_orbits('COM'))
