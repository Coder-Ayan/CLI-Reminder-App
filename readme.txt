It's a CLI reminder app.
It's made by myself using python3.

How does it work?
● Its first input takes the excel file path of the schedule.
● Its second input takes the sheet no of the excel file of the schedule.
● Then it's read the file and saves all the tasks in the schedule list in a structure as [[Title, Description, Time], ...]
● Then it schedules the tasks as its time and waits for the particular times.
● When it's reached the time of the task it sends a notification.


Note:
● Assure it the column names of the excel file starts with the capital letter and other letters are small letters as well as Title, Description, Time.

● If the time(s) of any table(s) accrued before the current time then the notification(s) of the remaining table(s) will send yesterday.
