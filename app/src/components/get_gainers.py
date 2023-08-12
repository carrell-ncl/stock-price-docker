import lxml.html
import requests


def get_gainers(url: str = "https://finance.yahoo.com/gainers") -> list[str]:
    """Scrapes the top 5 gainers from Yahoo Finance website

    Args:
        url (str, optional): https://finance.yahoo.com/gainers

    Returns:
        list[str]: Top 5 stocks
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"
    }
    ytext = requests.get(url, headers=headers).text
    yroot = lxml.html.fromstring(ytext)
    stocks = list()
    names = list()
    for x in yroot.xpath('//*[@id="fin-scr-res-table"]//a'):
        stocks.append(x.attrib["href"].split("/")[-1].split("?")[0])
        names.append(x.attrib["title"].split("/")[-1].split("?")[0])
    return names[:5], stocks[:5]
