# 11-misol
roy = [27, 65, 19]
roy2 = [98, 23, 11]
print(roy,   roy2)


res = list(map(lambda x, k: x * k, roy, roy2))
print(res)

# 12-misol
roy = ["ali", "xudoybergan2", "ozod9"]
print(roy)

res = list(map(lambda x: x.isalpha(), roy))
print(res)

# 13-misol
roy = [78, 12, 13, 12]
print(roy)
a = int(input("daraja kiriting: "))

res = list(map(lambda x: x ** a, roy))
print(res)


# 14-misol
roy = ["salom", "dunyo", "hello"]
print(roy)

res = list(map(lambda x: x + "!", roy))
print(res)


# 15-misol
roy = [12, 23, 4]
roy2 = [26, 89, 12]
roy3 = [74, 29, 10]
print(roy, roy2, roy3)

res = list(map(lambda x, k,m: sum(x,k,m), roy, roy2, roy3))
print(res)

# 16-misol
roy = [12.6, 38.3, 98.2]
print(roy)

res = list(map(lambda x:int(x) , roy))
print(res)

# 17-misol
roy = ["SALOM", "DUNYO"]
print(roy)

res = list(map(lambda x: x.lower(), roy))
print(res)

# 19-misol
roy = ["salom", "dunyo"]
print(roy)

res = list(map(lambda x: x[-1], roy))
print(res)


# 20-misol
roy = [1, 58, 12, 98]
print(roy)

res = list(map(lambda x: x**2, roy))
print(res)
