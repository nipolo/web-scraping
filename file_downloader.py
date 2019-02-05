import os
import wget
import urllib.request
import pathlib


class FileDownloader:

    def __init__(self, save_folder_name='downloads', file_with_urls='', logger=None):
        self.opener = urllib.request.build_opener()
        self.opener.addheaders = [('User-Agent',
                                   'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0')]
        urllib.request.install_opener(self.opener)

        current_dir = os.getcwd()
        self.destination_folder = os.path.join(current_dir, save_folder_name)
        self.file_with_urls = file_with_urls
        self.logger = logger

    def download_file(self, url, file_name = ''):
        original_file_path = wget.download(url, self.destination_folder)
        file_extension = pathlib.Path(original_file_path).suffix

        if file_name != '':
            renamed_file_path = os.path.join(os.path.dirname(original_file_path), file_name+file_extension)
            os.rename(original_file_path, renamed_file_path)

    def download_files(self):
        with open(self.file_with_urls, 'r') as urls_file:
            for index, url in enumerate(urls_file.readlines()):
                try:
                    self.download_file(url.replace('\n',''), str(index))
                except Exception as ex:
                    self.logger.writeline('Error processing image {0}: {1}'.format(url, str(ex)))
