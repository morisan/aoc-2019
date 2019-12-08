line = open('8.txt').readline().strip()

w = 25
h = 6
num_pixels = w * h

ans = None
least_zeros = None

for i in range(0, len(line), num_pixels):
  img_data = line[i:i+num_pixels]
  num_zeros = img_data.count('0')
  if least_zeros is None or num_zeros < least_zeros:
    least_zeros = num_zeros
    ans = img_data.count('1') * img_data.count('2')

print(ans)
