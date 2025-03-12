import time
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0 , -1):
    second = x % 60
    minute = int(x /60) % 60
    hours = int(x / 360)
    print(f"{hours:02}:{minute:02}:{second:02}")
    time.sleep(1)
    
print("Time'UP!")