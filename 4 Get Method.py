import requests     # Import module


'''
Type of requests :
- GET           --> used to retrieve information
- POST          --> used to send information
'''


# fetching the url using get request

response = requests.get('https://www.google.com')


# response.content

print(response.content)
print(response.status_code)


# response.headers (headers are additional info about the response)

print(response.headers)


for key,value in response.headers.items():
    print(key,'   ',value)




