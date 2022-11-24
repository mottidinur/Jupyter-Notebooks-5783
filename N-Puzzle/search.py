#search
# זהו הפתרון של תרגיל 1 והוא מימוש בפייתון לפסיאודוקוד שהוצג בכיתה
# search(n)
# f←frontier.create(state.create(n))
# while not frontier.isEmpty(f) do
#     s←frontier.delNext(f)
#     if state.isTarget(s)
#     then return s
#     ns←state.getNext(s)
#     for i←1 to length(ns) do
#       frontier.insert(f,ns[i])
# return null

import state
import frontier

def search(n):
    s=state.create(n)
    print(s)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            print(s)
            depth = s[-1]
            depth2 = f[1]
            items = f[-1]
            print("depth: {2} , items: {1}".format(len(depth),items,depth2))
            return s,depth2,items
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
            #print('frontier:',f)
    return 0

