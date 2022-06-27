def swapfiledata():
    filename=input("Enter the file name:-")
    filename1=input("Enter the file name:-")
    with open(filename, 'r') as a:
        data_a=a.read
    with open(filename1, 'r') as b:
        data_b=b.read
    with open(filename, 'w') as a:
        a.write(data_b)
    with open(filename1, 'w') as b:
        b.write(data_a)


swapfiledata()