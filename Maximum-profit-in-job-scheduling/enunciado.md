# [**1235. Maximum Profit in Job Scheduling**](https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/)

## Problem Statement

We have `n` jobs, where each job is scheduled to be done from `startTime[i]` to `endTime[i]`, obtaining a profit of `profit[i]`.

You're given the arrays `startTime`, `endTime`, and `profit`. Return the **maximum profit** you can take such that there are no two jobs in the subset with overlapping time ranges.

If you choose a job that ends at time `X`, you will be able to start another job that starts at time `X`.

---

## Examples

### Example 1:

Input:

```plaintext
startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]
```