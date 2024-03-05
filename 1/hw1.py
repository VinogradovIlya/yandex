from memory_profiler import profile
import sys
# p, v = list(map(int, input().split()))
# q, m = list(map(int, input().split()))

# tree1 = set(range(p-v, p+v+1))
# tree2 = set(range(q-m, q+m+1))
# res = tree1.union(tree2)
# tree1.clear()
# tree2.clear()
# print(len(res))

""" 
-100000000 100000000
100000000 100000000 (2)

8 8
15 5 (3)

0 7
12 5 (2)

-1 12
8 17  (2)

2 3
10 3 (1)

15 5
8 8
"""


from itertools import chain
p, v = map(int, input().split())
q, m = map(int, input().split())

left_v = p-v
right_v = p+v
left_m = q-m
right_m = q+m

if left_v > right_m or left_m > right_v:  # 2 3 10 3 -> -1 5 7 13
    # если дубликаты присутствуют
    print(sum(1 for _ in chain(range(left_v, right_v+1), range(left_m, right_m+1))))
    # for i in chain(range(left_v, right_v+1), range(left_m, right_m+1)):
    #     print(i)
    print(111)
elif left_v == right_m or left_m == right_v:  # -100000000 100000000 100000000 100000000 & 0 7 12 5
    print(sum(1 for _ in chain(range(left_v, right_v), range(left_m, right_m+1))))
    # for i in chain(range(left_v, right_v), range(left_m, right_m+1)):
    #     print(i)
    print(222)
elif right_m > right_v or left_v > right_v:  # 8 8 15 5 -> 0 16 10 20
    print(sum(1 for _ in chain(range(left_v, left_m), range(left_m, right_m+1))))
    # for i in chain(range(left_v, left_m), range(left_m, right_m+1)):
    #     print(i)
    print('+++')
elif left_v < left_m and right_v > right_m:  # 0 2 0 1 -> -2 2
    # если range без дубликатов
    print(sum(1 for _ in chain(range(left_v, right_v+1))))
    # for i in  chain(range(left_v, right_v+1), range(q-m, q+m+1)):
    #     print(i)
    print(333)
elif left_v > left_m and right_v < right_m:  # 15 5 8 8 -> 0 16 10 20
    # если range без дубликатов
    print(sum(1 for _ in chain(range(left_m, right_m+1))))
    # for i in  chain(range(left_v, right_v+1), range(q-m, q+m+1)):
    #     print(i)
    print(444)
else:
    print('error')

print('final')

p, v = map(int, input().split())
q, m = map(int, input().split())

tree1 = set(range(p-v, p+v+1))
tree2 = set(range(q-m, q+m+1))
res = tree1.union(tree2)
tree1.clear()
tree2.clear()
for i in res:
    print(i)
print(len(res))


""" сделать переменную счетчик, которая хранит последний номер из генератора и 
отсортировать генераторы по алфавиту """
