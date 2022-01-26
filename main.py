from urllib.error import HTTPError
from urllib.request import urlretrieve
from xml.etree.ElementTree import tostring
url = "https://disney-studios-awards.s3.amazonaws.com/luca/books/flipH45pEt23wR/files/mobile/"
for x in range (1, 181) :
    imageURL = url + str(x) + ".jpg"
    #print (imageURL)
    try:
        urlretrieve(imageURL, str(x) + ".jpg")
    except FileNotFoundError as err:
        print(err)   # something wrong with local path
    except HTTPError as err:
        print(err)  # something wrong with url