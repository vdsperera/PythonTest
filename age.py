def getAge():
    age = input('Enter Your Age : ');
    if int(age) < 0:
        raise ValueError('%s is not a valid age' % age);
    return age;

print(getAge());
