import re 
dateRegx = re.compile(r'\d\d/\d\d/\d\d\d\d')
mo = dateRegx.search(' Hello is the date 03/14/2019')
