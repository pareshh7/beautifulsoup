from bs4 import BeautifulSoup  #import beautiful soup library



def read_file():   #function to read file
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')  #make soup

p = (soup.body.p)


# .next_siblings returns an iterator of next siblings

for sibling in p.next_siblings:
    print(sibling, sibling.name)


# .previous_siblings returns an iterator of previous siblings

for sibling in p.previous_siblings:
    print(sibling, sibling.name)
