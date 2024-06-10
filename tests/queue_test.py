from persistqueue import Queue

items = ['a', 'b', 'c', 'd', 'e']

q = Queue("mypath")
q.put("a")
q.put("b")
q.put("c")
# x = q.get()
# print(x)
# print(len(q))
q.task_done()
print(len(q))

if (q.empty()):
    print('Queue is empty! Can\'t get any more values!')
else:
    x = q.get()
    print(x)
    q.task_done()