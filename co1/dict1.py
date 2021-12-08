stud={"regno":250,"age":21,"mark":100}
print(stud)
for i in stud:
    print(i,";",stud[i])
    print(stud[i])

print(stud["age"])
stud["age"]=22
print(stud["age"])
stud["regno"]=1
print(stud["regno"])
stud["name"]="parvathi"
print(stud["name"])
d1={"name":"parvathi","age":21}
d2=d1.copy()
print(d2)
d1.update(stud)
print(d1)
