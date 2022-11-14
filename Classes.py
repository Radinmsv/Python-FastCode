
from BaseClass import Template
Image_Processing = Template(Name="Image Processing",
                            Disc="This is The Image Processing Template",
                            Packages=("numpy as np","matplotlib as plt","cv2"),
                            Files=None
                            )

def Maker(a,dir,name,auto):
    preset = None
    if a == 1:
        Image_Processing.CreateProject(dir,name,auto)

    
