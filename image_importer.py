#
#
# get_url_images_in_text()
#
# @param html - the html to extract urls of images from him.
# @param protocol - the protocol of the website, for append to urls that not start with protocol.
#
# @return list of imags url.
#
#
import re

import requests
from utils.color_logger import *

logger = colorlog.getLogger("ImageImporter")


def get_url_images_in_text(html, protocol):
    urls = []
    #all_urls = re.findall(r'((http\:|https\:)?\/\/[^"\' ]*?(\.(gif)(\?width=300)*|\.(mp4)))', html,  # videos y gifs
    all_urls = re.findall(r'((http\:|https\:)?\/\/[^"\' ]*?(\.(mp4)))', html,  # solo videos
                          flags=re.IGNORECASE | re.MULTILINE | re.UNICODE)
    logger.info("{}".format(all_urls))
    for url in all_urls:
        #if requests.get(url[0]).status_code != 403:  # Comprobar que no devuelve una imagen que al acceder da un 403
        if not url[0].startswith("http"):
            urls.append(protocol + url[0])
        else:
            urls.append(url[0])

    return urls


#
#
# get_images_from_url()
#
# @param url - the url for extract images url from him. 
#
# @return list of images url.
#
#
def get_images_from_url(url):
    protocol = url.split('/')[0]
    logger.info('Looking in {}'.format(url))
    resp = requests.get(url)
    return get_url_images_in_text(resp.text, protocol)
