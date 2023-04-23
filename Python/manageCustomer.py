#from Main import main
import terminalCommands as cmd
import enum
from Models.server import server
from Models.serverType import serverType
from Models.customer import customer

class manageCustomer:

    def __init__(self, customer: customer, main):
        self.customer = customer
        self.mainMenu = main
        cmd.changeDir("/home/rlatuh-adm/iac-course/practicum/"+self.customer.name)
        cmd.clear()
        cmd.currentAbsPath()
        self.printMenu()

    def printMenu(self):
        print("Beheer: "+self.customer.name)
        print("[1] +Webserver")
        print("[2] +Database")
        print("[3] +Loadbalancer")
        print("[4] Huidige configuratie bekijken")
        print("[5] Terug naar hoofdmenu")
        self.deploymentSelector()
    
    # Selects the type of server to be deployed
    def deploymentSelector(self):
        choise = input("Kies een optie: ")
        match choise:
            case "1":
                self.deployServer(serverType.WEB)
            case "2":
                self.deployServer(serverType.DB)
            case "3":
                self.deployServer(serverType.LB)
            case "4":
                self.printCustomerEnv()
            case "5":
                self.mainMenu.__init__()
            case other:
                cmd.clear()
                print('Keuze ongeldig. probeer het opnieuw')
                self.printMenu()

    # Prints all the customers' environments and underlying servers
    def printCustomerEnv(self):
        return 0

    # Gather information and deploy server
    def deployServer(self, serverType: serverType):
        cmd.clear()
        self.server = self.generateServerObject(serverType)
        self.buildVagrantfile(self.server)
        self.addNewConfiguration(self.server)
        self.mainMenu.__init__()
        

    # Adds a new configuration line to the database
    def addNewConfiguration(self, server: server):
        filePath = '/home/rlatuh-adm/iac-course/practicum/Python/klant_server.txt'
        isEmpty = cmd.isFileEmpty(filePath) # check if file is empty

        newServer = self.customer.name+"\t"+server.hostname+"\t"+server.ip+"\t"+server.type.name+"\t"+server.memory # build tab delimited DB string

        with open(filePath, 'a') as customerFile:
            customerFile.write("\n"+newServer if not isEmpty else newServer)
            
    # Returns a serverobject based on user-input
    def generateServerObject(self, serverType: serverType):
        _server = server()
        try:
            _server.type = serverType
            _server.hostname = self.customer.name+'-'+serverType.name
            _server.ip = input('Kies een adres: ') # TODO: beschikbare adressen achterhalen en aangeven
            _server.memory = input('Kies de geheugengrootte: ')
        except Exception as e:
            print('Ongeldige input, probeer het opnieuw')
            self.deployServer()

        return _server
    
    # Builds a custom Vagrantfile and writes it to the customers' directory
    def buildVagrantfile(self, server: server):
        templatePath = '/home/rlatuh-adm/iac-course/practicum/Python/Vagrantfile'
        customerPath = '/home/rlatuh-adm/iac-course/practicum/'+self.customer.name+'/Vagrantfile'

        with open(templatePath, 'r') as vagrantFile:
            template = vagrantFile.read()

        customInput = template.format(hostname=server.hostname, ip=server.ip, memory=server.memory)

        with open(customerPath, 'w+') as vagrantFile:
            vagrantFile.write(customInput)