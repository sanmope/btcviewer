__author__ = 'GastonLucero'

import os
import json
from helpers.singleton import Singleton


class Reader(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.json_data = {"data": {}}
        self.sorted_data_array = []
        self.json_data_folder_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'json_history')
        self.js_arrays_folder_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'data', 'javascript_arrays')

    def sort_data_by_timestamp(self):
        for timestamp in self.json_data['data']:
            self.sorted_data_array.append([timestamp, self.json_data['data'][timestamp]])
        self.sorted_data_array.sort()

    def read_data_folder(self):
        for filename in os.listdir(self.json_data_folder_path ):
            print("Loading Json data from file: " + filename)
            file_path = os.path.join(self.json_data_folder_path , filename)
            file_data = self.load_json_from_file(file_path)
            self.json_data['data'].update(file_data['data'])

    def write_js_array_files(self, symbols):
        self.read_data_folder()
        self.sort_data_by_timestamp()
        for symbol in symbols:
            js_file_path = os.path.join(self.js_arrays_folder_path, 'array_{0}.js'.format(symbol))
            self._init_js_file(js_file_path)
            self._write_js_array_file(js_file_path, symbol)

    def _write_js_array_file(self, js_file_path, symbol):
        data = self.sorted_data_array[:1][0]
        append_string = self._get_js_append_string(data, symbol)
        self._append_in_js_file(append_string, js_file_path)
        for data in self.sorted_data_array[1:]:
            append_string = self._get_js_append_string(data, symbol)
            append_string = ',' + append_string
            self._append_in_js_file(append_string, js_file_path)

    @staticmethod
    def _get_js_append_string(data, symbol):
        timestamp = int(data[0])*1000
        sellvalue = data[1][symbol]['bid']
        buyvalue = data[1][symbol]['ask']
        volume = data[1][symbol]["volumen24hours"]["BTC"]
        result = '{"date": new Date(' + str(timestamp) + '), "sellvalue":' + str(sellvalue) + \
                 ', "buyvalue":' + str(buyvalue) + ', "volume":' + str(volume) + '}'
        return result

    @staticmethod
    def _append_in_js_file(string_data, js_file_path):
        with(open(js_file_path, 'a+')) as f:
            f.seek(-2, os.SEEK_END)
            # Remove two last ]; in file
            f.truncate()
            f.write(string_data + '];')

    @staticmethod
    def load_json_from_file(file_path):
        with open(file_path, 'r+') as f:
            json_data = json.load(f)
        return json_data

    @staticmethod
    def get_data_file_path(file_name):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)
        return file_path

    @staticmethod
    def _init_js_file(file_path):
        print('Initializing {0} js array file'.format(file_path))
        with(open(file_path, 'w')) as f:
            f.write('var data_array = [];')