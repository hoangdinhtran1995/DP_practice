""""
Given an array of positive integers. The task is to find the size of the
smallest subset such that the Bitwise OR of that set is Maximum possible.
"""
from canSum import canSum_tab as canSum
from howSum import howSum_tab as howSum
from bestSum import bestSum_tab as bestSum
from fib import fib
from gridtrav import gridtraveler
from canConstruct import canConstruct_tab as canConstruct
from countConstruct import countConstruct
from allConstruct import allConstruct
from smallest_subset_bitwise_or import smallest_subset
from list_xorer import list_xorer
from numwaystodecode import num_ways
from closestSum import closestSum
from firstRecChar import first_rec_char
from waysToStep import ways_to_step
from phonenr_wordsearch import phonenr_wordsearch


if __name__ == '__main__':
    print(phonenr_wordsearch("3662277", ["foo","bar","baz","foobar","emo","cap","car","cat"]))