import terminalCommands as cmd
from manageCustomer import manageCustomer

class program:

    def __init__(self):
        self.main()

    def main(self):
        print("1. Bestaande klant beheren")
        print("2. Nieuwe klant toevoegen")

        choise = input("Kies een optie:")
        match choise:
            case "1":
                self.printCustomers()
                self.selectCustomer()
            case "2":
                self.addNewCustomer()
            case other:
                print('Keuze ongeldig. probeer het opnieuw')
        
        cmd.clear()

    # Manage customers
    def printCustomers(self):
        cmd.changeDir("/home/rlatuh-adm/iac-course/practicum/Python")
        customerFile = open('klanten.txt', 'r') # reads file

        customerNumber = 1
        while True:
        # Get next line from file
            line = customerFile.readline()

        # if line is empty
        # end of file is reached
            if not line:
                break
            print("["+str(customerNumber)+"] "+line.strip())
            customerNumber += 1

        customerFile.close()

    # Selects a customer -> initiates customer management menu
    def selectCustomer(self):
        customerId = input("Kies een klant: ")
        mc = manageCustomer(customerId, self)

    # Adds a new customer customer auto increments
    def addNewCustomer(self):
        cmd.changeDir("/home/rlatuh-adm/iac-course/practicum/Python")
        file = 'klanten.txt'
        customerCount = sum(1 for line in open(file)) # Counts amount of customers

        newCustomer = ""
        with open(file, 'a') as customerFile:
            newCustomer += "klant"+str(customerCount+1)
            customerFile.write("\n"+newCustomer if customerCount > 0 else newCustomer)

        cmd.changeDir("/home/rlatuh-adm/iac-course/practicum")
        cmd.makeDir(newCustomer)
        
        print(newCustomer+" created")
        self.main()