#ID: 20CE122
#NAME: KEYUR SANGHANI
import collections

num=int(input())
dl=collections.OrderedDict()

for i in range(num):
    word = input()
    if word in dl:
        dl[word] +=1
    else:
        dl[word]=1

print(len(dl))

for a,b in dl.items():
    print(b,end=" ")
print(" \n ID: 20CE122 \n NAME: KEYUR SANGHANI ")