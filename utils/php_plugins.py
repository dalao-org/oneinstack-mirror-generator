import time

import httpx
from bs4 import BeautifulSoup

MAX_TRIES = 50
ALLOWED_NUMBER_OF_VERSIONS = 3
BLACKLIST_WORD = ["alpha", "beta", "rc", "test"]


def make_cache(package_name: str, file_prefix: str) -> list:
    tried = 0
    while tried < MAX_TRIES:
        try:
            resource_list = []
            url = f"https://pecl.php.net/package/{package_name}"
            soup = BeautifulSoup(httpx.get(url).text, "html.parser")
            for a in soup.find_all("a"):
                if a.text.startswith(f"{file_prefix}-") and a.text.endswith(".tgz"):
                    if any(word in a.text for word in BLACKLIST_WORD):
                        continue
                    resource_list.append({
                        "version": a.text.replace(f"{file_prefix}-", "").replace(".tgz", ""),
                        "url": f"https://pecl.php.net" + a["href"] if a["href"].startswith("/") else a["href"],
                        "file_name": a.text
                    })
            return resource_list[:ALLOWED_NUMBER_OF_VERSIONS]
        except httpx.ReadTimeout:
            tried += 1
            print(f"Retrying to download PHP plugin {package_name}: {tried}/{MAX_TRIES}")
            time.sleep(5)
    print(f"pcel.php.net is down. Failed to fetch {package_name}.")
    return []
