# Section 3
list1=[100,200,300,400,500]
x=list1[::-1]
print(x)

Fruits=["apple","banana","cherry"]
print(Fruits[1])
Fruits[0]="kiwi"
print(Fruits)
Fruits.insert(1,"lemon")
print(Fruits)
print(Fruits[-1])


Fruits1=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(Fruits1[2:5])

listt=["a","b",["c",["d","e",["f","g"],"k"],"I"],"m","n"]
sub=["h","i","j"]
listt[2][1][2]+=sub
print(listt)
