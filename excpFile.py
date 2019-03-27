def exists(file):
    try:
        f = open(fileName, "r");
        f.close();
        return True;
    except:
        return False;

fileName = input("Enter File Name : ");
print(exists(fileName));
