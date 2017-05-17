import Cleaner
import GUI

class Decisions:

    def __init__(self):
        cleaner = Cleaner.getClean()
        data = {}
        data = cleaner.cleaner()
        
        GUI.GUI(data)

Decisions()
