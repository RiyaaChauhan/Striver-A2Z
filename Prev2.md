## Table of Contents

1. [Basic Maths](#basic-maths)
2. [Recursion](#recursion)
3. [Two Pointers](#two-pointers)
4. [Sorting](#sorting)
5. [Algorithms and Techniques](#algorithms-and-techniques)
6. [Hashing](#hashing)
7. [Binary Search](#binary-search)
8. [Arrays](#arrays)
9. [Strings](#strings)
10. [Linked List](#linked-list)
11. [Bit Manipulation](#bit-manipulation)
12. [Stack](#stack)
13. [Sliding Window and Two Pointer Combined](#sliding-window-and-two-pointer-combined)

---

## Basic Maths

| **#** | **Problem Name** | **Platform** | **Status** | **File** | **Difficulty** | **Prerequisites** |
| ----- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------- |
| 1  | Number of factors | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/number-of-factors1435/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card) | ❌ | [code.py]() | 🟢 | Loops, Divisors, Square roots |
| 2  | Perfect Number | [LeetCode](https://leetcode.com/problems/perfect-number/) | ❌ | [code.py]() | 🟢 | Divisors, Sum of factors, Loops |
| 3  | Three Divisors | [LeetCode](https://leetcode.com/problems/three-divisors/description/) | ❌ | [code.py]() | 🟢 | Prime numbers, Perfect squares, Divisors |
| 4  | Four Divisors | [LeetCode](https://leetcode.com/problems/four-divisors/description/) | ❌ | [code.py]() | 🟡 | Divisors, Efficient looping techniques, Sum of numbers |
| 5  | Armstrong Number | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1) | ❌ | [code.py]() | 🟢 | Number manipulation, Digit extraction, Loops |
| 6  | Palindrome Number | [LeetCode](https://leetcode.com/problems/palindrome-number/description/) | ❌ | [code.py]() | 🟢 | Loops, Conditionals, Integer Operations (% And /), Overflow Handling |
| 7  | Valid Palindrome | [LeetCode](https://leetcode.com/problems/valid-palindrome/description/) | ❌ | [code.py]() | 🟢 | String Manipulation, Two-Pointer Technique, Isalnum, Tolower |
| 8  | Prime Number | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/prime-number2314/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card) | ❌ | [code.py]() | 🟢 | Mathematics, Prime Number Logic, Square Root Optimization |
| 9  | Count Primes | [LeetCode](https://leetcode.com/problems/count-primes/description/) | ❌ | [code.py]() | 🟡 | Sieve Of Eratosthenes, Boolean Arrays, Loops |
| 10 | Count Digits | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/count-digits5716/0) | ❌ | [code.py]() | 🟢 | Modulo, Digit Extraction, Loops |
| 11 | Count the Digits That Divide a Number | [LeetCode](https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/) | ❌ | [code.py]() | 🟢 | Modulo, Digit Extraction, Loops |
| 12 | GCD of two number | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card) | ❌ | [code.py]() | 🟢 | Euclidean Algorithm, Basic Math (division and modulus), Iterative Loops |
| 13 | LCM and GCD | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card) | ❌ | [code.py]() | 🟢 | Euclidean Algorithm, Relation Between LCM and GCD, Basic Math (multiplication, division) |
| 14 | Find Greatest Common Divisor of Array | [LeetCode](https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/) | ❌ | [code.py]() | 🟢 | Array Traversal, Euclidean Algorithm, Basic Math (min, max, division, modulus) |
| 15 | Reverse Integer | [LeetCode](https://leetcode.com/problems/reverse-integer/) | ❌ | [code.py]() | 🟡 | Modulus for Digit Extraction, Handling Integer Overflow, Iterative Loops |

---

## Recursion

| **#** | **Problem Name** | **Platform** | **Status** | **File** | **Difficulty** | **Prerequisites** |
| ----- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------------------------------------------------- | -------------- | ------------------------------------------------------ |
| 1 | Print 1 To N Without Loop | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1) | ❌ | [code.py]() | 🟢 | Recursion |
| 2 | Print N to 1 without loop | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-n-to-1-without-loop) | ❌ | [code.py]() | 🟢 | Recursion |
| 3 | Print GFG n times | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/print-gfg-n-times/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-gfg-n-times) | ❌ | [code.py]() | 🟢 | Recursion |
| 4 | Sum of first n terms | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1) | ❌ | [code.py]() | 🟢 | Recursion, Arithmetic operations (like exponentiation) |
| 5 | Factorials Less than or Equal to n | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/0?problemType=functional&difficulty%255B%255D=-1&page=1&query=problemTypefunctionaldifficulty%255B%255D-1page1) | ❌ | [code.py]() | 🟢 | Recursion, Factorial calculations |
| 6 | Reverse an Array | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/reverse-an-array/0) | ❌ | [code.py]() | 🟢 | Recursion, Arrays |
| 7 | Fibonacci Number | [LeetCode](https://leetcode.com/problems/fibonacci-number/description/) | ❌ | [code.py]() | 🟢 | Recursion, Understanding of Fibonacci sequence |

---

## Two Pointers

| **#** | **Problem Name** | **Platform** | **Status** | **File** | **Difficulty** | **Prerequisites** |
| ----- | ------------------------- | -------------------------------------------------------------------------------- | ---------- | --------------------------------------------------- | -------------- | ----------------------------------------------- |
| 1 | Reverse String | [LeetCode](https://leetcode.com/problems/reverse-string/description/) | ❌ | [code.py]() | 🟢 | Two Pointers, In-Place Modification |
| 2 | Move Zeroes | [LeetCode](https://leetcode.com/problems/move-zeroes/description/) | ❌ | [code.py]() | 🟢 | Two Pointers, In-Place Modification |
| 3 | Valid Palindrome II | [LeetCode](https://leetcode.com/problems/valid-palindrome-ii/description/) | ❌ | [code.py]() | 🟢 | Two Pointers, In-Place Modification |
| 4 | Container With Most Water | [LeetCode](https://leetcode.com/problems/container-with-most-water/description/) | ❌ | [code.py]() | 🟡 | Arrays, Two-pointer technique, Greedy algorithm |
| 5 | Sort Colors | [LeetCode](https://leetcode.com/problems/sort-colors/submissions/) | ❌ | [code.py]() | 🟡 | Two Pointers, In-Place Modification |
| 6 | Trapping Rain Water | [LeetCode](https://leetcode.com/problems/trapping-rain-water/description/) | ❌ | [code.py]() | 🔴 | Arrays, Two-pointer technique, Greedy algorithm |

---

## Sorting

| **#** | **Problem Name** | **Platform** | **Status** | **File** | **Difficulty** | **Prerequisites** |
| ----- | ------------------------ | ------------------------------------------------------------------------ | ---------- | -------------------------------------------------- | -------------- | ----------------------------------------------------- |
| 1 | Bubble Sort | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/bubble-sort/1) | ❌ | [code.py]() | 🟢 | Arrays, Loops, Sorting basics |
| 2 | Insertion Sort | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/insertion-sort/1) | ❌ | [code.py]() | 🟢 | Arrays, Loops, Sorting basics |
| 3 | Merge Sort | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/merge-sort/1) | ❌ | [code.py]() | 🟡 | Arrays, Recursion, Divide and Conquer |
| 4 | Quick Sort | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/quick-sort/1) | ❌ | [code.py]() | 🔴 | Arrays, Recursion, Divide and Conquer, Sorting basics |
| 5 | Recursive Bubble Sort | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/bubble-sort/1) | ❌ | [code.py]() | 🟢 | Arrays, Recursion, Swapping |
| 6 | Recursive Insertion Sort | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/insertion-sort/1) | ❌ | [code.py]() | 🟢 | Arrays, Recursion, Insertion |
| 7 | Selection Sort | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/selection-sort/1) | ❌ | [code.py]() | 🟢 | Arrays, Recursion, Swapping |

---
## Algorithms and Techniques

| **#** | **Problem Name** | **Platform** | **Status** | **File** | **Difficulty** | **Prerequisites** |
| ----- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------- | ----------------------------------------------------------------- | -------------- | --------------------------------------------------------------------- |
| 1 | Prefix Sum | [GeeksForGeeks](https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/) |✅|[code.py](https://github.com/RiyaaChauhan/Striver-A2Z/blob/main/Day_29/prefix.md)| 🟢 | Arrays, Loops, Basic Mathematics (Addition, Subtraction) |
| 2 | Fibonacci Sequence | [LeetCode](https://leetcode.com/problems/generate-fibonacci-sequence/description/) | - | | 🟢 | Recursion, Dynamic Programming, Basic Mathematics (Sequences) |
| 3 | Boyer-Moore Voting Algorithm | [TopCoder](https://www.topcoder.com/thrive/articles/boyer-moore-majority-vote-algorithm) | - | | 🟢 | Arrays, Loops, Basic Counting Logic |
| 4 | Euclidean Algorithm | [GeeksForGeeks](https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/) | - | | 🟡 | Basic Mathematics (Division, Remainder), Recursion |
| 5 | Sieve of Eratosthenes | [CP-Algorithms](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html) | ❌ | | 🟡 | Arrays, Loops, Basic Mathematics (Prime Numbers) |
| 6 | Binomial Coefficients | [GeeksForGeeks](https://www.geeksforgeeks.org/binomial-coefficient-dp-9/) | ❌ | | 🟡 | Combinatorics, Dynamic Programming, Recursion |
| 7 | In-place Array Modification | [GeeksForGeeks](https://www.geeksforgeeks.org/in-place-algorithm/) | ❌ | | 🔴 | Arrays, Loops, Two-pointer Technique |
| 8 | Sliding Window | [GeeksForGeeks](https://www.geeksforgeeks.org/window-sliding-technique/) | ❌ |  | 🔴 | Arrays, Loops, Two-pointer Technique, Hash Maps (for some variations) |
| 9 | Floyd's Tortoise and Hare Algorithm | [DEV Community](https://dev.to/alisabaj/floyd-s-tortoise-and-hare-algorithm-finding-a-cycle-in-a-linked-list-39af) | ❌ || 🔴 | Linked Lists, Two-pointer Technique, Cyclic Detection |
| 10 | Longest Common Subsequence (LCS) | [GeeksForGeeks](https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/) | ❌ | | 🔴 | Dynamic Programming, Strings, Recursion |
---
## Hashing

| **#** | **Problem Name** | **Platform** | **Status** | **File** | **Difficulty** | **Prerequisites** |
| ----- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------ | -------------- | --------------------------------------------------------------- |
| 1 | Find unique element | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/find-unique-element2632/0) | ❌ | [code.py]() | 🟢 | Hash maps, Frequency counting, Array traversal, Modulo operator |
| 2 | Sum of Unique Elements | [LeetCode](http://leetcode.com/problems/sum-of-unique-elements/description/) | ❌ | [code.py]() | 🟢 | Hash maps, Frequency counting, Array traversal |
| 3 | Find the Frequency | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/find-the-frequency/1) | ❌ | [code.py]() | 🟢 | Hash maps, Frequency counting, Array traversal |
| 4 | Frequencies in a Limited Array | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1) | ❌ | [code.py]() | 🟢 | Hash maps, Frequency counting, Arrays, Index manipulation |
| 5 | Check if array contains duplicates | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/check-if-array-contains-duplicates/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card) | ❌ | [code.py]() | 🟢 | Hash sets, Array traversal, Unordered data structures |
| 6 | Find the Duplicate Number | [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/description/) | ❌ | [code.py]() | 🟡 | Hash maps, Frequency counting, Array traversal |
| 7 | First Unique Character in a String | [LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/description/) | ❌ | [code.py]() | 🟢 | Hash maps, String traversal, Frequency counting |
| 8 | Union of Arrays with Duplicates | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card) | ❌ | [code.py]() | 🟢 | Hash maps, Hash sets, Array traversal, Set operations |
| 9 | Intersection of Two Arrays | [LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/description/) | ❌ | [code.py]() | 🟢 | Hash sets, Array traversal, Set operations |
| 10 | Two Sum - Pair with Given Sum | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/key-pair5616/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_cardk) | ❌ | [code.py]() | 🟢 | Hash Maps, Arrays, Loops, Complement |
| 11 | Majority Element | [LeetCode](https://leetcode.com/problems/majority-element/description/) | ❌ | [code.py]() | 🟢 | Hash Maps, Arrays, Loops, Boyer-Moore Voting Algorithm |
| 12 | K-diff Pairs in an Array | [LeetCode](https://leetcode.com/problems/k-diff-pairs-in-an-array/description/) | ❌ | [code.py]() | 🟡 | Hash Maps, Arrays, Loops |
| 13 | Missing Number | [LeetCode](https://leetcode.com/problems/missing-number/description/) | ❌ | [code.py]() | 🟢 | Hash Maps, Arrays, Loops |
| 14 | First Repeating Element | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/first-repeating-element4018/1) | ❌ | [code.py]() | 🟢 | Hash Maps, Arrays, Loops |
| 15 | Valid Anagram | [LeetCode](https://leetcode.com/problems/valid-anagram/description/) | ❌ | [code.py]() | 🟢 | Hash Maps, Strings, Loops |
| 16 | Group Anagrams | [LeetCode](https://leetcode.com/problems/group-anagrams/description/) | ❌ | [code.py]() | 🟡 | Hash Maps, Strings, Sorting, Loops |
| 17 | Longest Substring Without Repeating Characters | [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/) | ❌ | [code.py]() | 🟡 | Hash Maps, Strings, Sliding Window Technique, Loops |

---

## Binary Search

| **#** | **Problem Name** | **Platform** | **Status** | **File** | **Difficulty** | **Prerequisites** |
|-| ---------------- | ----------------- | ------ | ------------- | ------- | ----------------- |
| 1 | Binary Search | [LeetCode](https://leetcode.com/problems/binary-search/description/k) | ❌ | code.py | 🟢 | Recursion, Comparisons, Finding mid |
| 2 | Floor in a Sorted Array | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1) | ❌ | code.py | 🟢 | Binary Search, Array Traversal |
| 3 | Ceil The Floor | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/ceil-the-floor2802/1) | ❌ | code.py | 🟢 | Binary Search, Array Traversal |
| 4 | Search Insert Position | [LeetCode](https://leetcode.com/problems/search-insert-position/description/) | ❌ | code.py | 🟢 | Binary Search, Array Traversal |
| 5 | Find First and Last Position of Element in Sorted Array | [LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/) | ❌ | code.py | 🟡 | Binary Search, Array Traversal |
| 6 | Number of occurrence | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1) | ❌ | code.py | 🟢 | Binary Search, Array Traversal |
| 7 | Search in Rotated Sorted Array | [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/description/) | ❌ | code.py | 🟡 | Binary Search, Rotated Sorted Array |
| 8 | Search in Rotated Sorted Array II | [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/) | ❌ | code.py | 🟡 | Binary Search, Rotated Sorted Array, Handling Duplicates |
| 9 | Find Minimum in Rotated Sorted Array | [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/) | ❌ | code.py | 🟡 | Binary Search, Rotated Sorted Array |
| 10 | Find Kth Rotation | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/rotation4723/1) | ❌ | code.py | 🟢 | Binary Search, Rotated Sorted Array |
| 11 | Single Element in a Sorted Array | [LeetCode](https://leetcode.com/problems/single-element-in-a-sorted-array/description/) | ❌ | code.py | 🟡 | Binary Search, Rotated Sorted Array |
| 12 | Find Peak Element | [LeetCode](https://leetcode.com/problems/find-peak-element/description/) | ❌ | code.py | 🟡 | Binary Search, Rotated Sorted Array |
| 13 | Square Root | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/square-root/0) | ❌ | code.py | 🟢 | Binary Search, Integer Arithmetic |
| 14 | Find nth root of m | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1) | ❌ | code.py | 🟢 | Binary Search, Exponentiation, Integer Arithmetic |
| 15 | Koko Eating Bananas | [LeetCode](https://leetcode.com/problems/koko-eating-bananas/description/) | ❌ | code.py | 🟡 | Binary Search, Feasibility Check |
| 16 | Minimum Number of Days to Make m Bouquets | [LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/) | ❌ | code.py | 🟡 | Binary Search, Feasibility Check, Array Traversal |
| 17 | Find the Smallest Divisor Given a Threshold | [LeetCode](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/) | ❌ | code.py | 🟡 | Binary Search, Feasibility Check, Division & Summation |
| 18 | Capacity To Ship Packages Within D Days | [LeetCode](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/) | ❌ | code.py | 🟡 | Binary Search, Greedy Algorithms |
| 19 | Kth Missing Positive Number | [LeetCode](https://leetcode.com/problems/kth-missing-positive-number/description/) | ❌ | code.py | 🟢 | Binary Search |
| 20 | Split Array Largest Sum | [LeetCode](https://leetcode.com/problems/split-array-largest-sum/description/) | ❌ | code.py | 🔴 | Binary Search, Greedy Algorithms |
| 21 | Median of Two Sorted Arrays | [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/description/) | ❌ | code.py | 🔴 | Binary Search, Partitioning, Median Calculation |
| 22 | K-th element of two Arrays | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1) | ❌ | code.py | 🟡 | Binary Search, Partitioning, Array Merging Concepts |
| 23 | Row with max 1s | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1) | ❌ | code.py | 🟡 | Binary Search, 2D Arrays |
| 24 | Search a 2D Matrix | [LeetCode](https://leetcode.com/problems/search-a-2d-matrix/description/) | ❌ | code.py | 🟡 | Binary Search, Matrix Traversal, Index Mapping |
| 25 | Search a 2D Matrix II | [LeetCode](https://leetcode.com/problems/search-a-2d-matrix-ii/description/) | ❌ | code.py | 🟡 | Binary Search, Matrix Traversal, 2D Search Strategy |
| 26 | Find a Peak Element II | [LeetCode](https://leetcode.com/problems/find-a-peak-element-ii/description/) | ❌ | code.py | 🟡 | Binary Search, Peak Finding Algorithm, Matrix Traversal |
| 27 | Median in a row-wise sorted Matrix | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1) | ❌ | code.py | 🔴 | Binary Search, Median Concept, Matrix Traversal |

---

## Arrays
| **#** | **Problem Name** | **Platform** | **Status** | **File** | **Difficulty** | **Prerequisites** |
| ----- | ---------------- | ----------- | ---------- | ------------------------- | -------------- | -------------------- |
| 1 | Third Maximum Number | [LeetCode](https://leetcode.com/problems/third-maximum-number/) | |[code.py]()| 🟢 | Sorting |
| 2 | Right Rotate an Array by K Steps | [LeetCode](https://leetcode.com/problems/rotate-array/) |  | [code.py]()| 🟡 | Rotations |
| 3 | Check if the Array is Sorted and Rotated | [LeetCode](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) |  |[code.py]() | 🟢 | Pointers, In-place Modification |
| 4 | Remove Duplicates from Sorted Array | [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) |  |[code.py]() | 🟢 | Array Reversal, Modulo Operation |
| 5 | Kth Largest Element in Array | [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/description/) |  |[code.py]() | 🟡 | QuickSelect Algorithm, Partitioning Recursion |
| 6 | Search in Rotated Sorted Array Places | [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/description/) |  | [code.py]() | 🟡 | Binary Search |
| 7 | Move All Zeros to the End | [LeetCode](https://leetcode.com/problems/move-zeroes/) |  | [code.py]()| 🟢 | Two Pointers, Swapping Elements |
| 8 | Find Minimum in Rotated Sorted Array | [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/) |  | [code.py]() | 🟡 | Binary Search |
| 9 | Intersection of Two Arrays | [LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/description/) | ✅| [code.py]()| 🟢 | Hashing, Sets |
| 10 | Find Missing Number in an Array | [LeetCode](https://leetcode.com/problems/missing-number/) |  | [code.py]() | 🟢 | Bit Manipulation, XOR Operations |
| 11 | Max Consecutive 1's | [LeetCode](https://leetcode.com/problems/max-consecutive-ones/) |  | [code.py]() | 🟢 | Loops (for, while) |
| 12 | Find the Single Element Among Pairs | [LeetCode](https://leetcode.com/problems/single-element-in-a-sorted-array/) |  |[code.py]() | 🟡 | Binary Search |
| 13 | Number of Subarrays with Sum Equal to K | [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/description/) |  | [code.py]() | 🟡 | Prefix Sum, Hash Maps (unordered_map) |
| 14 | Maximum Sum of Distinct Subarrays With Length K | [LeetCode](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/) |  |[code.py]()| 🟡 | Sliding Window Technique, Hash Maps (unordered_map) |
| 15 | 2-Sum Problem | [LeetCode](https://leetcode.com/problems/two-sum/) |  |[code.py]()| 🟢 | Hash Maps (unordered_map), Basic Arithmetic (complement) |
| 16 | Sort 0, 1, 2 | [LeetCode](https://leetcode.com/problems/sort-colors/) |  |[code.py]()| 🟡 | Counting, Basic Iteration |
| 17 | Majority Element II (n by 2 times) | [LeetCode](https://leetcode.com/problems/majority-element/) |  |[code.py]()| 🟢 | Hash Maps, Boyer-Moore Voting Algorithm |
| 18 | Maximum Subarray (Kadane's Algorithm) | [LeetCode](https://leetcode.com/problems/maximum-subarray/) |  |[code.py]()| 🟡 | Kadane's Algorithm |
| 19 | Subarray with Sum K | [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/) |  | [code.py]() | 🟡 | Prefix Sum, Hash Maps, Sliding Window Technique |
| 20 | Stock Buy and Sell | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |  |[code.py]()| 🟢 | Min/Max Element Tracking |
| 21 | Rearrange Elements by Sign | [LeetCode](https://leetcode.com/problems/rearrange-array-elements-by-sign/) |  |[code.py]()| 🟡 | Iteration, Conditional Statements |
| 22 | Next Permutation | [LeetCode](https://leetcode.com/problems/next-permutation/) |  |[code.py]() | 🟡 | Sorting, Swapping Elements, Reverse, Linear Search |
| 23 | Replace Elements with Greatest Element on Right Side | [LeetCode](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) |  |[code.py]() | 🟢 | Max Function, Reverse Traversal |
| 24 | Longest Consecutive Subsequence | [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/) |  |[code.py]()| 🟡 | Sorting, Linear Search, Sequence Detection |
| 25 | Set Matrix 0's | [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/) |  | [code.py]()| 🟡 | 2D Arrays, Matrix Manipulation, Flags, Traversal |
| 26 | Rotate Matrix | [LeetCode](https://leetcode.com/problems/rotate-image/) |  |[code.py]()| 🟡 | 2D Arrays, Transpose of Matrix, Swapping, Array Reversal |
| 27 | Spiral Traversal | [LeetCode](https://leetcode.com/problems/spiral-matrix/) |  |[code.py]() | 🟡 | Loop Control, Directional Changes |
| 28 | Pascal's Triangle | [LeetCode](https://leetcode.com/problems/pascals-triangle/) |  |[code.py]()| 🟢 | Nested Loops, Binomial coefficients |
| 29 | Majority Element II (n by 3 times) | [LeetCode](https://leetcode.com/problems/majority-element-ii/) |  || 🟡 | Traversal, Counting, Boyer-Moore Voting Algorithm |
| 30 | 3-Sum Problem | [LeetCode](https://leetcode.com/problems/3sum/) |  |[code.py]() | 🟡 | Sorting, Two-pointer technique, Handling duplicates |
| 31 | 4-Sum Problem | [LeetCode](https://leetcode.com/problems/4sum/) |  | [code.py]() | 🟡 | Sorting, Nested loops, Two-pointer technique, Handling duplicates, Overflow prevention |
| 32 | Length of Subarray with an equal number of 0 and 1 | [LeetCode](https://leetcode.com/problems/contiguous-array/description/) |  |[code.py]() | 🟡 | Prefix sum, Hash maps, Subarray with a target sum |
| 33 | XOR Queries of a Subarray | [LeetCode](https://leetcode.com/problems/xor-queries-of-a-subarray/description/) |  |[code.py]() | 🟡 | XOR operation properties, Prefix XOR array, Range queries |
| 34 | Merge Overlapping Subintervals | [LeetCode](https://leetcode.com/problems/merge-intervals/description/) |  |[code.py]() | 🟡 | Sorting, Intervals |
| 35 | Merge Sorted Array Without Extra Space | [LeetCode](https://leetcode.com/problems/merge-sorted-array/description/) |  | [code.py]()| 🟢 | Pointers, In-Place Operations, Two Pointers |
| 36 | Repeating Numbers | [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/) |  | [code.py]() | 🟡 | In-Place Operations, Cycle Detection, Absolute Value |
| 37 | Count Inversions | [LeetCode](https://leetcode.com/problems/count-the-number-of-inversions/description/) |  |[code.py]()| 🔴 | Dynamic Programming, Modular Arithmetic |
| 38 | Reverse Pairs | [LeetCode](https://leetcode.com/problems/reverse-pairs/) |  |[code.py]()| 🔴 | Merge Sort, Efficient Counting Techniques |
| 39 | Maximum Product Subarray | [LeetCode](https://leetcode.com/problems/maximum-product-subarray/) |  |[code.py]()| 🟡 | Array, Prefix and Suffix Products |
| 40 | Count of Smaller Numbers After Self | [LeetCode](https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/) | |[code.py]()| 🔴 | Merge Sort, Divide and Conquer Algorithm, Array and Index Tracking |

---

## Strings

| **#** | **Problem Name** | **Platform** | **Status** | **File** | **Difficulty** | **Prerequisites** |
|- | ---------------------- | ---------------------- | -- | -------- | ----- | --------------- |
| 1 | Remove Outermost Parentheses | [LeetCode](https://leetcode.com/problems/remove-outermost-parentheses/) | | [code.py]() | 🟢 | Strings, Loops, Conditionals |
| 2 | Largest Odd Number in String | [LeetCode](https://leetcode.com/problems/largest-odd-number-in-string/description/) | | [code.py]()| 🟢 | Strings, Basic Number Properties |
| 3 | Longest Common Prefix | [LeetCode](https://leetcode.com/problems/longest-common-prefix/description/) | | [code.py]()| 🟢 | Binary Search, Strings, Prefix, Array Iteration |
| 4 | Isomorphic Strings | [LeetCode](https://leetcode.com/problems/isomorphic-strings/description/) | | [code.py]()| 🟢 | Hash Map, Strings, Character Mapping, Iteration |
| 5 | Rotate String | [LeetCode](https://leetcode.com/problems/rotate-string/description/) | |[code.py]()| 🟢 | String manipulation, String comparison, Loops, Array indexing, Functions |
| 6 | Valid Anagram | [LeetCode](https://leetcode.com/problems/valid-anagram/description/) | |[code.py]()| 🟢 | String manipulation, Hash maps (unordered_map), String comparison, Character counting |
| 7 | Sort Characters By Frequency | [LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/description/) | |[code.py]() | 🟡 | Hashmaps, Priority Queue |
| 8 | Maximum Nesting Depth of the Parentheses | [LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/) | |[code.py]()| 🟢 | Parentheses matching, Stack-like behavior (counting depth), Iteration through strings |
| 9 | Roman to Integer | [LeetCode](https://leetcode.com/problems/roman-to-integer/description/) | |  [code.py]() | 🟢 | Hash maps, Iteration, Conditional logic |
| 10 | String to Integer (atoi) | [LeetCode](https://leetcode.com/problems/string-to-integer-atoi/description/) | | [code.py]() | 🟡 | ASCII operations, Overflow handling, Loops |
| 11 | Substrings with K Distinct | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=count-number-of-substrings) | | [code.py]() | 🟡 | Sliding window, Hash maps, Two-pointer technique |
| 12 | Longest Palindromic Substring | [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/description/) | | [code.py]() | 🟡 | Two Pointers, String Manipulation |
| 13 | Sum of Beauty of All Substrings | [LeetCode](https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/) | | [code.py]() | 🟡 | Brute Force, Frequency Counting |
| 14 | Reverse Words in a String | [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/description/) | | [code.py]() | 🟡 | String Parsing, List Manipulation |

---

## Linked List

| **#** | **Problem Name** | **Platform** | **Status** | **File** | **Difficulty** | **Prerequisites** |
| - | ---------------- | --------- | ---------- | -------------------- | ------ | ------------------ |
| 1  | Creating a Node Structure of Linked List | GeeksForGeeks | ❌ | code.py | 🟡 | Pointers, OOPs |
| 2  | Insert at Head in Linked List | HackerRank | ❌ | code.py | 🟢 | Pointers, OOPs |
| 3  | Insert at Tail in Linked List | GeeksForGeeks | ❌ | code.py | 🟡 | Traversal, Pointers, OOPs |
| 4  | Insert at Position in Linked List | GeeksForGeeks | ❌ | code.py | 🔴 | Counting, Traversal, Pointers, OOPs |
| 5  | Delete at Head in Linked List | GeeksForGeeks | ❌ | code.py | 🟡 | Pointers, OOPs |
| 6  | Delete at Tail in Linked List | GeeksForGeeks | ❌ | code.py | 🟡 | Traversal, Pointers, OOPs |
| 7  | Delete at Given Position in Linked List | GeeksForGeeks | ❌ | code.py | 🔴 | Counting, Traversal, Pointers, OOPs |
| 8  | Search for a Value | GeeksForGeeks | ❌ | code.py | 🟢 | Comparison, Traversal, Pointers, OOPs |
| 9  | Reverse Linked List | LeetCode | ❌ | code.py | 🟢 | Traversal, Pointers, OOPs |
| 10 | Identical Linked List | GeeksForGeeks | ❌ | code.py | 🟡 | Comparison, Traversal, Pointers, OOPs |
| 11 |[Remove Duplicates from Sorted Linked List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)| LeetCode |✅|[code.py](https://github.com/RiyaaChauhan/Striver-A2Z/tree/main/Day_33)| 🟢 | Comparison, Traversal, Pointers, OOPs |
| 12 | Remove Duplicates from Sorted List II | LeetCode | ❌ | code.py | 🟡 | Comparison, Traversal, Pointers, OOPs |
| 13 | Remove Duplicates From an Unsorted Linked List | GeeksForGeeks | ❌ | code.py | 🟢 | Comparison, Traversal, Pointers, OOPs |
| 14 |[Merge Two Sorted Linked Lists](https://leetcode.com/problems/merge-two-sorted-lists/)| LeetCode |✅|[code.py](https://github.com/RiyaaChauhan/Striver-A2Z/tree/main/Day_34)|🟢| Comparison, Traversal, Pointers, OOPs |
| 15 |[Middle of the Linked List]()| LeetCode |✅|[code.py]()| 🟢 | Tortoise and Hare Algorithm, Linked List basics |
| 16 |[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)| LeetCode |✅|[code.py](https://github.com/RiyaaChauhan/Striver-A2Z/tree/main/Day_34)| 🟢 | Floyd’s Cycle Detection Algorithm, Fast and Slow Pointers |
| 17 |[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)| LeetCode |✅|[code.py](https://github.com/RiyaaChauhan/Striver-A2Z/tree/main/Day_34)| 🟡 | Cycle Detection, Resetting Pointers |
| 18 |[Find length of Loop]()| GeeksForGeeks |✅|[code.py](https://github.com/RiyaaChauhan/Striver-A2Z/tree/main/Day_34)| 🟢 | Linked List Basics, Slow & Fast Pointers, Cycle Detection, Pointers, List Traversal |
| 19 | Palindrome Linked List | LeetCode | ❌ | code.py | 🟢 | Linked List Basics, Slow & Fast Pointers, Reversing a Linked List, Pointers, List Traversal |
| 20 | Odd Even Linked List | LeetCode | ❌ | code.py | 🟡 | Linked List Basics, Pointers, List Traversal |
| 21 | Remove Nth Node From End of List | LeetCode | ❌ | code.py | 🟡 | Singly Linked Lists, Pointers, Two-pointers |
| 22 | Delete the Middle Node of a Linked List | LeetCode | ❌ | code.py | 🟢 | Singly Linked Lists, Pointers, Slow-Fast Pointers |
| 23 | Sort List | LeetCode | ❌ | code.py | 🔴 | Singly Linked Lists, Merge Sort, Recursive Merging, Recursion |
| 24 | Sort a linked list of 0s, 1s and 2s | GeeksForGeeks | ❌ | code.py | 🟢 | Linked Lists, In-place Sorting, Pointer Manipulation |
| 25 | Intersection of Two Linked Lists | LeetCode | ❌ | code.py | 🟢 | Linked Lists, Two Pointer Technique, Pointer Manipulation |
| 26 | Add 1 to a Linked List Number | GeeksForGeeks | ❌ | code.py | 🟡 | Linked Lists, Reversal, Carry Handling |
| 27 |[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)| LeetCode |✅|[code.py](https://github.com/RiyaaChauhan/Striver-A2Z/tree/main/Day_28)| 🟡 | Linked Lists, Carry Propagation |
| 28 | Reverse Nodes in k-Group | LeetCode | ❌ | code.py | 🔴 | Linked Lists, Recursion, Reversal Techniques |
| 29 | Rotate List | LeetCode | ❌ | code.py | 🟡 | Linked Lists, Modular Arithmetic |
| 30 | Flattening a Linked List | GeeksForGeeks | ❌ | code.py | 🟡 | Linked List, Pointers, Merging, Sorting, Recursion |
| 31 | Copy List with Random Pointer | LeetCode | ❌ | code.py | 🟡 | Linked Lists, Deep Copy, Hashing |

---

## Bit Manipulation

| **#** | **Problem Name** | **Platform** | **Status** | **File** | **Difficulty** | **Prerequisites** |  
|-----|----------------|------------------------------|----------|--------------|--------------|-----------------|  
| 1  | K-th Bit is Set or No | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1) | ❌ | 250_Kth_Bit_is_Set_or_Not.code.py | 🟢 | Bitwise AND (`&`), Bitwise Shift (`<<`) |
| 2  | Odd or Even | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/odd-or-even3618/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card) | ❌ | 251_Odd_or_Even.code.py | 🟢 | Bitwise AND (`&`) |
| 3  | Power of Two | [LeetCode](https://leetcode.com/problems/power-of-two/description/) | ❌ | 252_Power_of_Two.code.py | 🟢 | Bitwise AND (`&`), Properties of powers of two |
| 4  | Counting Bits | [LeetCode](https://leetcode.com/problems/counting-bits/description/) | ❌ | 253_Counting_Bits.code.py | 🟢 | Bitwise Shift (`>>`), Dynamic Programming |
| 5  | Set the rightmost unset bit | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/set-the-rightmost-unset-bit4436/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card) | ❌ | 254_Set_the_rightmost_unset_bit.code.py | 🟢 | Bitwise OR, Binary Representation |
| 6  | Swap Two Numbers | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1) | ❌ | 255_Swap_Two_Numbers.code.py | 🟢 | Bitwise XOR, Binary Properties |
| 7  | Divide Two Integers | [LeetCode](https://leetcode.com/problems/divide-two-integers/description/) | ❌ | 256_Divide_Two_Integers.code.py | 🟡 | Bitwise Shift, Integer Overflow Handling |
| 8  | Minimum Bit Flips to Convert Number | [LeetCode](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/) | ❌ | 257_Minimum_Bit_Flips_to_Convert_Number.code.py | 🟢 | Bitwise XOR, Counting Set Bits |
| 9  | Exceptionally odd | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/find-the-odd-occurence4820/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card) | ❌ | 258_Exceptionally_odd.code.py | 🟢 | Bitwise XOR, XOR properties, Array iteration, Odd/even occurrences. |
| 10 | Power Set | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/power-set4302/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card) | ❌ | 259_Power_Set.code.py | 🟡 | Bit masking, Set bits, Sorting, String manipulation. |
| 11 | XOR Operation in an Array | [LeetCode](https://leetcode.com/problems/xor-operation-in-an-array/description/) | ❌ | 260_XOR_Operation_in_an_Array.code.py | 🟢 | Bitwise XOR, XOR properties, Looping, Arithmetic sequence. |
| 12 | Single Number III | [LeetCode](https://leetcode.com/problems/single-number-iii/description/) | ❌ | 261_Single_Number_III.code.py | 🟡 | XOR operation, Bitwise manipulation. |
| 13 | Distinct Prime Factors of Product of Array | [LeetCode](https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/description/) | ❌ | 262_Distinct_Prime_Factors_of_Product_of_Array.code.py | 🟡 | Prime factorization, Sets |
| 14 | All divisors of a Number | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1) | ❌ | 263_All_divisors_of_a_Number.code.py | 🟢 | Number theory, Efficient iteration using sqrt(N) |
| 15 | Sieve of Eratosthenes | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card) | ❌ | 264_Sieve_of_Eratosthenes.code.py | 🟢 | Prime Numbers, Sieve Algorithm, Boolean Arrays |
| 16 | Prime Factorization of a Number using Sieve | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/prime-factors5052/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_cardk) | ❌ | 265_Prime_Factorization_of_a_Number_using_Sieve.code.py | 🟡 | Prime Numbers, Factorization, Efficient Iteration |
| 17 | Pow(x, n) | [LeetCode](https://leetcode.com/problems/powx-n/description/) | ❌ | 266_Pow_x_n.code.py | 🟡 | Exponentiation by Squaring, Logarithmic Optimization | 

---

## Stack

| **#** | **Problem Name** | **Platform** | **Status** | **File** | **Difficulty** | **Prerequisites** |
| ----- | ---------------- | ---------------------------------- | ---------- | -------------- | -------------- | ----------------- |
| 1  | Valid Parentheses                          | [LeetCode](https://leetcode.com/problems/valid-parentheses/description/)             | ❌     | code.py    | 🟢         | Stack, String                         |
| 2  | Min Stack                                  | [LeetCode](https://leetcode.com/problems/min-stack/description/)                     | ❌     | code.py    | 🟡         | Stack                                 |
| 3  | Infix to Postfix                           | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1) | ❌     | code.py    | 🟡         | Stack, Operator Precedence            |
| 4  | Prefix to Infix Conversion                 | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/prefix-to-infix-conversion/1) | ❌     | code.py    | 🟡         | Stack, Expression Parsing             |
| 5  | Prefix to Postfix Conversion               | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/prefix-to-postfix-conversion/1) | ❌     | code.py    | 🟡         | Stack, Expression Parsing             |
| 6  | Postfix to Prefix Conversion               | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/postfix-to-prefix-conversion/1) | ❌     | code.py    | 🟡         | Stack, Expression Parsing             |
| 7  | Next Greater Element I                     | [LeetCode](https://leetcode.com/problems/next-greater-element-i/description/)         | ❌     | code.py    | 🟢         | Stack, Monotonic Stack                |
| 8  | Next Greater Element II                    | [LeetCode](https://leetcode.com/problems/next-greater-element-ii/description/)        | ❌     | code.py    | 🟡         | Stack, Monotonic Stack                |
| 9  | Smaller on Left                            | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/smallest-number-on-left3403/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card) | ❌     | code.py    | 🟡         | Stack, Monotonic Stack                |
| 10 | Next Greater Element (NGE)                 | [GeeksForGeeks](https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card) | ❌     | code.py    | 🟡         | Stack, Monotonic Stack                |
| 11 | Trapping Rain Water                        | [LeetCode](https://leetcode.com/problems/trapping-rain-water/description/)            | ❌     | code.py    | 🔴         | Stack, Two Pointers                   |
| 12 | Sum of Subarray Minimums                   | [LeetCode](https://leetcode.com/problems/sum-of-subarray-minimums/description/)       | ❌     | code.py    | 🟡         | Stack, Monotonic Stack                |
| 13 | Asteroid Collision                         | [LeetCode](https://leetcode.com/problems/asteroid-collision/description/)             | ❌     | code.py    | 🟡         | Stack                                 |
| 14 | Sum of Subarray Ranges                     | [LeetCode](https://leetcode.com/problems/sum-of-subarray-ranges/description/)         | ❌     | code.py    | 🟡         | Stack, Sliding Window                 |
| 15 | Remove K Digits                            | [LeetCode](https://leetcode.com/problems/remove-k-digits/description/)                | ❌     | code.py    | 🟡         | Stack, Greedy                         |
| 16 | Largest Rectangle in Histogram             | [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/description/) | ❌     | code.py    | 🔴         | Stack, Monotonic Stack                |
| 17 | Maximal Rectangle                           | [LeetCode](https://leetcode.com/problems/maximal-rectangle/description/)              | ❌     | code.py    | 🔴         | Stack, Dynamic Programming            |
| 18 | Sliding Window Maximum                     | [LeetCode](https://leetcode.com/problems/sliding-window-maximum/description/)         | ❌     | code.py    | 🔴         | Stack                                 |
| 19 | Online Stock Span                          | [LeetCode](https://leetcode.com/problems/online-stock-span/description/)              | ❌     | code.py    | 🟡         | Stack, Monotonic Stack                |

---

# Sliding Window and Two Pointer Combined

| **#** | **Problem Name** | **Platform** | **Status** | **Solution File** | **Difficulty** | **Prerequisites** |
|---|--------------------------------------|-----------------|----------|----------------|--------------|-----------------|
| 1  | Longest Substring Without Repeating Characters           | [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/) | ❌     | code.py                                  | 🟡         | Sliding Window, Hash Map, Two-Pointer Technique |
| 2  | Max Consecutive Ones III                                 | [LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/description/) | ❌     | code.py                                  | 🟡         | Sliding Window, Two-Pointer Technique       |
| 3  | Length of Longest Subarray With at Most K Frequency      | [LeetCode](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/) | ❌     | code.py                                  | 🟡         | Sliding Window, Hash Map, Frequency Count   |
| 4  | Longest Repeating Character Replacement                  | [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/description/) | ❌     | code.py                                  | 🟡         | Sliding Window, Hashing, Two Pointer Technique  |
| 5  | Binary Subarray with Sum                                 | [LeetCode](https://leetcode.com/problems/binary-subarrays-with-sum/description/) | ❌     | code.py                                  | 🟡         | Sliding Window, Two Pointer                 |
| 6  | Count Number of Nice Subarrays                           | [LeetCode](https://leetcode.com/problems/count-number-of-nice-subarrays/description/) | ❌     | code.py                                  | 🟡         | Sliding Window, Two Pointer                 |
| 7  | Number of Substrings Containing All Three Characters     | [LeetCode](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/) | ❌     | code.py                                  | 🟡         | Sliding Window, Two Pointers, String Manipulation |
| 8  | Maximum Points You Can Obtain from Cards                 | [LeetCode](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/) | ❌     | code.py                                  | 🟡         | Sliding Window, Array Manipulation, Subarray Sum |
| 9  | Subarray with K Different Integers                       | [LeetCode](https://leetcode.com/problems/subarrays-with-k-different-integers/description/) | ❌     | code.py                                  | 🔴         | Sliding Window, Two Pointer                 |
| 10 | Minimum Window Substring                                 | [LeetCode](https://leetcode.com/problems/minimum-window-substring/description/) | ❌     | code.py                                  | 🔴         | Sliding Window                              |
