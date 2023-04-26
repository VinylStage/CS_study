# count 몇개있는지
text = 'This is taste good!'
count = text.count('t')
print(count)  # 2

# find 어디에 처음있는지(index)
position = text.find('is')
print(position)  # 2

# index find()와 비슷하지만 없을경우 ValueError
try:
    position = text.index("the")
    print(position)
except ValueError:
    print('읎어요')  # 읎어요

# join 특정 문자열 기준으로 합침
a_list = ['가', '나', '다', '라', '마', '바']
joined_list = ','.join(a_list)
print(joined_list)  # 가,나,다,라,마,바

# upper 모두 대문자로 바꿔줌
# lower 모두 소문자로 바꿔줌
# swapcase 소문자는 대문자로 대문자는 소문자로 바꿔줌
uppercase_text = text.upper()
print(uppercase_text)  # THIS IS TASTE GOOD!

lowercase_text = text.lower()
print(lowercase_text)  # this is taste good!

swapcase_text = text.swapcase()
print(swapcase_text)  # tHIS IS TASTE GOOD!

# replace 특정 문자열을 다른 문자열로 바꿔줌
replaced_text = text.replace('good', 'bad')
print(replaced_text)  # This is taste bad!

# split 문자열을 특정 문자를 기준으로 나눠줌(리스트반환)
list_text = 'i,have,a,pen'
ppap = list_text.split(',')
print(ppap)  # ['i', 'have', 'a', 'pen']

# len 리스트의 길이를 반환
print(len(a_list))  # 6

# del 특정 요소를 삭제
del a_list[1]
print(a_list)  # ['가', '다', '라', '마', '바']

# append 리스트 맨뒤에 새로운 요소를 추가
a_list.append('한글')
print(a_list)  # ['가', '다', '라', '마', '바', '한글']

# sort 리스트를 오름차순으로 정렬함
numbers = [4, 5, 2, 4, 76, 5, 6, 7, 4]
numbers.sort()
print(numbers)  # [2, 4, 4, 4, 5, 5, 6, 7, 76]

# reverse 리스트의 순서를 뒤집음
numbers.reverse()
print(numbers)  # [76, 7, 6, 5, 5, 4, 4, 4, 2]

# index 특정요소의 인덱스를 반환하는 메서드
fruits = ['사과', '감', '배']
print(fruits.index('감'))  # 1

# insert 특정위치에 요소를 삽입
fruits.insert(1, '귤')
print(fruits)  # ['사과', '귤', '감', '배']

# remove 특정요소를 제거
fruits.remove('배')
print(fruits)  # ['사과', '귤', '감']

# pop 마지막 요소를 빼낸 뒤 그 요소를 삭제
fruits.pop(1)
print(fruits)  # ['사과', '감']

# count 특정 요소의 개수를 셈
count_numbers = [3, 4, 3, 2, 4, 5, 3, 4, 4]
print(count_numbers.count(4))  # 4

# extend 리스트를 확장하여 새로운 요소들을 추가
count_numbers.extend([35, 456, 567, 76])
print(count_numbers)  # [3, 4, 3, 2, 4, 5, 3, 4, 4, 35, 456, 567, 76]

# +=를 사용해도 가능
count_numbers += [100, 200, 300]
# [3, 4, 3, 2, 4, 5, 3, 4, 4, 35, 456, 567, 76, 100, 200, 300]
print(count_numbers)

# 딕셔너리 초기화

empty_dict = {}
my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(my_dict)

# 딕셔너리 쌍 추가
my_dict["grape"] = 4
print(my_dict)  # {"apple": 1, "banana": 2, "orange": 3, "grape": 4}

# del: 딕셔너리에서 특정 요소를 삭제
del my_dict["apple"]
print(my_dict)  # {"banana": 2, "orange": 3, "grape": 4}

# 딕셔너리에서 특정 Key에 해당하는 Value를 얻는 방법(딕셔너리에 Key가 없는 경우, KeyError)
print(my_dict["banana"])  # 2

# keys 딕셔너리에서 모든 Key를 리스트로 만들기
my_dict2 = {"apple": 1, "banana": 2, "orange": 3}
key_list = list(my_dict2.keys())
print(key_list)  # ["apple", "banana", "orange"]

# values 딕셔너리에서 모든 Value를 리스트로 만들기
value_list = list(my_dict2.values())
print(value_list)  # [1, 2, 3]

# items 딕셔너리의 모든 키와 값을 튜플 형태의 리스트로 반환
person = {'name': 'John', 'age': 30, 'gender': 'male'}
items = person.items()
print(items)  # dict_items([('name', 'John'), ('age', 30), ('gender', 'male')])

# clear 딕셔너리의 모든 요소를 삭제
person = {'name': 'John', 'age': 30, 'gender': 'male'}
person.clear()
print(person)  # {}

# get 딕셔너리에서 지정한 키에 대응하는 값을 반환 (딕셔너리에 Key가 없는 경우, None 반환)
person = {'name': 'John', 'age': 30, 'gender': 'male'}
name = person.get('name')
print(name)  # John
email = person.get('email')
print(email)  # None
# 기본값을 설정할 수 있음
email = person.get('email', 'unknown')
print(email)  # unknown

# 10. in 해당키가 딕셔너리 안에 있는지 확인
person = {'name': 'John', 'age': 30, 'gender': 'male'}
print('name' in person)  # True
print('email' in person)  # False
