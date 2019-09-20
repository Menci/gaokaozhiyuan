from PIL import Image
# import numpy as np

from os import listdir
from os.path import isfile, join

di = [1, -1, 0, 1, -1, 0, 1, -1]
dj = [0, 0, 1, 1, 1, -1, -1, -1]

def check_color(color, limit=230):
  if color[3] == 0:
    return False
  if color[0] > limit and color[1] > limit and color[2] > limit:
    return True
  return False

path = '../ui/public/images/badges_origin'
out_path = '../ui/public/images/badges'
files = [f for f in listdir(path) if isfile(join(path, f))]

index = 0
for file in files:
  index += 1
  print('(%d/%d) %s' % (index, len(files), file))

  img = Image.open(join(path, file)).convert('RGBA')
  data = img.load()
  n, m = img.size

  # visited = np.zeros(img.size)
  q = []
  inits = [(0, 0), (n - 1, 0), (n - 1, m - 1), (0, m - 1)]
  for init in inits:
    if check_color(data[init]):
      data[init] = (255, 255, 255, 0)
      q.append(init)

  cnt = 0
  while len(q):
    p = q.pop(0)
    for i in range(len(di)):
      ne = (p[0] + di[i], p[1] + dj[i])
      if ne[0] >= 0 and ne[1] >= 0 and ne[0] < n and ne[1] < m:
        if check_color(data[ne]):
          data[ne] = (255, 255, 255, 0)
          q.append(ne)
  img.save(join(out_path, file), "PNG")
