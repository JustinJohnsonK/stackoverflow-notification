from robobrowser import RoboBrowser

from app.login import Login
from app.scrape import ScrapeData
from app.notify import DisplayNotification

# url = "https://stackoverflow.com/"
#
# uClient = urlopen(url)
# page_html = uClient.read()
# uClient.close()
# page_soup = soup(page_html, "html.parser")
#
# container = page_soup.findAll("div", {"class": "-rep js-header-rep"})
# print(container)
# print(len(container))

rb = RoboBrowser()
login = Login(rb)
data = ScrapeData(rb)
reputation = data.scrape()

print(reputation)

notification = DisplayNotification(reputation)

# rb.open("https://stackoverflow.com/users/login")
# form = rb.get_form(id="login-form")
# print(config.stackemail)
# form['email'].value = config.stackemail
# form['password'].value = config.stackpassword
# rb.submit_form(form)

# src = str(rb.parsed())

# page_soup = soup(src, "html.parser")
# container = page_soup.findAll("div", {"class": "-rep js-header-rep"})
# print(container)
# print(len(container))