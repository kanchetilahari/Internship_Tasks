
# Problem: Game of Thrones - I
# HackerRank: https://www.hackerrank.com/challenges/game-of-thrones/problem


if __name__ == '__main__':
    s=input()
    odd=0
    for char in set(s):
        if s.count(char)%2!=0:
            odd+=1
    if odd<=1:
        print("YES")
    else:
        print("NO")
