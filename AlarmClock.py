class Alarm_Clock:

    def __init__(self):
        self.current_time = 2 
        self.on_off = False #Initially the clock will be off
        self.set_time = 6


    def time_now(self):
        print("Current Time: " + str(self.current_time) + "pm")
        return self.current_time 

    def toggle_on_or_off(self):
        if(self.on_off == True):
             self.on_off = False # If the clock is currently on (True) --> turn it off (False)
        else: # Clock is currently off (False) --> turn it on
            self.on_off = True

    def change_time(self):
        self.current_time = self.set_time
        print("Alarm is set to: " + str(self.set_time) + "pm" ) 

