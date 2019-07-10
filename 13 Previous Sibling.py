from bs4 import BeautifulSoup     #import  library



def read_file():      #function to read file
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')   #make soup


body = soup.body


print(soup.html.contents)


print(body.previous_sibling.previous_sibling)   #previous_sibling method returns the immidiate previous sibling
