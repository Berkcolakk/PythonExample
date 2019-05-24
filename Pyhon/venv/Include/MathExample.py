def mathMethod(param1,param2,param3):
    total =int(param1)+int(param2)
    msg = print("Total :",total)
    fac = factorial(total,param3);
    for printLst in fac2:
        print(printLst)


def factorial(param1,param2):
    lst = [];
    for read in range(param1):
        param2 = param2 * (read + 1)

        lst.append(param2)

    return lst

num1 = input("Please Enter a Number: ")
num2 = input("Please Enter a Number: ")
factNum = 1;
mathMethod(num1,num2,factNum)