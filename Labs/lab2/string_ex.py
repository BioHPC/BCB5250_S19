st = 'ACGT‘
len(st) # getting the length of a string
import random 
random.choice('ACGT') # generating a random nucleotide
# now I'll make a random nucleotide string by concatenating random nucleotides 
st = ''.join([random.choice('ACGT') for _ in xrange(40)]) 
st
st[1:3] # substring, starting at position 1 and extending up to but not including position 3 
note that the first position is numbered 0
st[0:3] # prefix of length 3
st[:3] # another way of getting the prefix of length 3
st[len(st)-3:len(st)] # suffix of length 3
st[-3:] # another way of getting the suffix of length 3
st1, st2 = 'CAT', 'ATAC‘
st1 + st2 # concatenation of 2 strings
