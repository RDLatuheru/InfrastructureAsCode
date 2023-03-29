#from Main import main
import terminalCommands as cmd
import enum

class manageCustomer:

    main = None

    def __init__(self, customerId, main):
        self.customer = "klant"+customerId
        self.main = main
        cmd.changeDir("/home/rlatuh-adm/iac-course/practicum/"+self.customer)
        cmd.clear()
        print("Beheer: "+customerId)
        cmd.currentAbsPath()
        self.printMenu()

    def printMenu(self):
        print("[1] +Webserver")
        print("[2] +Database")
        print("[3] +Loadbalancer")
        print("[4] Huidige configuratie bekijken")
        print("[5] Terug naar hoofdmenu")
        self.runOption()
    
    def runOption(self):
        choise = input("Kies een optie: ")
        
        match choise:
            case "1":
                print("Deploying webserver")
            case "2":
                print("Deploying webserver")
            case "3":
                print("Deploying loadbalacer")
            case "4":
                self.printCustomerEnv()
            case "5":
                self.main.__init__()
            case other:
                print('Keuze ongeldig. probeer het opnieuw')

    def printCustomerEnv(self):
        return 0
    
    def addNewConfiguration(self, configType):
        file = 'klant_server.txt'
        isEmpty = cmd.isFileEmpty(file) # check if file is empty

        customerConfig = self.customer+"\t"+configType

        with open(file, 'a') as customerFile:
            customerFile.write("\n"+customerConfig if not isEmpty else customerConfig)