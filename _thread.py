import os
import threading

'''코드로 스레드 만들기'''


def foo():
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())


if __name__ == '__main__':
    print('process id', os.getpid())
    thread = threading.Thread(target=foo).start()

# process id 55608
# thread id 55528
# process id 55608


'''동일한 작업을 하는 스레드'''


def foo1():
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())


if __name__ == '__main__':
    print('process id', os.getpid())
    thread1 = threading.Thread(target=foo1).start()
    thread2 = threading.Thread(target=foo1).start()
    thread3 = threading.Thread(target=foo1).start()


# process id 39200
# thread id 40892
# process id 39200
# thread id 8600
# process id 39200
# thread id 23372
# process id 39200


'''각기 다른 작업을 하는 스레드'''


def foo2():
    print('This is foo')


def bar():
    print('This is bar')


def baz():
    print('This is baz')


if __name__ == '__main__':
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()

# This is foo
# This is bar
# This is baz
