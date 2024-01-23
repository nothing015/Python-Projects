'''

You are given an array (which will have a length of at least 3, but could be very large)
containing integers. The array is either entirely comprised of odd integers or entirely
comprised of even integers except for a single integer N. Write a method that takes
the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''

#Nuaiman's Solution
def find_outlier(integers):
    Ecount = 0
    Odd = 0
    for n in range(len(integers)):
        if integers[n] % 2 == 0:
            Even = integers[n]
            Ecount += 1
        elif integers[n] % 2 != 0:
            Odd = integers[n]
    if Ecount == 1:
        return Even
    else:
        return Odd

#Solution 2
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

#Solution 3
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

