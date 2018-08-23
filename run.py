from urllib.request import urlopen
from lxml import etree

class MusicSite():
    songlist = []

    def __init__(self, url, XPATHsong, XPATHauthor):
        self.url = url
        self.XPATHsong = XPATHsong
        self.XPATHauthor = XPATHauthor
        self.response = urlopen(url)
        self.htmlparser = etree.HTMLParser()
        self.tree = etree.parse(self.response, self.htmlparser)

    def getSongs(self):
        results = self.tree.xpath(self.XPATHsong)
        for result in results:
            print(result.text)

    def getSongs(self):
        results = self.tree.xpath(self.XPATHsong)
        for result in results:
            # print(result.text)
            MusicSite.songlist.append(result.text)

    def getAuthors(self):
        results = self.tree.xpath(self.XPATHauthor)
        i = 0
        for result in results:
            # print(result.text)
            MusicSite.songlist[i] = MusicSite.songlist[i] + " " + result.text
            i = i + 1

    def getSearchQueries(self):
        for song in self.songlist:
            print(song)

def main():

    print("start")
    musicsite = MusicSite("https://www.ranker.com/list/best-indie-songs-2018/ranker-music",
                          "//*[contains(@class, 'listItem__title')]",
                          "//*[contains(@class, 'listItem__properties black default')]")
    musicsite.getSongs()
    musicsite.getAuthors()
    musicsite.getSearchQueries()

    # url = "https://www.ranker.com/list/best-indie-songs-2018/ranker-music"
    # response = urlopen(url)
    # htmlparser = etree.HTMLParser()
    # tree = etree.parse(response, htmlparser)
    #
    # results = tree.xpath("//*[contains(@class, 'listItem__title')]")
    # for result in results:
    #     print(result.text)


if __name__ == "__main__":
    main()
