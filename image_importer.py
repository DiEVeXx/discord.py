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

# GARBAGEEEEEEEEEEEEEEEEEEEEEE
import random
import re

import requests
from utils.color_logger import *
logger = colorlog.getLogger("ImageImporter")
request_one = None
request_two = None


def get_videos(html, protocol, _type):
    global request_two
    urls = []
    logger.info(html)
    all_urls = re.findall(r'href=\"\/[0-9]+\"', html, flags=re.IGNORECASE | re.MULTILINE | re.UNICODE)
    logger.info(f'{all_urls}')
    for url in all_urls:
        u = url.split('/')
        u2 = u[1].split('"')[0]
        urls.append('https://es.redtube.com/' + u2)
        logger.info('Added: https://es.redtube.com/'+u2)
    # TODO QUITAR DUPLICADOS EN LISTA urls
    urls = list(dict.fromkeys(urls))
    if len(urls) > 0:
        video = urls[random.randint(0, len(urls) - 1)]
        logger.info('Chosen video: {}'.format(video))
        request_two = requests.get(video, hooks=dict(response=update_session))
        return get_media_url_in_text(request_two.text, protocol, _type), video
    return


def get_media_url_in_text(html, protocol, _type):
    urls = []
    if _type == 'gif':
        all_urls = re.findall(r'((http\:|https\:)?\/\/[^"\' ]*?(\.(gif)(\?*)*))', html, flags=re.IGNORECASE | re.MULTILINE | re.UNICODE)
    else:
        all_urls = re.findall(r'((http\:|https\:)?\/\/[^"\' ]*?(\.(mp4)))', html, flags=re.IGNORECASE | re.MULTILINE | re.UNICODE)

    logger.info("mp4's found:{}\n{}".format(len(all_urls), all_urls))
    for url in all_urls:
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
def update_session(r, *args, **kwargs):
    global request_one, request_two
    request_one = r.text
    request_two = r.text


def get_images_from_url(url, _type='video'):
    protocol = url.split('/')[0]
    logger.info('Looking in {}'.format(url))
    request_one = requests.get(url, hooks=dict(response=update_session))
    logger.info('Content{}'.format(request_one.content))
    logger.info('Initial search {}'.format(request_one.text))
    return get_videos(request_one.text, protocol, _type)
