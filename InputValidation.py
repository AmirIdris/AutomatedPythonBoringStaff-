while True:
    print('Enter your Age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric number')
        continue
    if age <1:
        print("please use positive Intiger")
        continue
    break
print(f'your age is {age}')


