import time
coffee = 0

coffee = int(input("주문(1:보통2:설탕3:블랙):"))

print("끓임")
time.sleep(2)
if coffee == 1:
    print("보통으로 섞음")
if coffee == 2:
    print("설탕섞음")
if coffee == 3:
    print("블랙으로 섞음")
time.sleep(2)
print("물")
time.sleep(2)
print("섞음")
time.sleep(2)
print("배달")
time.sleep(2)
print("끝")
