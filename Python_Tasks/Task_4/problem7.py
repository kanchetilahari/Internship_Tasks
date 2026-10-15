# Problem: String Split and Join
# HackerRank: https://www.hackerrank.com/challenges/python-string-split-and-join/problem


def split_and_join(line):
  words=line.split()
  res="-".join(words)
  return res
