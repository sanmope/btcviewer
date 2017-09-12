__author__ = 'GastonLucero'

import urllib2
import json
import os
import time


class Scraper(object):

    def __init__(self, data_file_name, symbols):
        self.count = 0
        self.data_file_name = data_file_name
        self.symbols = symbols
        self.bitinka_api = 'https://www.bitinka.pe/api/apinka/ticker?format=json'
        self.data_file_path = self._get_file_path(self.data_file_name)
        self._init_file(self.data_file_path)

    def scrap(self):
        json_data = self._get_api_data()
        self._first_append_in_file(json_data, self.data_file_path)
        self._log_count()

        while True:
            json_data = self._get_api_data()
            self._append_in_file(json_data, self.data_file_path)
            self._log_count()

    def _get_api_data(self):
        json_data = self._get_json_data(self.bitinka_api)
        json_data = self._filter_json_data(json_data, self.symbols)
        return json_data

    def _log_count(self):
        self.count += 1
        print('{0} records scraped'.format(self.count))

    @staticmethod
    def _append_in_file(json_data, data_file_path):
        with(open(data_file_path, 'a+')) as f:
            f.seek(-2, os.SEEK_END)
            # Remove two last } in file
            f.truncate()
            f.write(',' + json.dumps(json_data)[1:-1] + '}}')

    @staticmethod
    def _first_append_in_file(json_data, data_file_path):
        with(open(data_file_path, 'a+')) as f:
            f.seek(-2, os.SEEK_END)
            # Remove two last } in file
            f.truncate()
            f.write(json.dumps(json_data)[1:-1] + '}}')

    @staticmethod
    def _get_json_data(api):
        response = urllib2.urlopen(api)
        actual_epoch_time = int(time.time())
        response = response.read()
        json_data = json.loads(response)
        json_data['time'] = actual_epoch_time
        return json_data

    @staticmethod
    def _filter_json_data(json_data, symbols):
        json_filtered = dict()
        json_filtered[json_data['time']] = dict()
        for symbol in symbols:
            json_filtered[json_data['time']][symbol] = json_data[symbol]
        return json_filtered

    @staticmethod
    def _get_file_path(file_name):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)
        while os.path.exists(file_path):
            file_path += '1'
        return file_path

    @staticmethod
    def _init_file(file_path):
        with(open(file_path, 'w')) as f:
            f.write('{"data":{}}')
