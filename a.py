m = input("did you have a medical cause Y or N:")
a = int(input("enter the attendance of the student: "))

if m== 'Y':
    print("you areallowed")
else:
    if a>=75:
        print("allowed")
    else:
        print("not allowed")