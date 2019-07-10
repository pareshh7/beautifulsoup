from bs4 import BeautifulSoup      #import beautiful soup library


def read_file():    #function to read file
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')    #make soup


#Signature: find_all(name, attrs, recursive, string, limit, **kwargs)


#name parameter


a_tags = soup.find_all('a')


#attrs parameter passed as a dictionary


attr = {'class':'story'}


first_a = soup.find_all(attrs=attr)


print(first_a)


#recursive paramter


title = soup.find_all('title',recursive=False)


print(title)


# string parameter


regex = re.compile('story')


tag = soup.find_all(string=regex)


#limit parameter limits the no of output given by find_all function


a_tags = soup.find_all('a',limit=2)


print(a_tags)


# **kwargs arguments

tags = soup.find_all(class_='story')


# to write the class attribute of a tag - use class_ since simple class is a keyword in Python



