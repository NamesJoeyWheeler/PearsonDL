#!/usr/bin/env python3

from urllib import request
from argparse import ArgumentParser
from time import time
from uuid import UUID
from multiprocessing import Process, Pool, cpu_count
from os import path, makedirs
from sys import exit
from glob import glob

def main():
    parser = ArgumentParser()
    parser.add_argument('-p', '--pages', type=int, help='The number of pages in this book.')
    parser.add_argument('-i', '--id', type=str, help='This book\'s ID.')
    parser.add_argument('-g', "--generate_pdf", action='store_true', help='Generate a PDF from the downloaded images.')
    args = parser.parse_args()

    if not args.id:
        print("Please provide a value for this book's ID!")
        exit(1)
    elif not args.pages:
        print("Please provide a value for the number of pages in this book!")
        exit(1)
    elif not is_valid_uuid(args.id):
        print("Please provide a valid UUID for this book's ID!")
        exit(1)
    # End if/else block

    print("PearsonDL")
    print("Developed by NamesJoeyWheeler, FurryLovingMcNugget, and cdchris12")
    print("---------------------------------------------------")

    _id = args.id
    pages = args.pages

    if not path.isdir(f'Pearson Books/{_id}'):
        directory = _id
        parent_dir = 'Pearson Books/'
        _path = path.join(parent_dir, directory)
        makedirs(_path)
    # End if

    pool = Pool(cpu_count())

    # Create a process for each page
    for i in range(0, pages):
        pool.apply_async(get_files, args=(_id, i,))
    # End for

    pool.close()
    pool.join()

    if args.generate_pdf:
        try:
            from PIL import Image
        except ModuleNotFoundError:
            print("Python Imaging Library not installed, unable to generate PDF!")
            exit(1)
        # End try/except block

        print('Generating a PDF! (This may take a while)')
        # Grab list of created image files and sort them numerically
        image_list = sorted(glob(f'Pearson Books/{_id}/*.png'), key = lambda x: int(x.split("/")[2].split(".")[0]))

        im0 = Image.open(f'{image_list[0]}').convert('RGB')
        converted_list = []

        for i in range(1, len(image_list)):
            converted_list.append(Image.open(f'{image_list[i]}').convert('RGB'))
        # End for

        im0.save(f'Pearson Books/{_id}/{_id}.pdf', save_all=True, append_images=converted_list, optimize=True)
        print("Generated a PDF!")
    # End if
# End def

def is_valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.

    Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}

    Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.

    Examples
    --------
    >>> is_valid_uuid('c9bf9e57-1685-4c89-bafb-ff5af830be8a')
    True
    >>> is_valid_uuid('c9bf9e58')
    False
    """
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    # End try/except block

    return str(uuid_obj).upper() == uuid_to_test
# End def

def get_files(_id, page):
    pb = f'https://d38l3k3yaet8r2.cloudfront.net/resources/products/epubs/generated/{_id}/foxit-assets/pages/page{page}?password=&accessToken=null&formMode=true'
    request.urlretrieve(pb, f'Pearson Books/{_id}/{page}.png')
    print(f"Downloaded page {page+1}!")
# End def

if __name__ == "__main__":
    start_time = time()
    main()
    print("--- Generated in %.4f seconds ---" % (time() - start_time))
# End if