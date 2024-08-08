import requests
from bs4 import BeautifulSoup
import csv

# URL of the page you want to scrape
url = 'https://spiderum.com'

# Fetch the HTML content
response = requests.get(url)
html_doc = response.text  # Get the HTML content as a string

# Parse the HTML
soup = BeautifulSoup(html_doc, 'html.parser')
links = soup.find_all('a')

# Open a CSV file for writing
with open('links.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['URL', 'Text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the link data
    for link in links:
        writer.writerow({'URL': link.get('href'), 'Text': link.text})
