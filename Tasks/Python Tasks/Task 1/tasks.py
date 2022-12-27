# Section 1
#1
x=22
print(x)
#2
x1="python task"
print(x1)
#3
x2=True
x3=15
if x<=x3:
    print(x2)
else:
        x2=False
        print(x2)
        
#4
answer_1=15
print(type(answer_1))   
#5
answer_2="Hallo"
print(type(answer_2)) 
#6
x4=12.3
print(type(x4)) 
x5="welcome"
print(type(x5))
x6=[1,2,3]
print(type(x6))
x7={1,2,3}
print(type(x7))
x8="123"
print(type(x8))    


# Section 2
S1="Ault"
S2="Kelly"
s3=S1[0:2]+S2+S1[2:]
print(s3)
print(s3[::-1])
inp=s3.startswith("AuK")
print(inp)


Txt="Hello world"
print(Txt[0])
print(Txt[2:5])
print(Txt.upper())
print(Txt.lower())




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