__author__ = 'GastonLucero'

from clases.Reader import Reader


def main():
    try:
        file_name = 'data.json'
        file_path = Reader.get_data_file_path(file_name)
        Reader.load_json_from_file(file_path)
        print('Valid Json file.')
        return 1

    except Exception as e:
        print('INVALID Json file.')
        return 0



if __name__ == "__main__":
    main()
