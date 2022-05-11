import collections


a=[9,9,4,4,4,4,4,5,9,10,10]

count=collections.Counter(a)
print(count)
# freqCount=defaultdict(int)
print(sorted(a, key=lambda x: (count[x])))
# for e in a:
#     freqCount[e] += 1
# sorted(freqCount.items(), key=lambda kv: kv[1])
# for k,v in freqCount.items():
#     print(k,v)
