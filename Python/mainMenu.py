import terminalCommands as cmd
from manageCustomer import manageCustomer
from Models.customer import customer

class mainMenu:

    def __init__(self):
        self.main()

    def main(self):
        print("1. Bestaande klant beheren")
        print("2. Nieuwe klant toevoegen")

        choise = input("Kies een optie:")
        match choise:
            case "1":
                customerCount = self.printCustomers()
                self.selectCustomer(customerCount)
            case "2":
                self.addNewCustomer()
            case other:
                print('Keuze ongeldig. probeer het opnieuw')
        
        cmd.clear()

    # Manage customers
    def printCustomers(self):
        cmd.changeDir("/home/rlatuh-adm/iac-course/practicum/Python")
        customerFile = open('klanten.txt', 'r') # reads file

        customerNumber = 0
        while True: # get next line from file
            line = customerFile.readline()

            if not line: # if line is empty end of file is reached
                break
            customerNumber += 1
            print("["+str(customerNumber)+"] "+line.strip())

        customerFile.close()

        return customerNumber

    # Selects a customer -> initiates customer management menu
    def selectCustomer(self, customerCount):
        try:
            customerId = int(input("Kies een klant: "))
            if(customerId <= customerCount):
                manageCustomer(customer('klant'+str(customerId)), self)
            else:
                raise ValueError('Keuze ongeldig, probeer het opnieuw')
        except Exception as e:
            print(e)
            self.selectCustomer(customerCount)


    # Adds a new customer customer auto increments
    def addNewCustomer(self):
        cmd.changeDir("/home/rlatuh-adm/iac-course/practicum/Python")
        file = 'klanten.txt'
        customerCount = sum(1 for _ in open(file)) # Counts amount of customers

        newCustomer = ""
        with open(file, 'a') as customerFile:
            newCustomer += "klant"+str(customerCount+1)
            customerFile.write("\n"+newCustomer if customerCount > 0 else newCustomer)

        cmd.changeDir("/home/rlatuh-adm/iac-course/practicum")
        cmd.makeDir(newCustomer)
        
        print(newCustomer+" created")
        self.main()