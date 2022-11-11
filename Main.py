import time
from tqdm import tqdm

class Template():
    def __init__(self, Name , Disc, Packages):
            self.Name = Name
            self.Disc = Disc
            self.Packages = Packages  

Image_Processing = Template(Name="Image Processing",
                            Disc="This is The Image Processing Template",
                            Packages=("Numpy","matplotlib","cv2"))


def Main():
    Working_Dir = input("Please Enter The Working Directory")
    
Main()