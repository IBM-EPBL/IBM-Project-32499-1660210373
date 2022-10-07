import random
import time

while True:
    temp = random.randint(1,200)
    humidity = random.randint(1,100)
    print("Checking Temperature:{temp1}C \n Checking Humidity:{humidity1}F".format(temp1=temp,humidity1=humidity))
    if temp>=80:
        print("Temperature is {temp2}C \n Alarm Detected...".format(temp2=temp))
        time.sleep(10)
    else:
        print("Temperature is low")
