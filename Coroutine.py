import asyncio
import random

'''yield'''


def my_coroutine():
    while True:
        value = yield
        print('Received value:', value)


# 코루틴 객체 생성
co = my_coroutine()

# 코루틴 실행준비
next(co)

# 값을 보내기
co.send('Hello, world!')


def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3


def my_coroutine2():
    while True:
        x = yield
        print('Received:', x)


co = my_coroutine2()
next(co)

co.send(10)  # Received: 10
co.send(20)  # Received: 20
co.send(30)  # Received: 30


phone_book = {"John": "123-4567", "Jane": "234-5678", "Max": "345-6789"}


def search():
    name = yield
    while True:
        if name in phone_book:
            phone_number = phone_book[name]
        else:
            phone_number = "Cannot find the name in the phone book you know?"
        name = yield phone_number


# 코루틴 객체생성
search_coroutine = search()
next(search_coroutine)

# 겁색 예시
result = search_coroutine.send("John")
print(result)  # 123-4567
result = search_coroutine.send("Jane")
print(result)  # 234-5678
result = search_coroutine.send("Sarah")
print(result)  # Cannot find the name in the phone book you know?


'''async function'''


async def my_coroutine3():
    print('Coroutine started')
    await asyncio.sleep(1)
    print('Coroutine finished')


async def main():
    print('Before calling my_coroutine3')
    await my_coroutine3()
    print('After calling my_coroutine3')

asyncio.run(main())


async def fetch_data():
    print("Data Retrieving")
    await asyncio.sleep(1)  # 데이터를 가져오는데 1초가 걸린다고 가정
    return random.randint(1, 100)


async def main():
    data = await fetch_data()
    print(f'Retrieved Data: {data}')

asyncio.run(main())
