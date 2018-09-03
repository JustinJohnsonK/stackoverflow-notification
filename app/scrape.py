from bs4 import BeautifulSoup as soup

class ScrapeData(object):

    def __init__(self, arg):

        self.rb = arg
        self.src = str(self.rb.parsed())

    def scrape(self):

        page_soup = soup(self.src, "html.parser")
        container = page_soup.findAll("div", {"class": "-rep js-header-rep"})
        reputation = container[0].text

        return reputation