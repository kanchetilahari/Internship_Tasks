
# Problem: Making Anagrams
# HackerRank: https://www.hackerrank.com/challenges/making-anagrams/problem


if __name__ == '__main__':
    s1=input().strip()
    s2=input().strip()
    count={}
    for char in s1:
        count[char]=count.get(char,0)+1
    for char in s2:
        count[char]=count.get(char,0)-1
    deletions=0
    for value in count.values():
        deletions+=abs(value)
    print(deletions)
