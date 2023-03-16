# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import requests
from bs4 import BeautifulSoup

url = "https://planning.lichfielddc.gov.uk/online-applications/"
params = {"parish": "ELF"}

page = requests.get(url, params=params)

soup = BeautifulSoup(page.content, "html.parser")

# Find all the table rows containing planning applications
rows = soup.find_all("tr", {"class": "searchresult"})

for row in rows:
    # Extract the relevant data from each row
    application_number = row.find("td", {"class": "searchresultnumber"}).get_text().strip()
    application_date = row.find("td", {"class": "searchresultdate"}).get_text().strip()
    application_address = row.find("td", {"class": "searchresultaddress"}).get_text().strip()

    # Print out the data
    print(f"Application Number: {application_number}")
    print(f"Application Date: {application_date}")
    print(f"Application Address: {application_address}")
    print("\n")

