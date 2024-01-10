words = input()

ans = []
for i in range(len(words)):
    ans.append(words[i::])

ans.sort()

for i in ans:
    print(i)