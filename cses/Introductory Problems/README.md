# CSES

# Introductory Problems

## Weird Algorithm

![](https://img.shields.io/badge/Time%20limit-1.00s-blue)
![](https://img.shields.io/badge/Memory%20limit-512MB-orange)

code: [python](./0-weird-algorithm.py)

Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:

    3 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Your task is to simulate the execution of the algorithm for a given value of n.

**Input**: The only input line contains an integer n.

**Output**: Print a line that contains all values of n during the algorithm.

**Constraints**: $`1 \le n \le 10^6`$

**Example**
```
Input:
3

Output:
3 10 5 16 8 4 2 1
```

**Response**
```
❯ time python3 0-weird-algorithm.py 3
10 5 16 8 4 2 1
python3 0-weird-algorithm.py 3  0.02s user 0.01s system 66% cpu 0.053 total
```