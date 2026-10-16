# Problem: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem


from collections import Counter
if __name__ == '__main__':
    X=int(input())
    shoe_sizes=list(map(int,input().split()))
    shoe_inventory=Counter(shoe_sizes)
    N = int(input())
    total_earnings=0
    for _ in range(N):
        size,price=map(int,input().split())
        if shoe_inventory[size]>0:
            total_earnings+=price
            shoe_inventory[size]-=1
    print(total_earnings)
