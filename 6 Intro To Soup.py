from bs4 import BeautifulSoup  #import beautiful soup library


def read_file():               #function to read the file
    file = open('intro_to_soup_html.html')
    data = file.read()
    file.close()
    return data


html_file = read_file()


soup = BeautifulSoup(html_file,'lxml')  #making soup


print(soup.prettify()) #indentated version of soup

#
