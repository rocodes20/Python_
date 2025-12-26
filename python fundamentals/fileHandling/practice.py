data = True
count = 0
with open("sample.txt","r") as f:
    while data:
       data = f.readline()
       count+=1
       if "python" in data:
           print(f"word found at line {count}")
           break
       print(data)
       
