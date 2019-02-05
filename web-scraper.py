from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests
from file_downloader import FileDownloader

fileDownLoader = FileDownloader()
for page_index in range(1, 110):
    with open('log.txt', 'a') as log_file:
        try:
            with open('t-shirt-links.txt', 'a') as t_shirt_links:
                t_shirt_links.write('Starting to process page {0}\n'.format(page_index))
                headers = {
                    'user-agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
                }
                try:
                    pages_with_data = requests.get('https://www.gearbest.com/men-s-t-shirts-c_11926/{0}.html?page_size=120'
                                                   .format(str(page_index)), headers=headers)

                    # r = requests.get('https://www.threadless.com/catalog/type,guys/style,tees/page,{0}'.format(page_index))

                except RequestException as e:
                    print('Error in page {0}'.format(str(page_index)))

                links_parser = BeautifulSoup(pages_with_data.text)
                results = links_parser.find_all('a', {'class', 'gbGoodsItem_thumb'})

                for index, item in enumerate(results):
                    try:
                        page_with_image = requests.get(item.attrs['href'], headers=headers)
                        image_parser = BeautifulSoup(page_with_image.text)
                        image_url = image_parser.find('div', {'class': 'goodsIntro_largeImgWrap'}).find('img').attrs['data-zoom']
                        # fileDownLoader.download_file(image_url, '{0}_{1}'.format(str(page_index),str(index+1)))
                        t_shirt_links.write(image_url+'\n')
                    except Exception as ex:
                        log_file.write('Error in page number {0} item {1}: '.format(page_index, index) + str(ex) + '\n')
        except IOError as io_exeption:
            log_file.write('Error in page number {0}: '.format(page_index) + str(io_exeption) + '\n')
