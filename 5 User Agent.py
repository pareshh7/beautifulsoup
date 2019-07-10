import requests
from fake_useragent import UserAgent

# User agent object

ua = UserAgent()

# Specifying the header you wish to send

header = {'user-agent':ua.chrome}

page = requests.get('https://www.google.com',headers=header)

print(page.content)

# Timeout

page = requests.get('https://www.google.com',timeout=3)
