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



# 4
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




# 5
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




# 6
# Description:
# You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:
#
# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# If no bigger number can be composed using those digits, return -1:
#
# 9 ==> -1
# 111 ==> -1
# 531 ==> -1

# 思路
# 我觉得对任何 kata 题目而言，最重要的不是用什么技巧写代码，而是如何发现问题中的规律。这个问题也是如此。想知道如何解题，我们先想想 数字是怎么比大小 的。
#
# 数字比大小的规则很简单，大概描述起来如下：
#
# 先比较位数，位数高的更大。
#
# 如果位数相同，则从第一位数字开始比较，数字更大的取胜。如果第一位数字相等，则比较第二位数字，以此类推直到末位数。
#
# 对这个题目而言，构造出来的新数字位数跟原数字是一样的，所以只用考虑上面的第二条规则。加上题目的描述，我们就可以分析出 下一个更大数字 到底是什么意思：尽量只调整末位 x 位数获得满意的结果，并且 x 尽可能小。换句话说，能动最后两位数字的就别动最后三位。
#
# 那么怎么知道最少动最后几位数字能满足要求呢？这就得进一步分析下规律了。让我们回顾两个例子：
#
# nextBigger(513) == 531
# nextBigger(531) == -1
# nextBigger(2531) == 3125
# 第一个例子里，我们把 13 换成了 31 ，5 根本没必要动。第二个例子里完全没有可换的。第三个例子最有趣，我们把首位换成了 3 ，然后把其次三位数全部重排了，重排规律是从小到大，这样才能保证新数字是 "下一个更大" 的 。
#
# 规律得自己琢磨。我就说说结论。对于 xyz 这种数字，先分析一下最后两位 yz ，如果 y < z ，就只用换最后两位。如果 y >= z ，说明换两位不可行，所以只能考虑最后三位 xyz 。这时候如果 x >= max(y, z) ，则三位也不能换，以此类推。如果 x < any(y, z) ，则可以把 y 和 z 中比 x 大的最小的数拿出来，跟 x 互换位置，剩下的数按顺序排列，就组成下一个更大的数字了。
#
# 解法
# 按照上面的思路，我们可以梳理一下解法：
#
# 取出最后两位数字，判断它能否达到要求（通过不同组合生成更大的数字）。如果无法生成更大的数字，换三位试试，以此类推，如果扫描到首位还没有结果，返回 -1 。
#
# 如果找到了符合要求的后 x 位数字，则把整个数字单独分割开来，前面的称为 left ，后面 x 位称为 right 。
#
# 对 right 重排，形成下一个更大的数字。重排规则如下：
#
# 对 right 而言，找到比 right[0] 的下一个更大数字，把它作为新的 right[0] 。
#
# 剩下的数字升序排列，然后跟新的 right[0] 组合。
#
# 组合 left 和 right 形成新的数字，这就是完整的 "下一个更大的数字" 。


def next_bigger(n):
    s = list(str(n))
    print(s)
    for i in range(len(s)-2,-1,-1):
        print(i)
        if s[i] < s[i+1]:
            t = s[i:]
            #print(t)
            m = min(filter(lambda x: x>t[0], t))
            #print(m)
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1


#print(next_bigger(2514))


# 7
# Description:
# How many ways can you make the sum of a number?
# From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#
#
# In number theory and combinatorics, a partition of a positive integer n,
# also called an integer partition, is a way of writing n as a sum of positive integers.
# Two sums that differ only in the order of their summands are considered the same partition.
# If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:
def exp_sum(n):
  if n < 0:
    return 0
  dp = [1]+[0]*n
  print(dp)
  for num in range(1,n+1):
    print('*'*20)
    for i in range(num,n+1):
      dp[i] += dp[i-num]
      print(dp)
  return dp[-1]


def twoSum(nums,target):
    first = 0
    last = -1
    nums.sort()
    #print(nums[-1])
    #print(nums[0])
    while nums[first] + nums[last] != target:
        print(first,last)
        if nums[first] + nums[last] > target:
            last = last - 1
        else:
            first = first + 1
    return [first, last]

# print(twoSum([150,24,79,50,88,345,3],200))



# 8
# He noted the PIN 1357, but he also said, it is possible that each of the
# digits he saw could actually be another adjacent digit (horizontally or vertically,
#                                                         but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.
#
# He also mentioned, he knows this kind of locks. You can enter an unlimited
# amount of wrong PINs, they never finally lock the system or sound the alarm.
# That's why we can try out all possible (*) variations.
#
# * possible in sense of: the observed PIN itself and all variations considering the adjacent digits
#
# Can you help us to find all those variations? It would be nice to have a function,
# that returns an array (or a list in Java and C#) of
# # all variations for an observed PIN with a length of 1 to 8 digits.
# # We could name the function getPINs (get_pins in python, GetPINs in C#).
# # But please note that all PINs, the observed one and also the results, must be strings,
# # because of potentially leading '0's. We already prepared some test cases for you.
# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
import itertools
def get_pins(observed):
    dict_n = {"1": [1, 2, 4],
              "2": [1, 2, 3, 5],
              "3": [2, 3, 6],
              "4": [1, 4, 5, 7],
              "5": [2, 4, 5, 6, 8],
              "6": [3, 5, 6, 9],
              "7": [4, 7, 8],
              "8": [5, 7, 8, 9, 0],
              "9": [6, 8, 9],
              "0": [8, 0]}  # 建立对应关系的字典
    num = []
    r_num = []
    for i in observed:
        num.append(dict_n[i])  # 根据键找值,存入num列表
    #print(num)
    result_num = list(itertools.product(*num))  # 生成全排列元组,存入列表
    print(result_num)
    for n in result_num:
        for m in n:
            r_num.append(str(m))
    r_num = "".join(r_num)  # 拼接在一起
    print(r_num)
    result = [r_num[i:i+len(observed)] for i in range(0, len(r_num), len(observed))]  # 按固定长度输出
    return result

#print(get_pins('11'))


#9
# Description:
# Create a function named divisors/Divisors that takes an integer
# n > 1 and returns an array with all of the integer's divisors(except for 1 and ' \
#         'the number itself), from smallest to largest. If the number is prime return ' \
#         'the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
#
# Example:
# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"

def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l

#10
# The goal of this exercise is to convert a string to a new string where each
# character in the new string is "(" if that character appears only once in the
# original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
#
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("


from collections import Counter
def duplicate_encode(word):
    word = word.lower()
    wd = Counter(word)
    result = []
    for letter in word:
        if wd[letter] > 1:
            result.append(')')
        else:
            result.append('(')
    return ''.join(result)

#mater
def duplicate_encode2(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])