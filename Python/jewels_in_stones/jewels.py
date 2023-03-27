def numJewelsInStones(jewels: str, stones: str) -> int:
    count = 0
    iterator = iter(stones)
    while True:
        try:
            stone = next(iterator)
            if stone in jewels:
                count += 1
        except StopIteration:
            break
    return count


def main():
    jewels = "aA"
    stones = "aAAbcd"
    count = numJewelsInStones(jewels, stones)
    print(count)


if __name__ == '__main__':
    main()
