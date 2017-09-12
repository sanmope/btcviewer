__author__ = 'GastonLucero'

from clases.Scraper import Scraper

def main():
    data_file_name = 'data.json'
    symbols = ["LTC", "USD", "EUR", "ARS"]

    scraper = Scraper(data_file_name, symbols)
    scraper.scrap()

if __name__ == "__main__":
    main()
