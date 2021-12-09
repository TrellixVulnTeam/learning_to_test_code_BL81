import os
from typing import Dict, List
import requests
import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import pandas as pd


ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

class Scraper:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.root_dir = ROOT_DIR
        
    def download(self, url):
        """
        Downloads a file given an URL and puts it in the folder `self.root_dir`
        """
        # if path doesn't exist, make that path dir
        if not os.path.isdir(self.root_dir):
            os.makedirs(self.root_dir)
        # download the body of response by chunk, not immediately
        response = requests.get(url, stream=True)
        # get the total file size
        file_size = int(response.headers.get("Content-Length", 0))
        # get the file name
        filename = os.path.join(self.root_dir, url.split("/")[-1])
        # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
        progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as f:
            for data in progress.iterable:
                # write data read to the file
                f.write(data)
                # update the progress bar manually
                progress.update(len(data))
                
    def get_all_images(self):
        """
        Returns a list of image URLs from Naturalist exported CSV
        """
        data = pd.read_csv(self.csv_path)
        return data[]
            
    def main(self):
        # get all image URLs
        imgs = self.get_all_images(self.csv_path)
        for img in imgs:
            # for each image, download it
            self.download(img, ROOT_DIR)
            
    def __str__(self):
        return str(self.csv_path)

if __name__ == "__main__":
    scraper = Scraper("/home/batman/Desktop/py/automate_boring_stuff/naturalist/observations-203332.csv")
    
    