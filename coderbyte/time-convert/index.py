def timeConvert(nums):
    time = str(nums // 60 )+ ":" + str(nums% 60)
    print(time)
    
timeConvert(63)