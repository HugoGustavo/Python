import time;
import calendar;

ticks = time.time();
print('Number of ticks since 12:00am, January 1, 1970: ', ticks);
print();
print(time.localtime());

localtime=time.localtime(time.time());
print('Local current time: ', localtime);

localtime = time.asctime(time.localtime(time.time()));
print('Local current time: ', localtime);
print();

cal = calendar.month(2016,2);
print('Here is the calendar: ');
print(cal);