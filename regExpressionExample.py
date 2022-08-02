import re
PhonNumRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo = PhonNumRegEx.search('My number is 415-555-4242.')
print('Phone Number found:' + mo.group())


# running regular expression in a user defined function 

def isPhoneNumber(text):
    phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
    mo = phoneNumber.search(text)
    return mo.group()


number = isPhoneNumber('My number is 415-555-4242.')
print('Phone Number is found from function :' + number)

#  findall() method examples 
PhonNumRegExAll = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
numbers = PhonNumRegExAll.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(numbers)