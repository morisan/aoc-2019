cnt = 0
for i in range(128392, 643282):
  test = str(i)
  ok = True
  prev = None
  repeat_cnt = 1
  repeat_cnts = []
  for c in test:
    if not ok:
      break

    j = int(c)
    if prev is not None and j < prev:
      ok = False
    elif j == prev:
      repeat_cnt += 1
    elif repeat_cnt > 1:
      repeat_cnts.append(repeat_cnt)
      repeat_cnt = 1

    prev = j

  if repeat_cnt > 1:
    repeat_cnts.append(repeat_cnt)

  if ok and 2 in repeat_cnts:
    cnt += 1

print(str(cnt))
