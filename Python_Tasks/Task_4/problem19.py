
# Problem: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem


X=int(input())
shoe_sizes=list(map(int,input().split()))
inventory={}
for size in shoe_sizes:
    if size in inventory:
        inventory[size]+=1
    else:
        inventory[size]=1
N=int(input())
total=0
for _ in range(N):
    size,price=map(int,input().split())
    if size in inventory and inventory[size]>0:
        total+=price
        inventory[size]-=1
print(total)
