class getClean:

    def __init__(self):
        self.label = list()
        self.relation = list()
        self.shape = list()
        self.count = list()
        self.log = list()
        self.nodes = list()
        self.relations = list()
        self.labels = list()
        self.diagram = list()
        self.interactions = {}
        self.n = 0
        self.k = 0
        self.full = list()

    def cleaner(self):
        file = open("treeLog.txt")
        for ele in file:
            self.log.append(ele)
            
        for ele in self.log:
            try:
                i = ele.index("N") 
                self.relation.append(ele[i:ele.index("[")].strip(" "))
                i = ele.index('=')
                self.label.append(ele[i+2:ele.index("]")].strip(" ").strip("=").strip('"'))
            except ValueError:
                pass
            
        for i in range(len(self.label)):
            ele = self.label[i]
            try:
                    count = ele[ele.index("(")+1:ele.index(")")]
                    self.label[i] =[ele[:ele.index(" ")], count]
            except ValueError:
                pass

        for i in range(len(self.relation)):
            self.interactions[self.relation[i]] = self.label[i]
            
        for i in range(len(self.interactions)):
            node = "N"+str(i)
            if node in self.interactions:
                self.nodes.append(self.interactions[node])
                for j in range(len(self.interactions)):
                    relation = node + "->N" + str(j)
                    if relation in self.interactions:
                        self.relations.append([i,j])
                        self.labels.append(self.interactions[relation])
                        
        for i in range(len(self.relations)):
            if self.k == self.relations[i][0]:
                self.k += 1
                
        for i in range(len(self.nodes)):
            temp = 0
            for j in range(len(self.relations)):
                if i == self.relations[j][0]:
                    temp += 1
            if temp > self.n:
                self.n = temp
                
        for i in range(len(self.nodes)):
            temp = list()
            for j in range(len(self.relations)+1):
                node = [i , j]
                if node in self.relations:
                        temp.append(j)
            self.diagram.append((i, temp))

        self.full.append(self.diagram)
        self.full.append(self.labels)
        self.full.append(self.relations)
        self.full.append(self.nodes)
        self.full.append(self.n)
        self.full.append(self.k)
        
        return self.full


