from requests_html import HTMLSession


class TitlesISBN:
    def __init__(self, title):
        try:
            self.title = title.replace(" ", "%20")
            self.link = ('https://www.abebooks.co.uk/servlet/SearchResults?cm_sp=SearchF-_-TopNavISS-_-Results&kn='
                         + title
                         + '&sts=t')
            session = HTMLSession()
            r = session.get(self.link)
            result_detail = r.html.find('div.result-detail', first=True)
            isbn_uncut = result_detail.find('span.pl-md', first=True).text
            self.isbn = isbn_uncut.split(" ")[1]
        except Exception as e:
            print("AbeBooks parsing failed: " + e)
            self.link = "Error"
            self.isbn = "Error"

