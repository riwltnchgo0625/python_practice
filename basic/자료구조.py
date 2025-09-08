# 문자열
# str1 = "python"
# print(str1[0])
# print(str1[-1])
# print(str1[3:5])
# print(str1[1:])
# print(str1[:3])

# data = "python is easy programming laguage"
# print(type(data))
# print( data.count('p') )
# print( data.find('x') )
# print(data.index('p'))
# print(data.replace('python','java'))

# data2 = " henry, 010-12324-5678 "
# print(data2.strip())
# print(data2.split(','))

# # 리스트 
# list3 = ['henry', 25, False]  # 생성
# list3.append(170.5)
# list3.insert(2,69.5)
# list3[1] = 26
# list3.remove("henry")
# list3.pop(0)
# list3.clear()
# print(list3)

# list4 = ['henry', 25, False, 170.5, 52.7]  # 생성
# print( list4[0] )
# print( list4[3 : ] )
# print( list4[ : 2 ] )

# list1 = [1,2,3]
# list2 = [4,5,6]
# print(list1 + list2)
# print(list1 * 3)

# # 튜플
# t = ("henry",25,39.5)
# # t[1] = 26
# print(t[1])

# # packing / unpacking 

# n, a, w = t
# print(n)  # t[0]

# n, *d = t
# print(d)

# 딕셔너리 
dict1 ={"name":"henry", "age":25, "weight": 70.5}
print( dict1["name"] )
dict1["hobby"] = ["football", "sing"]
print( dict1 )
dict1["age"] = 26
print( dict1 )
# dict1.pop("name")
# print( dict1 )
# dict1.clear()
# print( dict1 )

# 딕셔너리 { 키 : 값 }
print( dict1.items() )
print( dict1.keys() )
print( dict1.values() )