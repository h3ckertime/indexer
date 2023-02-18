import requests
from bs4 import BeautifulSoup
import os

banner = """

_________ _        ______   _______           _______  _______ 
\__   __/( (    /|(  __  \ (  ____ \|\     /|(  ____ \(  ____ )
   ) (   |  \  ( || (  \  )| (    \/( \   / )| (    \/| (    )|
   | |   |   \ | || |   ) || (__     \ (_) / | (__    | (____)|
   | |   | (\ \) || |   | ||  __)     ) _ (  |  __)   |     __)
   | |   | | \   || |   ) || (       / ( ) \ | (      | (\ (   
___) (___| )  \  || (__/  )| (____/\( /   \ )| (____/\| ) \ \__
\_______/|/    )_)(______/ (_______/|/     \|(_______/|/   \__/
  
                                by Sahmeran
                     Telegram: https://t.me/h3ckertime                                                                                            

  
"""
print(banner)

url = input("Please enter the website URL to be crawled: ")

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Failed to access website:", e)
else:
    print("Website accessed successfully.")
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    print("Links on the page:")
    for link in links:
        print(link.get('href'))

    site_name = url.split('//')[1].replace(".", "_")
    file_name = f"{site_name}.txt"
    error_file_name = f"{site_name}_errors.txt"

    with open(file_name, "w") as f:
        for link in links:
            f.write(link.get('href') + "\n")
        print(f"Links saved to {file_name}.")

    if not os.path.isfile(error_file_name):
        with open(error_file_name, 'w'): pass

    with open(error_file_name, 'a') as f:
        f.write("Website accessed successfully.\n")
