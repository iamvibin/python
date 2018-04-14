import re
hand = open('C:/Users/VIBIN/Desktop/pYmC3/regex_sum_82466.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)',line)
    numlist.extend(stuff)
j=0
for i in numlist:
    j = j + int(i)

print(j)
