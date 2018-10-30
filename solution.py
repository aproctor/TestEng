import sys

if len(sys.argv) < 2:
  print "You must supply a file name:  pythone solution.py <filename>"
  sys.exit()

source_file = open(sys.argv[1],"r")

dictionary = {}
for line in source_file:
  num = int(line)
  val = dictionary[num] if num in dictionary else 0
  dictionary[num] = val + 1

smallest_key = 0
smallest_count = 99999999999
for key, value in dictionary.items():
  print key, ": ", value
  if ((value == smallest_count and key < smallest_key) or value < smallest_count):
    smallest_key = key
    smallest_count = value

print smallest_key, " ", smallest_count
