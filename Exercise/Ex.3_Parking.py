# look at the file " parking.py " first
import math

Entrance_Hours = int(input("Enter the number of hours you want to park: "))
Entrance_min = int(input("Enter the number of minutes you want to park: "))
Exit_Hours = int(input("Enter the number of hours you want to exit: "))
Exit_min = int(input("Enter the number of minutes you want to exit: "))

TIme_En = Entrance_Hours * 60 + Entrance_min  #change the time to minutes
Time_Ex = Exit_Hours * 60 + Exit_min

delta_time = abs(Time_Ex - TIme_En)
print(delta_time)

if delta_time <= 15 :
    print("0")
elif 15 < delta_time <= 180 :
    print(math.ceil(delta_time/60)*10)
elif 180 < delta_time < 240 :
    print(math.ceil((delta_time/60)+1)*10)
elif 240 <= delta_time <= 360 :
    print(math.ceil(delta_time/60)*20)
else:
    print("200")
