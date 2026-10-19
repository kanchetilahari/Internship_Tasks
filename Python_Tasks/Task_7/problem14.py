
# Problem: Anagram
# HackerRank: https://www.hackerrank.com/challenges/anagram/problem


if __name__ == '__main__':
    q=int(input())
    for _ in range(q):
        s=input()
        n=len(s)
        if n%2!=0:
            print(-1)
        else:
            first=s[:n//2]
            second=s[n//2:]
            changes=0
            for char in first:
                if char in second:
                    second=second.replace(char,'',1)
                else:
                    changes+=1
            print(changes)
