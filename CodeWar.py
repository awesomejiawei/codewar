#1
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)


#2
# Your task is to check wheter a given integer is a perfect power. If it is a perfect power,
# return a pair m and k with mk = n as a proof. Otherwise return Nothing, Nil, null, NULL, None or your language's equivalent.
#
# Note: For a perfect power, there might be several pairs. For example 81 = 3^4 = 9^2, so (3,4) and (9,2) ar
# e valid solutions. However, the tests take care of this, so if a number is a perfect power, return any pair that proves it.
# isPP(4) => [2,2]
# isPP(9) => [3,2]
# isPP(5) => None

from math import log, sqrt

def isPP(n):
    for b in range(2, int(sqrt(n)) + 1):
        e = int(round(log(n, b)))
        if b ** e == n:
            return [b, e]
    return None


# 3
# ##Lyrics... Pyramids are amazing! Both in architectural and mathematical sense.
# If you have a computer, you can mess with pyramids even if you are not in Egypt
# at the time. For example, let's consider the following problem. Imagine that you have a plane
# pyramid built of numbers, like this one here:
#
#    /3/
#   \7\ 4
#  2 \4\ 6
# 8 5 \9\ 3

def longest_slide_down(pyramid):
    i = -2
    curlayer = pyramid[i]
    lastlayer = pyramid[-1]
    #print(curlayer)
    #print(lastlayer)
    while abs(i) != len(pyramid):
        tmp = []
        for idx in range(len(curlayer)):
            tmp.append(max(curlayer[idx] + lastlayer[idx], curlayer[idx] + lastlayer[idx + 1]))
        lastlayer = tmp[:]
        print(tmp)
        i = i - 1
        curlayer = pyramid[i]
    return pyramid[0][0] + max(lastlayer)

# Master's approach
def longest_slide_down2(p):
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1])  for i in range(len(tmp))]
    return res.pop()
# print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))




# Description:
# The rgb() method is incomplete. Complete the method so that passing in RGB decimal values
# will result in a hexadecimal representation being returned. The valid decimal values
# for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.
#
# The following are examples of expected output values:
# gb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

# print(rgb(255,21,23))





# What is an anagram? Well, two words are anagrams of each other
# if they both contain the same letters. For example:
# 'abba' & 'baab' == true
#
# 'abba' & 'bbaa' == true
#
# 'abba' & 'abbba' == false
#
# 'abba' & 'abca' == false
from collections import Counter
def anagrams(word, words):
    target = Counter(word)
    result = []
    for oneword in words:
        if target == Counter(oneword):
            result.append(oneword)
    return result


# Mater Version
def anagrams2(word, words): return [item for item in words if sorted(item)==sorted(word)]