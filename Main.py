import os
import time
from tqdm import tqdm

class Template():
    def __init__(self, Name , Disc, Packages):
            self.Name = Name
            self.Disc = Disc
            self.Packages = Packages 
    def __str__(self) -> str:
        return self.Name 
    def create_Project(dire = "",Name = "",Auto_Import_moudels = True):
        path = os.path.join(dire,Name)
        os.mkdir(path)
        print(path)

Image_Processing = Template(Name="Image Processing",
                            Disc="This is The Image Processing Template",
                            Packages=("Numpy","matplotlib","cv2")
                            )


def Main():
    Name = input("Please Enter Your Project Name: ")
    Working_Dir = input("Please Enter The Working Directory: ")
    print("1. " + Image_Processing.Name)
    tem_num = input("Please Enter The Template Number: ")
    if tem_num == 1:
        Image_Processing.create_Project(dire=Working_Dir,Name=Name)


Main()