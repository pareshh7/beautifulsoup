from bs4 import BeautifulSoup  #import beautiful soup library


def read_file():    #function to read file
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(),'lxml')  #make soup


link = soup.a


for parent in link.parents:  # .parents method returns a list (generator) of parents
    print(parent.name)
