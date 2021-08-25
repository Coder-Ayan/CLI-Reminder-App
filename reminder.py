from pandas import read_excel
import schedule
from plyer import notification

# Taking inputs of the file name and sheet no
file_name = input("Path of the excel file of your schedule: ")
sheet = 'Sheet' + input('Enter the number of the sheet of the excel file: ')

# Raising a value error if any keeps empty
if file_name == '' or sheet.endswith("Sheet"):
    raise ValueError("Values are required")

# Readin the excel file
try:
    df = read_excel(file_name, sheet_name=sheet)
except:
    # Raising a file not found error
    raise FileNotFoundError("The file doesn't found")

today_schedule = []
no_of_rows = len(df.index)

# Appending values in the today_shedule list
for i in range(no_of_rows):
    title = df['Title'][i]
    desc = df['Description'][i]
    time = df['Time'][i]

    today_schedule.append([title, desc, time])

notified = 0 # The notified variable keeps the occurs of notified
# Creating notify function
def notify(title, desc):
    notification.notify(title=title, message=desc,
                        app_icon="python icon.ico")

    # Increasing the value of notified by 1 when a notification has been notified and globaling it
    global notified
    notified += 1
    # Exiting when all notifications are notified
    if notified == no_of_rows:
        exit()


# Scheduling
for item in today_schedule:
    schedule.every().day.at(str(item[2])).do(notify, item[0], item[1])

# Printing one of the way to exit he programm
print("Press Ctrl+c to exit")

while True:
    schedule.run_pending()
