# Problem: Piling Up!
# HackerRank: https://www.hackerrank.com/challenges/piling-up/problem


if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        n=int(input())
        cubes=list(map(int,input().split()))
        l=0
        r=n-1
        last_cube=float('inf')
        possible=True
        while l<=r:
            if cubes[l]>=cubes[r]:
                current=cubes[l]
                l+=1
            else:
                current=cubes[r]
                r-=1
            if current>last_cube:
                possible=False
                break
            last_cube=current
        if possible:
            print("Yes")
        else:
            print("No")
