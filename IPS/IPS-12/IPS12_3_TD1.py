s = input()
freq = {}
for i in s:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1
result =max(freq, key = freq.get)
result = result + ' ' + str(freq[result])

print('Most frequent character: ' , result)