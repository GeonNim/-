a ={
    "name" : "geon",
    "age" : 20,
    "address" : "Seoul",
    # "address" : "Incheon",
    "gu" : ["sedemoungu", "shinchon"],
    "year": 2001
}

# key 출력
for x in a.keys():
    # print(x)
    pass

# value 출력
for x in a. values():
    # print(x)
    pass


# itmes : key, value를 튜플로 묶어서 출력
# print(a.items())
for key, value in a.items():
    # print(key, value)
    pass

b = dict(a)
# print(b)
b["name"] = "james"
# print(a)
# print(b)

# dictionary 내부의 dictionary
family = {
    "first" :{
        "a": "marshall",
        "b": "james"
    },
    "second":{
        "a": "john",
        "b":"doe"
    }
}

# print(family["first"]["a"])

#setdefault : key가 없을 경우 추가 - 있으면 있는 그 상태를 출력
a.setdefault("year",2024)
print(a)











