
def main():
    K, S = map(int, input().split())
    K += 1

    count = 0

    for X in range(K):
        for Y in range(K):
            if X+Y > S:
                continue
            for Z in range(K):
                if X + Y + Z == S:
                    count += 1
                continue

    print(count)


main()
