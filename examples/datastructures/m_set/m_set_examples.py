#!/usr/bin/env python3

def modify_set(someset):
    someset.add("C")
    someset.discard("A")

myset = set()
myset.add("A")
myset.add("B")
modify_set(myset)
print(myset)
