# Problem: Mars Exploration
# HackerRank: https://www.hackerrank.com/challenges/mars-exploration/problem

if __name__ == '__main__':
    s=input()
    expected="SOS"*(len(s)//3)
    changes=0
    for i in range(len(s)):
        if s[i]!=expected[i]:
            changes+=1
    print(changes)
