import sys

if len(sys.argv) < 2:
  print "You must supply a file name:  pythone solution.py <filename>"
  sys.exit()

source_file = open(sys.argv[1],"r")

checksum = 0
for line in source_file:
    for char in line:
      if char == '1':
        checksum += 1

print checksum
