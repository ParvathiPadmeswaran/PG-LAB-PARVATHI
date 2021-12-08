place={"location":"kayamkulam","dist":"alappy","pin":690535}
print(place)
del(place["pin"])
print(place)
place.clear()
print(place)
d1={"name":"parvathi","age":21}
d2=d1.copy()
print(d2)
d1.update(place)
print(d1)
print(len(d1))
print()
dn={"name":1,"name1":2,"age":21,}
print(dn)
print(sorted(dn))
print(sorted(dn.items()))
import operator
print("sort dict by key")
sdk=sorted(dn.items(),key=operator.itemgetter(0))
print(sdk)
print("sort dict by value")
sdk=sorted(dn.items(),key=operator.itemgetter(1))
print(sdk)
