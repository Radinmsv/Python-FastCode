import os
import time
from tqdm import tqdm
from Classes import *
list = [Image_Processing]
def Main():
    name = input("Please Enter the Project Name: ")
    Dir = input("Choose a directory ")
    x = 1
    for i in list:
        print(str(x) + ". " + str(i))
    x += 1
    a = input("Please Choose a preset: ")
    aimport = input("Do you want auto import? (True/False) ")
    if aimport == "True":
        aimport = True
    if aimport == "False":
        aimport = False
    Maker(a,Dir,name,aimport)
if __name__ == "__main__":
    Main()