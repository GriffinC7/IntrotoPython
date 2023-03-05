def main():
 inName = input("Enter Name: ")
 inAge = int(input("Enter Age: "))
 writefile(inName, inAge)
 print("Program finished")
 
def writeFile(name, age):
    outfile = open(text.txt, 'w')

    outfile.write(name +'\n'+, str(age) + '\n')

    outfile.close()



main()
