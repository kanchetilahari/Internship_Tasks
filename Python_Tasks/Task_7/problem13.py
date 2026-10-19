# Problem: Sherlock and the Valid String
# HackerRank: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter
def is_valid(s):
    counts=list(Counter(s).values())
    frequencies=Counter(counts)
    if len(frequencies)==1:
        return "YES"
    if len(frequencies)!=2:
        return "NO"
    (count1,freq1),(count2,freq2)=frequencies.items()
    if (count1==1 and freq1==1) or (count2==1 and freq2==1):
        return "YES"
    if abs(count1-count2)==1:
        if (count1>count2 and freq1==1) or (
            count2>count1 and freq2==1
        ):
            return "YES"
    return "NO"
if __name__ == '__main__':
    s = input().strip()
    print(is_valid(s))
