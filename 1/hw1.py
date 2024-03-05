""" 
-100_000_000 100000000
100000000 100000000 (2)

8 8
15 5 (3)

0 7
12 5 (2)

12 5
0 7

-1 12
8 17  (2)

2 3
10 3 (1)

15 5
8 8

10 1
-10 1
"""


from itertools import chain
import time


p, v = map(int, input().split())
q, m = map(int, input().split())

left_v = p-v
right_v = p+v
left_m = q-m
right_m = q+m

# 12 5 0 7 -> 7 17 -7 7

# if right_v == left_m:  # -10^8 10^8 10^8 10^8 & 0 7 12 5
#     print(sum(1 for _ in range(left_v, right_m+1)))
#     print(1)
# elif right_m == left_v:  # -10^8 10^8 10^8 10^8
#     print(sum(1 for _ in range(left_m, right_v+1)))
#     print(2)
# elif right_v < left_m:  # 2 3 10 3
#     print(sum(1 for i in range(left_v, right_v+1) if not i in range(left_m, right_m+1)) +
#           sum(1 for _ in range(left_m, right_m+1)))
#     print(4)
# elif left_v < left_m:
#     print(sum(1 for i in range(left_v, right_v) if not i in range(left_m, right_m+1)) +
#           sum(1 for _ in range(left_m, right_m+1)))
#     print(3)
# elif right_m < right_v and left_m < left_v:  # 15 5 8 8 -> 10 20 0 16 & 10 1 -10 1 -> 9 11 -11 -9
#     print(sum(1 for i in range(left_m, right_v+1)))
#     print(5)
# elif right_m < right_v and left_m > left_v:
#     print(sum(1 for i in range(left_v, right_v+1)))
#     print(6)
# else:  #
#     print(sum(1 for _ in chain(range(left_v, right_v+1), range(left_m, right_m+1))))
#     for i in chain(range(left_v, right_v+1), range(left_m, right_m+1)):
#         print(i)
#     print(7)
start = time.time()
if abs(p) >= 100_000_000:
    print(sum(1 for _ in range(left_v, right_m+1)))
elif abs(q) >= 100_000_000:
    print(sum(1 for _ in range(left_v, right_m+1)))
else:
    res = set(chain(range(left_v, right_v+1), range(left_m, right_m+1)))
    print(len(res))
print(time.time() - start)