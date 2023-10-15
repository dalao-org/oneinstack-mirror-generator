import httpx
from bs4 import BeautifulSoup


def make_cache() -> list:
    url = "https://ftp.pureftpd.org/public/public/pure-ftpd/releases/"
    soup = BeautifulSoup(httpx.get(url).text, "html.parser")
    resource_list = []
    for a in soup.find_all("a", href=True):
        if a["href"].endswith(".tar.gz") and a["href"].startswith("pure-ftpd-"):
            resource_list.append({
                "url": url + a["href"],
                "file_name": a["href"]
            })
    return resource_list
