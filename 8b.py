line = open('8.txt').readline().strip()

w = 25
h = 6
num_pixels = w * h

ans = None

for i in range(0, len(line), num_pixels):
  img_data = list(line[i:i+num_pixels])

  if ans is None:
    ans = img_data
  else:
    for i,v in enumerate(img_data):
      if ans[i] == '2':
        ans[i] = v

ans = ''.join(ans)
ans = ans.replace('0', ' ')
ans = ans.replace('1', '█')

for i in range(0, len(ans), w):
  print(ans[i:i+w])

