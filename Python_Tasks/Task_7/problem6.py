# Problem: Pangrams
# HackerRank: https://www.hackerrank.com/challenges/pangrams/problem

import string
if __name__ == '__main__':
    s=input().lower()
    letters=set(s)
    if set(string.ascii_lowercase).issubset(letters):
        print("pangram")
    else:
        print("not pangram")
