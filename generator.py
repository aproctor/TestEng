import sys
import random

MIN_NUMBER = 0
MAX_NUMBER = 10
MIN_NUM_LINES = 100
MAX_NUM_LINES = 400

num_lines = 10
if len(sys.argv) > 1:
  num_lines = int(sys.argv[2])
else:
  num_lines = random.randint(MIN_NUM_LINES, MAX_NUM_LINES)


for i in range(num_lines):
  print random.randint(MIN_NUMBER, MAX_NUMBER)

