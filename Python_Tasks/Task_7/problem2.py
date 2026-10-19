
# Problem: The Captain's Room
# HackerRank: https://www.hackerrank.com/challenges/py-the-captains-room/problem

if __name__ == '__main__':
    k=int(input())
    rooms=list(map(int,input().split()))
    room_counts={}
    for room in rooms:
        room_counts[room]=room_counts.get(room,0)+1
    for room, c in room_counts.items():
        if c==1:
            print(room)
            break
