#! python3

import bs4,requests, os

url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok= True)
ending = ''
while not url.endswith('#'):
    print('downloading the %s ...' %url)
    page = requests.get(url)
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text,'html.parser')
    image = soup.select('#comic img')
    if image == []:
        print('no image found')
    else:
        try:
            comicUrl = 'http:'+image[0].get('src')
            print('downloading image')
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('done')