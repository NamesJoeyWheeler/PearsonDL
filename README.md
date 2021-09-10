# PearsonDL

A Python script that downloads books from the Pearson website in (multiple) PNG files and/or a single PDF file.

# Disclaimer

Only use this for books you LEGALLY own. We do not condone, promote or tolerate the use of this script for illegal purposes.

# What is needed:

- Python 3.x (tested with `3.6`, `3.7` and `3.9`)
- Pillow (if PDF generation is desired)

# How to use:

- Linux/Mac:
  - Open a new terminal
  - Clone this repo (`git clone https://github.com/NamesJoeyWheeler/PearsonDL.git`)
  - `cd` into the repo folder (`cd PearsonDL`)
  - To only download PNG images:
    - Run the downloader as so:
      - `python3 PearsonDL.py -i <ID> -p <Number_Of_Pages>` or
      - `./PearsonDL.py --id <ID> --pages <Number_Of_Pages>`
  - To generate a PDF file as well:
    - Install the required packages:
      - `pip3 install -r requirements.txt`
    - Run the downloader with the `-g` flag:
      - `python3 PearsonDL.py -i <ID> -p <Number_Of_Pages> -g`
      - `./PearsonDL.py --id <ID> --pages <Number_Of_Pages> --generate_pdf`

- Windows:
  - Open a new CMD or PowerShell window
  - Clone this repo (`git clone https://github.com/NamesJoeyWheeler/PearsonDL.git`)
  - `cd` into the repo folder (`cd PearsonDL`)
  - To only download PNG images:
    - Run the downloader as so:
      - `python3 PearsonDL.py -i <ID> -p <Number_Of_Pages>` or
      - `./PearsonDL.py --id <ID> --pages <Number_Of_Pages>`
  - To generate a PDF file as well:
    - Install the required packages:
      - `pip3 install -r requirements.txt`
    - Run the downloader with the `-g` flag:
      - `python3 PearsonDL.py -i <ID> -p <Number_Of_Pages> -g -r`
      - `./PearsonDL.py --id <ID> --pages <Number_Of_Pages> --generate_pdf --remove_png`
 
- You should be able to find out how many pages the book has by going onto the last page of the book on the Pearson site (or viewing the manifest link).

- It will now download the pages into a folder named after the ID which is in the `Pearson Books` folder.

- If the `-g` flag was passed, the program will now generate a PDF of all the downloaded pages, titled `<id>.pdf`

- If the `-r` flag was passed, the program will now delete all the downloaded page images

 
 # How to use Classic:
 
- Linux/Mac:
  - Open a new terminal
  - Clone this repo (`git clone https://github.com/NamesJoeyWheeler/PearsonDL.git`)
  - `cd` into the repo folder (`cd PearsonDL`)
    - Run the downloader as so and follow the instructions:
      - `python3 PearsonDL_Classic.py` or
      - `./PearsonDL_Classic.py`

- Windows:
  - Open a new CMD or PowerShell window
  - Clone this repo (`git clone https://github.com/NamesJoeyWheeler/PearsonDL.git`)
  - `cd` into the repo folder (`cd PearsonDL`)
    - Run the downloader as so and follow the instructions:
      - `python3 PearsonDL_Classic.py` or
      - `./PearsonDL_Classic.py`

- You should be able to find out how many pages the book has by going onto the last page of the book on the Pearson site (or viewing the manifest link).

- It will now download the pages into a folder named after the ID which is in the `Pearson Books` folder.


# How to get cookie for downloading:

- Login to the Pearson website.

- Open up developer tools and go to the `network` tab.

- Open the book on Pearson.

- Now keep an eye out in developer tools for something starting with 'manifest?password'. Click on it, then look for the 'Request Header'.

- After you've found the 'Request Header', look for 'Cookie'. Once you found it, copy the value.

![Picture showing where the cookie is](https://i.imgur.com/c74GyW8.jpg)

- Next, open up PearsonDL.py or PearsonDL_Classic.py (depends on what you want to use) in a text editor. Look for a line containing `opener.addheaders = [('Cookie', 'ADD COOKIE VALUE HERE')]`.

- Once you find it, edit 'ADD COOKIE VALUE HERE' with the cookie value you copied earlier. Save it, then it should work.


# How to get product number and book ID (PearsonDL):

- Login to the Pearson website.

- Open up developer tools and go to the `network` tab.

- Open the book on Pearson.

- Now keep an eye out in developer tools for something starting with 'manifest?password'. Copy that link.

  - The link should look something like this:

  - `https://plus.pearson.com/eplayer/pdfassets/prod1/<product number>/<book id>/manifest?password=&isCheckPsd=false&form=true`
  
![Picture showing where the link is](https://i.imgur.com/SazUx49.jpg)

- Now copy the id between 'prod1/' and '/manifest'. You can now use this in PearsonDL!


# How to get product number and book ID (PearsonDL Classic):

- Login to the Pearson website.

- Open up developer tools and go to the `network` tab.

- Open the book on Pearson.

- Now keep an eye out in developer tools for something starting with 'manifest?password'. Copy that link.

  - The link should look something like this:

  - `https://plus.pearson.com/eplayer/pdfassets/prod1/<product number>/<book id>/manifest?password=&isCheckPsd=false&form=true`
 
![Picture showing where the link is](https://i.imgur.com/SazUx49.jpg)
 
- Now copy the product number between 'prod1/' and before the book id, then copy the book id after the product number and before '/manifest'. You can now use this in PearsonDL Classic!
