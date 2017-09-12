__author__ = 'GastonLucero'

from clases.Reader import Reader


def main():
    symbols = ["LTC", "USD", "EUR", "ARS"]

    reader = Reader()
    reader.write_js_array_files(symbols)


if __name__ == "__main__":
    main()
