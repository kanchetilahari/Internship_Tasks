
# Problem: Super Reduced String
# HackerRank: https://www.hackerrank.com/challenges/reduced-string/problem

if __name__ == '__main__':
    s=input()
    result=[]
    for char in s:
        if len(result)>0 and result[-1]==char:
            result.pop()
        else:
            result.append(char)
    answer=''.join(result)
    if answer=='':
        print("Empty String")
    else:
        print(answer)
