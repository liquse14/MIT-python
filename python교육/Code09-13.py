import random

sum = 0


##함수선언##
def getNumber():
    return random.randrange(1, 46)


##전역변수선언##
lotto = []
num = 0

##메인코드부분##
print("로또추첨\n");

while True:
    num = getNumber()

    if lotto.count(num) == 0:
        lotto.append(num)
    if len(lotto) >= 6:
        break

print("추첨된 로또 번호==>", end='')
lotto.sort()
for i in range(0, 6):
    print("%d " % lotto[i], end='')
    sum += lotto[i]
print("\n총합은 %d" % sum)
