import time 
import RPI.GPIO as gp
print("Enter Pin Number: ")
x=input()
LED = x
if(x > "40" or x < "0"):
    print ("Invalid Number")
else:
    print("Running....")
    
while True:
    time.sleep(2)
    gp.output(LED,gp.HIGH)
    time.sleep(1)
    gp.output(LED,gp.LOW)
    
    
