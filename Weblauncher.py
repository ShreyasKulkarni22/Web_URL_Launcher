from sys import *
import webbrowser
import re
import urllib.request

def is_connected():
    lib=urllib.request.urlopen('https://www.google.com/')
    return lib

def Find(string):
    url=re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",string)
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            url=Find(line)
            for str in url:
                webbrowser.open(str,new=2)

def main():
    print("---------Auto WebLauncher by Shreyas Kulkarni---------")
    print("Application Name:"+argv[0])

    if len(argv)!=2:
        print("Error: Invalid number of Arguments")
        exit()
    
    if argv[1]=="-h" or argv[1]=="-H":
        print("This Script is used to open predefined urls present in a file")
        exit()
    
    if argv[1]=="-u" or argv[1]=="-U":
        print("Usage: Application_Name Name_of_file")
        exit()
    
    try:
        connected=is_connected()
        if connected:
            WebLauncher(argv[1])
        else:
            print("Unable to connect to the internet..")
    except ValueError:
        print("Error: Invalid datatype of input")
    except Exception as E:
        print("Error: ",E)

if __name__=="__main__":
    main()