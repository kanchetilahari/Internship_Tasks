# Problem: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

if __name__ == '__main__':
    q=int(input())
    for _ in range(q):
        s=input()
        found=False
        for i in range(1,len(s)//2+1):
            first=s[:i]
            if first.startswith('0'):
                continue
            number=int(first)
            result=first
            while len(result)<len(s):
                number+=1
                result+=str(number)
            if result==s:
                print("YES",first)
                found=True
                break
        if not found:
            print("NO")
