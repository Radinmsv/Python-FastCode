import os
import Classes
class Template():
    def __init__(self, Name , Disc, Packages,Files):
            self.Name = Name
            self.Disc = Disc
            self.Packages = Packages 
            self.Files = Files
    def __str__(self) -> str:
        return self.Name
    def CreateProject(self,dir = "C/FastCode/Projects/",ProjectName = "Project_1",AutoImport = True):
        path = os.path.join(str(dir),ProjectName)
        path_to_python_file = os.path.join(path,"Main.py")
        try:
            os.mkdir(path)
        except:
            print("Directory Already Exist")
        
        try:
            Main_Py = open(path_to_python_file,"x")
        except:
            print("File Already Exist")
            Main_Py = open(path_to_python_file,"w")
        if AutoImport == True:
            x = 0
            for i in self.Packages:
                Main_Py.write("import " + str(i) + "\n")
                x += 1

def ChoosePreset(a):
    if a == 1 or a == "Image_Processing":
        return Classes.Image_Processing
