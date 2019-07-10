from bs4 import BeautifulSoup

import re   #import neccesary libraries


def read_file():     #function to read file
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(),'lxml')   #make soup


regex = re.compile('^b')     #regex to find all tags that start with b


for tag in soup.find_all(regex):
    #print(tag.name)
    pass


regex = re.compile('t')      #regex to find all tags that contains t


for tag in soup.find_all(regex):
    #print(tag.name)
    pass


for tag in soup.find_all(['a','b']):   #find all tags that contain a or b
    #print(tag.name)
    pass

