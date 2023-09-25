n = int(input())

print('+ ', end='')
for a in range(n-2):
    print('- ', end='')
print('+')

for b in range(n-2):
    print('| ', end='')
    for c in range(n-2):
        print('- ', end='')
    print('|')

print('+ ', end='')
for a in range(n-2):
    print('- ', end='')
print('+')