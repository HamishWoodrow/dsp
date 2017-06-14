# Hint:  use Google to find python function
import datetime
####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

####b)
date_start = '12312013'
date_stop = '05282015'

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

def dif_a(date_start,date_stop):
    start=datetime.datetime.strptime(date_start, '%m-%d-%Y').date()
    end=datetime.datetime.strptime(date_stop, '%m-%d-%Y').date()
    return (end-start).days

def dif_b(date_start,date_stop):
    start=datetime.datetime.strptime(date_start, '%m%d%Y').date()
    end=datetime.datetime.strptime(date_stop, '%m%d%Y').date()
    return (end-start).days

def dif_c(date_start,date_stop):
    start=datetime.datetime.strptime(date_start, '%d-%b-%Y').date()
    end=datetime.datetime.strptime(date_stop, '%d-%b-%Y').date()
    return (end-start).days
