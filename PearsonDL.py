import os
import urllib.request
import os.path
from os import path

print("PearsonDL")
print("Developed by NamesJoeyWheeler & FurryLovingMcNugget")
print("---------------------------------------------------")
id = input("Book ID: ")
pages = int(input("How many pages would you like? "))

if os.path.isfile('Pearson Books/') and os.access('Pearson Books/', os.R_OK):
    for i in range(0, pages):
        pb = f'https://d38l3k3yaet8r2.cloudfront.net/resources/products/epubs/generated/{id}/foxit-assets/pages/page{i}?password=&accessToken=null&formMode=true'
        urllib.request.urlretrieve(pb, f'Pearson Books/{id}/{i}.png')
        print('Downloading...')
else:
    directory = id
    parent_dir = 'Pearson Books/'
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)
    for i in range(0, pages):
        pb = f'https://d38l3k3yaet8r2.cloudfront.net/resources/products/epubs/generated/{id}/foxit-assets/pages/page{i}?password=&accessToken=null&formMode=true'
        urllib.request.urlretrieve(pb, f'Pearson Books/{id}/{i}.png')
        print('Downloading...')
