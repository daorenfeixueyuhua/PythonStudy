def kmp(pattern, text):
    n = len(pattern)
    next = [0] * (n+1)
    for i in range(1, n):
        j = i
        while j > 0:
            j = next[j]
            if pattern[j] == pattern[i]:
                next[i+1] = j
                break

    positions = []
    m = len(text)
    j = 0
    for i in range(m):
        if i < n and text[i] == pattern[j]:
            j += 1
        else:
            while j > 0:
                j = next[j]
                if text[i] == pattern[j]:
                    j += 1
                    break

        if j == n:
            positions.append(i - n + 1)
    return positions


if __name__ == '__main__':
    print(kmp("ara", "character"))
