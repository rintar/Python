#coding: utf-8
import datetime

today = datetime.date.today()
birthday = datetime.date(2009, 6, 29)
life = today - birthday
print(life.days)
