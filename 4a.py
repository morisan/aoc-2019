cnt = 0
for i in range(128392, 643282):
  test = str(i)
  ok = True
  has_adj = False
  prev = None
  for c in test:
    if not ok:
      break

    j = int(c)
    if prev is not None and j < prev:
      ok = False
    elif j == prev:
      has_adj = True

    prev = j

  if ok and has_adj:
    cnt += 1

print(str(cnt))
