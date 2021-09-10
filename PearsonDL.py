#!/usr/bin/env python3

from urllib import request
from argparse import ArgumentParser
from time import time
from uuid import UUID
from multiprocessing import Process, Pool, cpu_count
from os import path, makedirs, sep, remove
from sys import exit
from glob import glob

def main():
    parser = ArgumentParser()
    parser.add_argument('-p', '--pages', type=int, help='The number of pages in this book.')
    parser.add_argument('-i', '--id', type=str, help='This book\'s product number and ID.')
    parser.add_argument('-g', "--generate_pdf", action='store_true', help='Generate a PDF from the downloaded images.')
    parser.add_argument('-r', "--remove_png", action='store_true', help='Remove the downloaded PNG files after PDF generation.')
    parser.add_argument('-v', "--verbose", action='store_true', help='Show verbose output.')
    args = parser.parse_args()

    if not args.id:
        print("Please provide a value for this book's product number and ID!")
        exit(1)
    elif not args.pages:
        print("Please provide a value for the number of pages in this book!")
        exit(1)
    # End if/else block

    print("PearsonDL")
    print("Developed by NamesJoeyWheeler, FurryLovingMcNugget, and cdchris12")
    print("---------------------------------------------------")

    _id = args.id
    pages = args.pages

    if not path.isdir(path.join('Pearson Books', _id)):
        directory = _id
        parent_dir = 'Pearson Books'
        _path = path.join(parent_dir, directory)
        makedirs(_path)
    # End if

    print("Downloading page images...")
    pool = Pool(cpu_count())

    # Create a process for each page
    for i in range(0, pages):
        pool.apply_async(get_files, args=(_id, i, args.verbose,))
    # End for

    pool.close()
    pool.join()
    print("Page downloads complete!")

    if args.generate_pdf:
        try:
            from PIL import Image
        except ModuleNotFoundError:
            print("Python Imaging Library not installed, unable to generate PDF!")
            exit(1)
        # End try/except block

        print('Generating a PDF... (This may take a while)')
        # Grab list of created image files and sort them numerically
        image_list = sorted(glob(path.join('Pearson Books', _id, "*.png")), key = lambda x: int(x.split(sep)[2].split(".")[0]))

        im0 = Image.open(f'{image_list[0]}').convert('RGB')
        converted_list = []

        for i in range(1, len(image_list)):
            converted_list.append(Image.open(f'{image_list[i]}').convert('RGB'))
        # End for

        im0.save(path.join('Pearson Books', _id, f'book.pdf'), save_all=True, append_images=converted_list, optimize=True)
        print("Generated a PDF!")

        if args.remove_png:
            print("Cleaning up downloaded PNG files...")
            for png in image_list:
                remove(png)
            # End for
            print("PNG files removed!")
        # End if
    # End if
# End def


def get_files(_id, page, verbose=False):
    pb = f'https://plus.pearson.com/eplayer/pdfassets/prod1/{_id}/pages/page{page}?password=&accessToken=null&formMode=true'
    opener = request.build_opener()
    opener.addheaders = [('ADD COOKIE HERE!')]
    request.install_opener(opener)
    request.urlretrieve(pb, f'Pearson Books/{_id}/{page}.png')

    if verbose: 
        print(f"Downloaded page {page+1}!")
    # End if
# End def

if __name__ == "__main__":
    start_time = time()
    main()
    print("--- Generated in %.4f seconds ---" % (time() - start_time))
# End if