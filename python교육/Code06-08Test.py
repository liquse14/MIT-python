i,k,guguLine=0,0,""

for i in range(9,1,-1):
    guguLine=guguLine+(" #  %d단 #" %i)

print(guguLine)

for i in range(9,0,-1):
    guguLine=""
    for k in range(9,1,-1):
        guguLine=guguLine+str("%2d X%2d=%2d"%(k,i,k*i))# %2d는 두자리 확보
    print(guguLine)
