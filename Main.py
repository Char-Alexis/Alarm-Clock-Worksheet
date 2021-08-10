from AlarmClock import Alarm_Clock 
# from pythonfile import classname


# Instantiation of Object
time_one = Alarm_Clock()

#  Execuation of Object Method
time_one.time_now() # 2pm
print(time_one.on_off)
time_one.toggle_on_or_off()
print(time_one.on_off)

time_one.change_time() # Set the current time equal to the changed time

# time_one.time_now() # 6pm

