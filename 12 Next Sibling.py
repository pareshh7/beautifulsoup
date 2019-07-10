from bs4 import BeautifulSoup   #import beaautiful soup library



def read_file():               #function to read file
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')         #make soup


body = soup.body


p = soup.body.p  #accessing the sibling p tag of body tag


print(body.contents)


print(p.next_sibling.next_sibling)  #next sibling method returns the immidiate sibling 

