from bs4 import BeautifulSoup  #import libraries



def read_file():               #function to read file
    file = open('intro_to_soup_html.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')  #make soup


title = soup.title


print(title.string)   #accessing navigable strings


# .replace_with("") function to change navigable string


print(title)


title.string.replace_with("title has been changed")


print(title)


