import random
import math

def cumulative_distribution(histogram):
    """compute the cumulative distribution function given pdf"""
    cumulative = []
    sum = 0
    for key, value in histogram.items():
        # print("key, value:", key, value)
        sum += value
        cumulative.append((key, sum))
    print(cumulative)
    return cumulative

def binary_search(cumulative, target):
    """search through the list to find the target.
    If the target is not found, returns the next index.
    """
    left = 0
    right = len(cumulative) - 1
    while left < right:
        middle = int(math.floor((left + right) / 2))
        if cumulative[middle][1] == target:
            return middle
        elif cumulative[middle][1] < target:
            left = middle + 1
        elif cumulative[middle][1] > target:
            right = middle - 1
    return left if target <= cumulative[left][1] else left + 1

def sample(cumulative):
    """Generate sample from distribution"""
    totals = cumulative[-1][1]
    random_int = random.randint(1, totals)

    return cumulative[binary_search(cumulative, random_int)][0]
