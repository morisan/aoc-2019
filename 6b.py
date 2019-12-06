lines = open('6.txt').readlines()

mapping = {}
for l in lines:
  [node, orbit] = list(l.strip().split(')'))

  if node in mapping:
    mapping[node].append(orbit)
  else:
    mapping[node] = [orbit]

def find_parent(child):
  for parent, children in mapping.items():
    if child in children:
      return parent
  return False

def find_ancestors(child, ancestors):
  parent = find_parent(child)
  if parent:
    ancestors.append(parent)
    return find_ancestors(parent, ancestors)
  else:
    return ancestors

def find_orbital_distance(a, b):
  a_ancestors = find_ancestors('YOU', [])
  b_ancestors = find_ancestors('SAN', [])

  for i, a in enumerate(a_ancestors):
    for j, b in enumerate(b_ancestors):
      if a == b:
        return i+j

print(find_orbital_distance('YOU', 'SAN'))
