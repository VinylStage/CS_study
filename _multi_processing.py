from multiprocessing import Process
import os


'''프로세스 만들기'''
print('hellow os')
print(f'my pid is {os.getpid()}')
# hello, os
# my pid is 48352


def foo():
    print(f'child process {os.getpid()}')
    print(f'my parent is {os.getpid()}')


if __name__ == '__main__':
    print(f'parent process {os.getpid()}')
    child = Process(target=foo).start()

# hellow os
# my pid is 51404
# parent process 51404
# hellow os
# my pid is 42388
# child process 42388
# my parent is 42388

'''동일한 작업을 하는 프로세스'''


def foo1():
    print('hello, os')


if __name__ == '__main__':
    child1 = Process(target=foo1).start()
    child2 = Process(target=foo1).start()
    child3 = Process(target=foo1).start()

# hello, os
# hello, os
# hello, os

'''각기 다른 작업을 하는 프로세스'''


def foo2():
    print('This is foo')


def bar():
    print('This is bar')


def baz():
    print('This is baz')


if __name__ == '__main__':
    child1 = Process(target=foo2).start()
    child1 = Process(target=bar).start()
    child1 = Process(target=baz).start()

# This is foo
# This is bar
# This is baz
