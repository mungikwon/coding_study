cache = {}


def play(n):
    global cache

    print(cache)
    
    if n in cache:
        return cache[n]

    if n < 10:
        if (n == 3) or (n == 6) or (n == 9):
            return 1
        else:
            return 0

    i = (n // 10)
    j = (n % 10)
    cache[n] = (play(i) + play(j))
    return cache[n]


n = int(input())
count = 0
for i in range(1, n + 1):
    print(i)
    count += play(i)
print(count)