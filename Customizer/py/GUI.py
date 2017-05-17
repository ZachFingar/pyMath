from Painter import *
from tkinter.colorchooser import *
from math import *

class GUI:

    def __init__(self, dictionary):
        self.root = Tk()
        self.root.title("Customizer")
        
        self.cFrame = Frame(self.root)
        self.cLabel = Label(self.root, text = "Decision Tree:")

        self.aFrame = Frame(self.root, height = 500, width = 500)
        self.aLabel = Label(self.root, text = "File Data:")
        self.arff = Text(self.aFrame, height = 32, width = 50)
        self.aReset = Button(self.root, text = "Reset", command = self.getArff)

        self.n = StringVar()
        self.iFrame = Frame(self.root)
        self.cReset = Button(self.iFrame, text = "Re-Draw", command = self.changeTree)
        self.ciLabel = Label(self.iFrame, text = "Enter maximum number of rows: ")
        self.cText = Entry(self.iFrame, textvariable = self.n)

        
        self.cLabel.grid(row = 0, column = 0)
        self.aLabel.grid(row = 0, column = 1)
        self.cFrame.grid(row = 1, column = 0)
        self.aFrame.grid(row = 1, column = 1)
        self.iFrame.grid(row = 2, column = 0)
        self.aReset.grid(row = 2, column = 1)

        self.P = DrawDecisions(dictionary, self.cFrame)
        self.canvas = self.P.canvas
        self.canvas.config(scrollregion = self.canvas.bbox("all"))
        
        self.xscrollbar = Scrollbar(self.cFrame, orient=HORIZONTAL, command=self.canvas.xview)
        self.yscrollbar = Scrollbar(self.cFrame, orient=VERTICAL, command=self.canvas.yview)
        self.yscrollbar.pack(side=RIGHT, fill=Y)
        self.xscrollbar.pack(side=BOTTOM, fill=X)
        
        self.canvas.pack(side=TOP)
        self.canvas.configure(xscrollcommand=self.xscrollbar.set)
        self.canvas.configure(yscrollcommand=self.yscrollbar.set)

        self.tyscrollbar = Scrollbar(self.aFrame, orient=VERTICAL, command=self.arff.yview)
        self.tyscrollbar.pack(side=RIGHT, fill=Y)

        self.arff.pack(fill = BOTH)
        self.arff.configure(yscrollcommand=self.tyscrollbar.set)
        
        self.ciLabel.pack()
        self.cText.pack()
        self.cReset.pack()

        self.n.set(self.P.rowLength + 1)
        self.data = list()
        self.attribute = list()
        self.decisions = {}
        self.e0 = 0
        self.firstArff()
        
        self.root.mainloop()

    def firstArff(self):
        file = open("Origin.txt")
        for ele in file:
            if "@attribute" in ele:
                self.attribute.append(ele.replace("@attribute","").rstrip())
            elif "@relation"in ele:
                pass
            elif "@data" in ele:
                pass
            else:
                x = ele.rstrip()
                if x == "":
                    pass
                else:
                    self.data.append(x.split(","))

        ele = self.attribute[len(self.attribute)-1]
        self.attribute = self.attribute[:len(self.attribute)-1]
        self.decisions = ele[ele.index("{")+1:ele.index("}")].strip("'").strip("'").split(",")
        self.findEntropy()
        self.getArff()
                
    def findEntropy(self):
        freq = {}
        entropy = 0.0
        i = len(self.attribute)
        for record in self.data:
            if record[i] in self.decisions:
                if record[i] in freq:
                    freq[record[i]] += 1.0
                else:
                    freq[record[i]]  = 1.0
        for ele in freq:
            entropy += -(freq[ele]/len(self.data)) * log(freq[ele]/len(self.data), 2)
            
        self.e0 = entropy

    def getRoot(self):
        for i in range(len(self.attribute)):
            e = list()
            ele = self.attribute[i]
            if "numeric" in ele:
                pass
            else:
                element = ele[:ele.index("{")].strip(" ")
                elements = ele[ele.index("{")+1:ele.index("}")].split(",")
                self.arff.insert(END, element + " entropies:\n")
                for attribute in elements:
                    e.append(self.subsetEntropy(attribute, i))
                total = 0
                for i in range(len(e)):
                    total += e[i][0]*(e[i][1]/len(self.data))
                self.arff.insert(END, "Weighted:  " + str(total) + "\n")
                self.arff.insert(END, "Gain: " + str(self.e0 - total) + "\n\n")

    def subsetEntropy(self, attribute, i):
        fq = {}
        entropy = 0.0
        count = 0
        for record in self.data:
            if attribute == record[i]:
                if record[len(self.attribute)] in fq:
                    fq[record[len(self.attribute)]] +=1
                else:
                    fq[record[len(self.attribute)]]  = 1
                count += 1
        for ele in fq:
            entropy += -(fq[ele]/count) * log(fq[ele]/count, 2)
        self.arff.insert(END, attribute + ": " + str(entropy) + "\n")
        results = [entropy, count]
        return results
    
    def getArff(self):
        self.arff.delete(1.0, END)
        file = open("Origin.txt")

        self.arff.insert(END, "Original Entropy: " + str(self.e0) + "\n")

        self.getRoot()
        self.arff.insert(END, "Arff File:\n")
        for ele in file:
            self.arff.insert(END, ele)
            
    def changeTree(self):
        try:
            n = self.n.get()
            n = int(n)
            if n < 0:
                n = n + 1
            elif n == 0:
                n = 1
            self.P.newBranchLength(n)
        except:
            self.n.set("Integers only!")
        
