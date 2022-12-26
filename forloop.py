
days = ["monday","tuesday","wednesday","thursday","friday",]
for x in days:
    print(x)

for x in "dheep":
    print(x)  

for x in range(3):
    print("index of", x)

for x in range(1,9,2):
    print(x)

a = ["monday","tuesday","wednesday","thursday","friday",]
b = ["week1","week2","week3",]

for x in a:
    for y in b:
        print(x,y) 


#dict

dict ={
    "name":"dheep",
    "age":"22",
    "siblings":"1"

}
for x in dict:
  print(x)

for x in dict:
  print(dict[x])

for x, y in dict.items():
  print(x, y)'''
'''
lst=[1,2,3,4]

#for item in range(len(lst)):
 #   print(item,lst[item])

for item in lst:
    if item>2:
        print(item)

dict ={
    "name":"dheep",
    "age":"22",
    "siblings":"1"
}

for x, y in dict.items():
  print(x, y)
