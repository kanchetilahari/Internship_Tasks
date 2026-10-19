
# Problem: Gemstones
# HackerRank: https://www.hackerrank.com/challenges/gem-stones/problem



if __name__ == '__main__':
    n=int(input())
    common=set(input().strip())
    for _ in range(n-1):
        rocks=set(input().strip())
        common=common.intersection(rocks)
    print(len(common))
