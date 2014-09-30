__author__ = 'weirded'

import json
import urllib2
import urllib

save_dir = "T:\\slvp\\"
api_url = 'https://api.vk.com/method/'
group_id = '-60432911'
album_id = 'wall'
count = '1000'
offset = 0


def get_photo_links(group_id, album_id):
    url = api_url + 'photos.get?' + \
        'owner_id=' + group_id + \
        '&album_id=' + album_id + \
        '&count=' + count + \
        '&offset=' + str(offset) + \
        '&rev=1&extended=0'
    print url
    # url = 'https://api.vk.com/method/photos.get?owner_id=-60432911&album_id=wall&count=1000&offset=0&rev=1&extended=0'
    response = urllib2.urlopen(url)
    return json.loads(response.read())['response']


for offset in range(0, 15000, 1000):
    i = offset
    for photo in get_photo_links(group_id, album_id):
        i += 1
        if 'src_xxbig' in photo:
            photo_url = photo['src_xxbig']
        elif 'src_xbig' in photo:
            photo_url = photo['src_xbig']
        elif 'src_big' in photo:
            photo_url = photo['src_big']
        else:
            continue
        path = save_dir + "wall_" + str(i) + '.jpg'
        try:
            urllib.urlretrieve(photo_url, path)
            print path
        except urllib.ContentTooShortError:
            print "Oh"
        except IOError:
            print "shit"
