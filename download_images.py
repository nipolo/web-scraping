from file_downloader import FileDownloader


with open('io-data/download-logger.txt', 'a') as log_file:
    fileDownLoader = FileDownloader(file_with_urls='t-shirt-links.txt', logger=log_file)
    # fileDownLoader = FileDownloader(file_with_urls='1.txt')
    fileDownLoader.download_files()

