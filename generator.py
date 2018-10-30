import sys
import random

MIN_NUM_CHARACTERS = 5
MAX_NUM_CHARACTERS = 20
MIN_NUM_LINES = 10
MAX_NUM_LINES = 40

num_lines = 10
if len(sys.argv) > 1:
  num_lines = int(sys.argv[2])
else:
  num_lines = random.randint(MIN_NUM_LINES, MAX_NUM_LINES)


for i in range(num_lines):
  num_chars = random.randint(MIN_NUM_CHARACTERS, MAX_NUM_CHARACTERS)
  strbuffer = []
  for j in range(num_chars):
    strbuffer.append(str(random.randint(0,1)))
  print ''.join(strbuffer)

