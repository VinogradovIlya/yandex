from memory_profiler import profile
# p, v = list(map(int, input().split()))
# q, m = list(map(int, input().split()))

# tree1 = set(range(p-v, p+v+1))
# tree2 = set(range(q-m, q+m+1))
# res = tree1.union(tree2)
# tree1.clear()
# tree2.clear()
# print(len(res))


@profile
def split_line(string, start=0):
    num = ''
    for i in range(start, len(string)):
        if string[i].isdigit():
            num += string[i]
        else:
            break
    return int(num)


@profile
def result(str1, str2):
    # p, v = list(map(int, input().split()))
    # q, m = list(map(int, input().split()))
    # user_v = input()
    # user_m = input()

    p = split_line(user_v)
    v = split_line(user_v, user_v.find(' ') + 1)

    q = split_line(user_m)
    m = split_line(user_m, user_m.find(' ') + 1)
    # print(p, v, q, m)

    tree1 = set(range(p-v, p+v+1))
    tree2 = set(range(q-m, q+m+1))
    res = tree1.union(tree2)
    print(len(res))


if __name__ == '__main__':
    result()
