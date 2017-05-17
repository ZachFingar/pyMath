from tkinter import *

class DrawDecisions:

    def __init__(self, dictionary, root):
        data = dictionary

        self.diagram = data[0]
        self.labels = data[1]
        self.nodes = data[3]
        self.relations = data[2]
        self.n = data[4]
        self.k = data[5]
        self.coords = {}
        self.nodeLength = 0
        self.rowLength = 0

        self.selected = None

        self.ocolor = "dark green"
        self.rcolor = "#1e81f9"
        self.tcolor = "white"
        self.rtcolor = "white"
        self.activeColor = "#1fe0db"
        self.lcolor = "#1fe0db"

        self.current = ""
        self.stop = True
        
        self.HEIGHT = 800
        self.WIDTH = 1200
        self.canvas = Canvas(root, bg = "#464646", height = 500, width = 800)

        self.packTree()
        
        self.canvas.focus_set()
        self.canvas.bind("<Button-1>", self.move)
        self.canvas.bind("<B1-Motion>", self.drag)
        self.canvas.bind("<ButtonRelease-1>", self.drop)
        self.canvas.bind("<Button-3>", self.select)

    def move(self, event):
        node = self.canvas.gettags(event.widget.find_withtag("current"))
        if node != ():
            self.current = node[0]
            self.stop = False
        else:
            pass
        if self.selected != None:
            self.resetSelected()
        
    def drag(self, event):
        if self.stop == False:
            if "N" not in self.current:
                pass
            else:
                node = (self.current.replace("N", ""))
                node = (node.replace("S", ""))
                node = (node.replace("R",  ""))
                node = int(node)
                self.canvas.delete("S" + self.current)
                self.canvas.delete(self.current)
                x = self.canvas.canvasx(event.x)
                y = self.canvas.canvasy(event.y)
                x1 = x - 50
                y1 = y - 25
                x2 = x1 + 100
                y2 = y1 + 50
                self.coords[node] = [x1, y1, x2, y2]
                if len(self.diagram[node][1]) != 0:
                    self.canvas.create_oval(x1,y1,x2,y2, activefill = self.activeColor, fill = self.ocolor,
                                                                tags = (self.current))
                else:
                    self.canvas.create_rectangle(x1,y1,x2,y2, activefill = self.activeColor, fill = self.rcolor,
                                                 tags = (self.current))
                self.canvas.update()


    def drop(self, event):
        if self.stop == False:
            self.stop = True
            self.reLine()
            self.reNode()
            
    def select(self,event):
        node = self.canvas.gettags(event.widget.find_withtag("current"))
        if node != ():
            if "N" not in node[0]:
                pass
            else:
                if self.selected == None:
                    self.selected = node[0]
                    self.canvas.itemconfig(self.selected, fill = self.activeColor)
                else:
                    self.resetSelected()
                    self.selected = node[0]
                    self.canvas.itemconfig(self.selected, fill = self.activeColor)
        else:
            if self.selected == None:
                pass
            else:
                self.resetSelected()
                
                
    def resetSelected(self):
        self.reNode()
        self.selected = None
        
    def packTree(self):
        self.outline()
        self.packNodes()
        self.packLines()
        self.reNode()
           
    def packNodes(self):
        for i in self.coords:
            setUp = self.coords[i]
            x1 = setUp[0]
            y1 = setUp[1]
            x2 = setUp[2]
            y2 = setUp[3]

            node = "N" + str(i)
            ntext = "SN" + str(i)
            if len(self.diagram[i][1]) != 0:
                self.canvas.create_oval(x1,y1,x2,y2, activefill = self.activeColor,
                                       fill = self.ocolor, tags = (node))
            else:
                self.canvas.create_rectangle(x1,y1,x2,y2, activefill = self.activeColor,
                                                 fill = self.rcolor, tags = (node))
                if "/" in self.nodes[i][1]:
                    attributes = self.nodes[i][1].split("/")
                    main = attributes[0]
                    other = attributes[1]
                    p = float(other) / float(main)
                    x3 = x2 - (p*100)
                    self.canvas.create_rectangle(x3,y1,x2,y2, activefill = self.activeColor,
                                                 fill = "red", tags = (node))
                    
            midx = x2 - (100/2)
            midy = y2 - (50/2)
            self.canvas.create_text(midx,midy, fill = self.tcolor, text = self.nodes[i], tags = ntext)

    def packLines(self):
        count = 0
        for i in self.coords:
            setUp = self.coords[i]
            x1 = setUp[2]
            y1 = setUp[3]
            midx1 = x1 - (100/2)
            midy1 = y1 - (50/2)
            for j in range(0, len(self.diagram[i][1])):
                node = "N" + str(self.diagram[i][1][j])
                try:
                    setUp = self.coords[self.diagram[i][1][j]]
                    x2 = setUp[2]
                    y2 = setUp[3]
                    midx2 = x2 - (100/2)
                    midy2 = y2 - (50/2)
                    relation = "R" + str(i)
                    text = "SR" + str(i)
                    self.canvas.create_line(midx1,midy1,midx2,midy2, fill = self.lcolor, tags = relation)
                    midx = (midx2 + midx1)/2
                    midy = (midy2 + midy1)/2
                    self.canvas.create_text(midx, midy, fill = self.rtcolor, text = self.labels[count], tags = text)
                    count += 1
                except:
                    pass

                
    def reLine(self):
        for i in range(len(self.diagram)):
            relation = "R" + str(i)
            text = "SR" + str(i)
            self.canvas.delete(relation)
            self.canvas.delete(text)
        self.packLines()
        
    def reNode(self):
        for i in self.coords:
            node = "N" + str(i)
            text = "SN" + str(i)
            coords = self.coords[i]
            x1 = coords[0]
            y1 = coords[1]
            x2 = coords[2]
            y2 = coords[3]
            self.canvas.delete(node)
            self.canvas.delete(text)
            if len(self.diagram[i][1]) != 0:
                self.canvas.create_oval(x1,y1,x2,y2, activefill = self.activeColor,
                                        fill = self.ocolor, tags = (node))
            else:
                self.canvas.create_rectangle(x1,y1,x2,y2, activefill = self.activeColor,
                                             fill = self.rcolor, tags = (node))
                if "/" in self.nodes[i][1]:
                    attributes = self.nodes[i][1].split("/")
                    main = attributes[0]
                    other = attributes[1]
                    p = float(other) / float(main)
                    x3 = x2 - (p*100)
                    self.canvas.create_rectangle(x3,y1,x2,y2, activefill = self.activeColor,
                                                 fill = "red", tags = (node))
            midx = x2 - (100/2)
            midy = y2 - (50/2)
            self.canvas.create_text(midx, midy, state = DISABLED, disabledfill = self.tcolor, text = self.nodes[i], tags = text)

    def outline(self):
        dx = 100
        dy = 50
        x1 = (self.WIDTH/2) - (dx/2)
        x2 = x1 + dx
        y1 = 25
        y2 = y1 + dy
        self.coords[0] = [x1,y1,x2,y2]
        row = self.getRows()
        for i in range(len(row)):
            x1 = self.coords[0][0]
            x2 = self.coords[0][2]
            y1 = y1 + 2*dy
            y2 = y1 + dy
            
            nodes = len(row[i]) * dx
            gaps = (len(row[i]) - 1) * (dx / 2)
            rowLength = nodes + gaps
            
            x1 = x1 - ((rowLength)/2) + 50
            x2 = x1 + dx
            for node in row[i]:    
                self.coords[node] = [x1,y1,x2,y2]
                x1 = x1 + dx + (dx/2)
                x2 = x1 + dx
                self.nodeLength += 1

    def getRows(self):
        rows = list()
        row = list()

        rows.append(self.diagram[0][1])
        self.findChildren(self.diagram[0][1], row)
        for r in row:
            if len(r) == 0:
                pass
            else:
                rows.append(r)
        self.rowLength = len(rows)
        return rows
        
            
    def findChildren(self, parents, rows = list(), n = 0):
        row = list()
        for parent in parents:
            children = self.diagram[parent][1]
            if len(children) == 0:
                pass
            else:
                for child in children:
                    row.append(child)
        rows.append(row)
        n += 1
        if n == len(self.diagram):
            return
        else:
            self.findChildren(row, rows, n)

    def newBranchLength(self, n):
        self.canvas.delete("all")
        row = self.getRows()
        row = row[0:n-1]
        self.coords = {}
        dx = 100
        dy = 50
        x1 = (self.WIDTH/2) - (dx/2)
        x2 = x1 + dx
        y1 = 25
        y2 = y1 + dy
        self.coords[0] = [x1,y1,x2,y2]
        for i in range(len(row)):
            x1 = self.coords[0][0]
            x2 = self.coords[0][2]
            y1 = y1 + 2*dy
            y2 = y1 + dy
            
            nodes = len(row[i]) * dx
            gaps = (len(row[i]) - 1) * (dx / 2)
            rowLength = nodes + gaps
            
            x1 = x1 - ((rowLength)/2) + 50
            x2 = x1 + dx
            for node in row[i]:    
                self.coords[node] = [x1,y1,x2,y2]
                x1 = x1 + dx + (dx/2)
                x2 = x1 + dx
        self.packNodes()
        self.packLines()
        self.reNode()





        
