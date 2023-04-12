from requests_html import HTMLSession


class ParserAbe:
    def __init__(self, isbn):
        try:
            self.isbn = isbn
            self.link = (f'https://www.abebooks.co.uk/servlet/SearchResults?cm_sp=SearchF-_-topnav-_-Results&kn='
                         + isbn
                         + '&sts=t')
            session = HTMLSession()
            r = session.get(self.link)
            info = r.html.find('div.result-data', first=True)
            price_group = r.html.find('div.item-price-group', first=True)
            self.title = info.find('h2.title', first=True).text
            self.author = info.find('p.author', first=True).text
            self.price_used = price_group.find('p.item-price', first=True).text

        except Exception as e:
            print(f"AbeBooks parsing failed: {e}")
            print(self.link)
            self.title = "Error"
            self.author = "Error"
            self.price_used = "Error"
            self.link = "Error"
