F = open('input1.txt', encoding="utf8")
S = F.read()
S = list(map(str, S.split('\n')))
C = []
L = []
for i in range(len(S)):
    S[i] = S[i].split(':')
for i in range(len(S)):
    C.append(S[i][0])
for i in range(len(S)):
    L.append(S[i][1])
D = dict(zip(C, L))
INP = []
for i in range(int(input())):
    INP.append(input())
for lan in INP:
    for i in D:
        if D[i].find(lan) != -1:
            print(i, end = ' ')
    print()