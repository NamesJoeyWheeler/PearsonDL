# PearsonDL

A Python script that downloads books from the Pearson website in (multiple) PNG files and/or a single PDF file.

# Disclaimer

Only use this for books you LEGALLY own. We do not condone, promote or tolerate the use of this script for illegal purposes.

# What is needed:

- Python 3.x (tested with `3.6` and `3.7`)
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



# How to get book ID:

- Login to the Pearson website.

- Open up developer tools and go to the `network` tab.

- Open the book on Pearson.

- Now keep an eye out in developer tools for something starting with 'manifest?password'. Copy that link.

  - The link should look something like this:

  - `https://d38l3k3yaet8r2.cloudfront.net/resources/products/epubs/generated/<id>/foxit-assets/manifest?password=&isCheckPsd=false&form=true`
  
- Now copy the id between '/generated/' and '/foxit-assets'. You can now use this ID in PearsonDL!

