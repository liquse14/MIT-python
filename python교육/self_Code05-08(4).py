pointcard=True
count=5
age=int(input("나이입력"))

if(age<18):
    print("못삼")
elif((60<=age)or(pointcard==True)and(count==5)):
    print("5000원")

else:
    print("8000원")
    
    
