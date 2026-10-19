# Problem: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem


if __name__ == '__main__':
    s=input()
    n=int(input())
    weights=set()
    previous=''
    current_weight=0
    for char in s:
        weight=ord(char)-ord('a')+1
        if char==previous:
            current_weight+=weight
        else:
            current_weight=weight
        weights.add(current_weight)
        previous=char
    for _ in range(n):
        value=int(input())
        if value in weights:
            print("Yes")
        else:
            print("No")
