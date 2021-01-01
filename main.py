import json
import threading
import time as t
import os

#method that returns the size of a string in bytes
def utf8len(s):
    return len(s.encode('utf-8'))

#method to implement the time-to-live property
def Timer(key,timer):
    print("Thread started")
    time = int(timer)
    while time>0:
        t.sleep(1)
        time-=1
    key = str(key)
    #print("Thread ended")
    if key in main.data.keys():
        #print("Key Found")
        del main.data[key]
    file = open("DataStore.txt", 'w')
    s = ""
    for i in main.data.keys():
        s += i + "-" + str(main.data[i]) + "\n"
    file.write(s)
    file.close()

#initializes json object
class JSON_OBJECT:
    def __init__(self, json, time, key):
        self.json = json
        self.time = time
        if time !=-1:
            thread = threading.Thread(target=Timer, args=(key,self.time))
            thread.start()
            
#class that defines the CRD methods 
class Main:
    def __init__(self,dir):
        self.DIR = dir
        file = open('DataStore.txt','w+')
        file = open('DataStore.txt','r')
        self.data = dict()
        s = file.read()
        for data in s.split("\n"):
            if(data == ""):continue
            key = data.split("-")[0]
            value = data.split("-")[1]
            value = '"'+value
            value += '"'
            value = json.loads(value)
            self.data[key] = value
        print(self.data)
    def get_JSON(self,s):
            return json.loads(s)
    def Create(self,key, value):
        f_size=os.stat('DataStore.txt').st_size
        if f_size>1000000000:
            return "Error: File size exceeds 1GB"
        if key in self.data.keys():
            return "Error: Key already exists"
        self.data[key] = value
        file = open("DataStore.txt",'w')
        s = ""
        for i in self.data.keys():
            s += i+"-"+str(self.data[i])+"\n"
        file.write(s)
        file.close()
        return "Successful"

    def convert_json_to_JSON_OBJECT(self,json,time,key):
        return JSON_OBJECT(json,time,key)

    def Read(self,key):
        if key in self.data.keys():return self.data[key]
        return "Error: No such key available"

    def Delete(self,key):
        if key in self.data.keys():
            del self.data[key]
            file = open("DataStore.txt", 'w')
            s = ""
            for i in self.data.keys():
                s += i + "-" + str(self.data[i]) + "\n"
            file.write(s)
            file.close()
            return "Successful"
        return "Error: No such key available"

main = Main("")
def create_key():
    key = input("Enter the key:\n")
    if utf8len(key)>32:
        print("Error: The key size should be less than 32 chars.")
        return
    s = input("Enter the json name:\n")
    if utf8len(s)>16000:
        print("Error: The key size should be less than 32 chars.")
        return
    b = input("1)Time_to_Live\n2)No Time_to_Live\n")
    if(b=="1"):
        time = input("Enter the time:\n")
        time = int(time)
        js = main.get_JSON(s)
        js = main.convert_json_to_JSON_OBJECT(js, time, key)
    else:
        js = main.get_JSON(s)
        js = JSON_OBJECT(js, -1, key)
    print(js)
    if js != "Invalid JSON":
        print(main.Create(key,js.json))

while True:
    print("1)Create","2)Read","3)Delete","4)Quit\n")
    option = input("Choose the action\n")
    if option=="1":
        create_key()
    if option=="2":
        key = input("Enter the key\n")
        print(main.Read(key))
    if option=="3":
        key = input("Enter the key\n")
        print(main.Delete(key))
    if option=="4":
        break

