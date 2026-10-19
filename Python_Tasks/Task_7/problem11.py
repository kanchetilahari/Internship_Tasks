# Problem: Two Strings
# HackerRank: https://www.hackerrank.com/challenges/two-strings/problem

def two_strings(s1,s2):
    if set(s1).intersection(set(s2)):
        return "YES"
    return "NO"
if __name__ == '__main__':
    p=int(input())
    for _ in range(p):
        s1=input().strip()
        s2=input().strip()
        print(two_strings(s1,s2))
