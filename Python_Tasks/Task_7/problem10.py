# Problem: CamelCase
# HackerRank: https://www.hackerrank.com/challenges/camelcase/problem

if __name__ == '__main__':
    s=input().strip()
    if not s:
        print(0)
    else:
        words=1
        for char in s:
            if char.isupper():
                words+=1
        print(words)
