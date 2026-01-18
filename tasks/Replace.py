def replace(s, old, new):
    if not old:
        return s
    if not s:
        return ''
    if s.startswith(old):
        return new + replace(s[len(old):], old, new)
    else:
        return s[0] + replace(s[1:], old, new)

def double(s): return ''.join([c * 2 for c in s])

def double1(s):
    if not s: return ''
    else: return s[0] * 2 + double1(s[1:])

def count_less_than(list1, list2):
    if not list1 or not list2: return 0
    else:
        count = 1 if list1[0] < list2[0] else 0
        return count + count_less_than(list1[1:], list2[1:])

print(replace("aasfadfwadasddqwad", "wad", "wow"))
print(double1("aasfadfwadasddqwad"))
print(count_less_than([1, 2, 3, 4 , 5], [3, 3, 3]))