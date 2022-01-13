# # this is a comment
# # TODO built this function

# def add(num, num2):
#     '''
#     this is supposed to add numbers 
#     '''


# name = "johnny"

# nothing = None

# is_working = True
# car_off = True

# if nothing:
#     print("This is true")  # [x]
#     num = 7
#     print('car is off')
# elif car_off:
#     print('this is the second condition')
#     print('everything will run if car_off is True')
# elif is_working:
#     print('this is working')
# else:
#     print("this is not true...")

# # this is another condition
# if is_working:
#     print('this is working also')

# print(15/6)
# print(15//6)

# print("ace of spades".split(" "))
# # -> ["ace", "of", "spades"]
# print("ace-of-spades".split("-"))
# # -> ["ace", "of", "spades"]
# print("ace of spades".split(" "))
# # -> ["aceofspades"]

# my_scare = "boo"
# my_scare.upper()

# "WHY??".lower()

# "then I went to the store I like".replace("I", "you")

# print("eggs" in "green eggs and ham")
# food = "eggs"

# print(food in "green eggs and ham")

# # conditional -> this first item thatt represents
# # True, it runs that indented [block]

# 'my code rules '[-1]
# 'my code rules'[3:7]
# 'my code rules'[:2]
# 'my code rules'[3:]
# 'my code rules'[::-1]
# 'peiege eleaeteiene'[::2]


# arr = [1, 'two', 3, 'four', True, False, 'hello']
# print(len(arr))
# print(arr[1])
# print(arr[-1])

# print(('peiege eleaeteiene'[::2]))

# one_through_ten = list(range(10))
# print(one_through_ten)

# three_through_ten = list(range(3, 10))
# print(three_through_ten)

# a = [1, 23, 12, 99, 82]
# a.sort()
# print(a)

# a.append(88)
# print("After adding 88", a)

# a.insert(1, 77)
# print("after inserting 77 at index 1 ...", a)

# a.pop()
# print('popping.... ', a)

# if 42 in a:
#     print("yup it's in there")
# else:
#     print("nope")

# # help(list)

# cat = {
#     "name": 'Hamlet',
#     "breed": 'American Shorthair',
#     "fav_food": 'Prosciutto'
# }

# cat["name"] = "Garfield"
# print(cat)

# print(cat.get("name"))


# state = "Washington State"
# year = 1889
# n = 42
# my_message = f"{state} was the {n}th state to join the union in {year}."
# print(my_message)

# location = "California"
# number = 6

# my_second_message = f"{location} is the {number}th largest economy"
# print(my_second_message)

# topic = 'inflation'
# num = 7
# y = 1982
# my_third_message = "{} is at {} percent. highest since {}".format(
#     topic, num, y)
# print(my_third_message)

# template = "my name is {} and i like {}"
# print(template.format("Steve", "Cheese"))


# # loops

# # n = 0
# # while n < 1000:
# #     n += 1
# #     if n % 2 == 0:
# #         print(f'{n} is even...')

# # n = True
# # num = 1
# # while n:

# #     if num % 2 == 0:
# #         print(f'{num} is even')

# #         if num == 750:
# #             n = False
# #             print('End program')
# #     num += 1

# # for loop

# for i in range(1, 751):
#     if i % 2 == 0:
#         print(f'{i} is even...')

#         if i == 750:
#             print("end program")

# nums = [1,2,3,55,66,44,33,750,22,11,33,44]
# for i in range(len(nums)):
#     element = nums[i]
#     if element % 2 == 0:
#         print(f'{i} is even...', 'NUMS')

#         if i == 750:
#             print("Hi I am 750")

# students = ["peter", "paul", "marry", "bingo"]
# for i in range(len(students)):
#     student = students[i]
#     print(student.get("name"))

students = [
    { 
        "name": "Kimmie",
        "city": "Atlanta"
    },
    { 
        "name": "Chris",
        "city": "Salt Lake City"
    },
    { 
        "name": "Zack",
        "city": "Los Angeles"
    }
]

for i in range(len(students)):
    student = students[i]
    print(student.get("name"))

    if student.get("city") == 'Los Angeles':
        print(f'{student.get("name")} wins an iPad for {student.get("city")}', 1)
        print(f"{student.get('name')} wins an iPad for {student.get('city')}", 2)

for i in range(len(students)):
    student = students[i]
    print(student.get("city"))

# Iterating through list of students
for student in students:
    print(student)

# Iterating through dict
for key in students[0]: # key to key
    print(key) # string of the key
    print('value', students[0].get(key))

# Iterating through dict PART 2
for key in students[1]: # key to key
    print(key, 'PART 2') # string of the key
    print('value', students[1][key])

# Iterating through dict PART 3
for anything in students[2]: # key to key
    print(anything, 'PART 3') # string of the key
    print('value', students[2][anything])

# Iterating through dict PART 4
for key, value in students[0].items(): # key to key
    print(key, '->', value)

def say_hello(friend="Tim"): # if we don't put a parameter, it will default to Tim
  print("Hello, {}!".format(friend))

say_hello("Tom")

def move(name, city="Seattle", state="Washington"):
  msg = "{} is moving to {}, {}"
  msg = msg.format(name, city, state)
  print(msg)

move("Charlie", "Los Angeles", "California")
move(city="San Francisco", name="Mark", state="California")
move("John", state="New York", city="New York")



numbers = [1, 2, 3, 4]
def addition(num):
    return num + num

result = map(addition, numbers)
# print(result)

result2 = map(lambda x: x + x, numbers)
# print(list(result2))

result3 = map(lambda y: y * y, numbers)
# print(list(result3))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result4 = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result4))


# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
  
# result contains odd numbers of the list
result5 = filter(lambda x: x % 2 != 0, seq)
# print(list(result5)) # [1, 3, 5, 13]
  
# result contains even numbers of the list
result6 = filter(lambda x: x % 2 == 0, seq)
# print(list(result6)) # [0, 2, 8]
