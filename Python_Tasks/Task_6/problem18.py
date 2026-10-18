# Problem: Set Mutations
# HackerRank: https://www.hackerrank.com/challenges/py-set-mutations/problem
if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        operation, size = input().split()
        other = set(map(int, input().split()))
        if operation == 'intersection_update':
            a.intersection_update(other)
        elif operation == 'update':
            a.update(other)
        elif operation == 'symmetric_difference_update':
            a.symmetric_difference_update(other)
        elif operation == 'difference_update':
            a.difference_update(other)
    print(sum(a))
