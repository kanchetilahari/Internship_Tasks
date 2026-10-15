# Problem: Introduction to Sets
# HackerRank: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem



def average(array):
    uniq_heights=set(array)
    res=sum(uniq_heights)/len(uniq_heights)
    return res
