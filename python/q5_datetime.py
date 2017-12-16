# Hint:  use Google to find python function

from datetime import datetime


def find_delta_days(start, stop, date_format):
    delta = datetime.strptime(stop, date_format) - datetime.strptime(start, date_format)
    return delta


####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

print('A. {}'.format(find_delta_days(date_start, date_stop, '%m-%d-%Y')))

####b)  
date_start = '12312013'  
date_stop = '05282015'  

print('B. {}'.format(find_delta_days(date_start, date_stop, '%m%d%Y')))

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

print('C. {}'.format(find_delta_days(date_start, date_stop, '%d-%b-%Y')))
  
