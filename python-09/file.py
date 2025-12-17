# f = open("file.txt","r") # opens file and by default r is always there 
# data = f.read() # to read a file 
# print(data)
# f.close() # closes a file always 

#TO WRITE IN A FILE :- 
# St = "Yashi are you okay ?"
# f = open("my.txt","w")
# f.write(St)
# line = f.readline()  reads just one line from file
f = open("my.txt","w")
lines = f.readlines() 
print(lines,type(lines)) # reads all all lines but returns a list of strings
# f.write() writes a string 
# f.writelines() writes a list of strings but doesn't add \n automatically
# f.seek() moves the cursor to a specific point of file
# pos = f.tell() tells you the current position of cursor
f.close()
