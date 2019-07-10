from bs4 import BeautifulSoup   #import beautiful soup library


def read_file():   #function to read the content of file
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(),'lxml')


title = soup.title


parent = title.parent #accessing the parent of title tag


p = soup.p


print(p.parent.name)  #parent of p tag


html = soup.html


print(type(html.parent))
