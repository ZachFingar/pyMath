import tkinter
import csv
from tkinter.filedialog import askopenfilename


class findTargetList():
    def __init__(self):
        self.file = None;
        self.targetPrice = 0;
        self.checkFileFlag = False;
        self.menu = [];
        tkinter.Tk().withdraw();
        self.main();

    def main(self):
        #Program Explanation
        print("This program scans a .csv for a list of items that matches the specified target price. \n" +
              'The first line of the file must start with "target price," followed by a number.')
        self.start()
        prices = sorted(self.menu[1])
        solution = self.findSolution(prices);

        #Print solution
        if solution == None:
            print("No Solution")
        elif not isinstance(solution, list):
            i = menu[1].index(solution)
            print(self.menu[0][i], self.menu[1][i])
        else:
            print("Target Price:", self.targetPrice)
            print()
            print("Items:")
            for answer in solution:
                #match numbers with their items
                i = self.menu[1].index(answer)
                print(self.menu[0][i], self.menu[1][i])

        
    def start(self):
        while (self.checkFileFlag == False):
            input("\nPress Enter to open a valid .csv file.")
            #Open Tkinters file chooser
            filePath = askopenfilename()
            if (self.checkFile(filePath)):
                self.checkFileFlag = True;
            else:
                self.checkFileFlag = False;
        

    def checkFile(self, path):
        #Check the file type, if not .csv - return.
        tag = path[len(path)-4:]
        if (tag != ".csv"):
            print("The file must be saved with the .csv tag.")
            return False
        else:
            #Open file as read only
            self.file = open(path, "r")
            #Make sure the first line contains a target price.
            first = self.file.readline().split(",")
            firstString = first[0].lower().replace(" ", "")
            if (firstString != "targetprice"):
                print('The first line of the file does not start with "target price".')
                return False
            else:
                #Make the second value numerical
                targetString = first[1].strip("\n").replace("$", "") 
                try:
                    self.targetPrice = round(float(targetString), 2)
                except:
                    print('Could not convert target price to numeric.')
                    return False
            item = list()
            price = list()
            for line in self.file:
                row = line.split(",")
                if (row[0] == "\n") or (row[0] == ""):
                    pass
                else:
                    item.append(row[0])
                    #Check if 2nd value is a string or not.
                    numString = row[1]
                    numString = numString.replace("$", "").replace(" ", "")
                    try:
                        number = round(float(numString), 2)
                    except:
                        print('Could not convert Item: "', item, '" price to numeric.' +
                              " Please try again.")
                        return False
                    price.append(number)

            self.menu = [item, price]
            return True

    def findSolution(self, subset):
        allSums = {0} #Final Set, the one that will be iterated through
        findOrigin = {} #dictionary used to trace where additions came from
        solution = list() #The list of solutions

        #Iterate through the subset
        for i in subset:
            #Create a temporary set
            temp = {0}

            #Check to see if this matches target price
            if (i == self.targetPrice):
                return i

            #Iterate through the sums set
            for j in allSums:
                addition = round(i+j, 2) #The next addition to be added to the set
                findOrigin[addition] = [i,j] #Define how this item was created
                temp.add(addition)  #add this to the temp set

                #Check to see if the target price has been found
                if addition == self.targetPrice: 
                    solution.append(findOrigin[j][0]) #the first spot is always in the subset list
                    solution.append(i)
                    
                    last = findOrigin[j][1] #set the stop flag.
                    
                    #if the second spot is 0, then stop
                    while last != 0:
                        #the number in findOrigins [0] slot will always be an original number - i
                        solution.append(findOrigin[last][0])
                        last = findOrigin[last][1]
                        
                        
                    #reverse the solution to give an acsending answer
                    solution.reverse()
                    return solution

            #Add the temporary set to the final set
            allSums |= temp

        return None

findTargetList()
