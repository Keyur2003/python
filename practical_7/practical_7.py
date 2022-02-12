#ID: 20CE122
#NAME: KEYUR SANGHANI
Test_case = int(input())
for i in range(Test_case):
    num = input()
    ln = len(num)
    if ln % 2 == 0:
        p, q = num[:ln//2], num[ln//2:]
    else:
        p, q = num[:ln//2], num[ln//2+1:]
    if sorted(p) == sorted(q):
        print("YES")
    else:
        print("NO")
    