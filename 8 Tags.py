from bs4 import BeautifulSoup #import beautifulsoup bs library


def read_file():              #function to read file
    file = open('tags.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')  #make soup


meta = soup.meta #accessing meta tag


#access tag attributes either using list [] or using get() function


print(meta.get('charset'))


print(meta['charset'])


# modify attributes


body = soup.body


body['style'] = 'some style' 
