from playsound import playsound
import os
from datetime import datetime
from datetime import date
import time
import schedule
import winsound;


# time 
current_datetime = datetime.now()
time_value = current_datetime.strftime("%H:%M:%S")

print("Time:", time_value)


# day and date
current_date = date.today()
day = current_date.strftime("%A")
date_value = current_date.strftime("%Y-%m-%d")
print("Day:", day)
print("Date:", date_value)

# class
class_name="1"
main_folder="main_folder"

#location of the program
script_dir = os.path.dirname(os.path.abspath(__file__))



#schedule

#functions of the schedule
def _1(period):
    print("Executing task at", time.strftime("%Y-%m-%d %H:%M:%S"))
    print(period)

    #the file runner

    folder_name = period
    #no of audio files run
    i=1
    while(i<=5): 
      file_name = str(i)+".wav"
      file_path = os.path.join(script_dir,main_folder,class_name,str(day), folder_name, file_name)
      if os.path.isfile(file_path):
        print("playing audio :",i)
        winsound.PlaySound(file_path,winsound.SND_FILENAME)
        # playsound(file_path)
      i=i+1
_1("1")



#schedule intial time fixer
schedule.every().day.at("14:20").do(lambda: _1("1")).tag('1')
schedule.every().day.at("11:22:20").do(lambda: _1("2")).tag('2')
schedule.every().day.at("09:45").do(lambda: _1("3")).tag('3')
schedule.every().day.at("10:30").do(lambda: _1("4")).tag('4')
schedule.every().day.at("11:15").do(lambda: _1("5")).tag('5')
schedule.every().day.at("11:30").do(lambda: _1("6")).tag('6')
schedule.every().day.at("12:15").do(lambda: _1("7")).tag('7')
schedule.every().day.at("13:00").do(lambda: _1("8")).tag('8')
schedule.every().day.at("13:45").do(lambda: _1("9")).tag('9')
schedule.every().day.at("14:30").do(lambda: _1("10")).tag('10')
schedule.every().day.at("15:15").do(lambda: _1("11")).tag('11')
schedule.every().day.at("15:25").do(lambda: _1("12")).tag('12')
schedule.every().day.at("16:05").do(lambda: _1("13")).tag('13')
schedule.every().day.at("16:45").do(lambda: _1("14")).tag('14')





#infinte loop the sechudule checker
while True:
    schedule.run_pending()
    time.sleep(1)