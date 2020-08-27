from bs4 import BeautifulSoup


def print_soup():
    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    print(soup.prettify())
