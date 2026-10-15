
# Problem: Mutations
# HackerRank: https://www.hackerrank.com/challenges/python-mutations/problem



def mutate_string(string, position, character):
    res=string[:position]+character+string[position+1:]
    return res
