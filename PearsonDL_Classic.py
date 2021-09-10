import os
import urllib.request
import os.path
from os import path

print("PearsonDL")
print("Developed by NamesJoeyWheeler & FurryLovingMcNugget")
print("---------------------------------------------------")
num = input("Product Number: ")
id = input("Book ID: ")
pages = int(input("How many pages would you like? "))
directory = id
parent_dir = 'Pearson Books/'
path = os.path.join(parent_dir, directory)
os.makedirs(path)
for i in range(0, pages):
    opener = urllib.request.build_opener()
    opener.addheaders = [('ADD COOKIE HERE!')]
    urllib.request.install_opener(opener)
    pb = f'https://plus.pearson.com/eplayer/pdfassets/prod1/{num}/{id}/pages/page{i}?password=&accessToken=null&formMode=true'
    urllib.request.urlretrieve(pb, f'Pearson Books/{id}/{i}.png')
    print('Downloading...')