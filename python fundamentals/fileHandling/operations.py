with open("sample.txt","r") as f:
    data = f.read()
    print(data)


with open("sample.txt","w") as d:
    d.write("Lets do it buddyyy ....")

with open("sample.txt","a") as ap:
    ap.write("Deal Sealed..")

import os 
os.remove("sample2.txt")