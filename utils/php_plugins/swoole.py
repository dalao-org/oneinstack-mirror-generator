import httpx
from bs4 import BeautifulSoup

ALLOWED_NUMBER_OF_VERSIONS = 5
MAX_TRIES = 10


def make_cache() -> list:
    tried = 0
    while tried < MAX_TRIES:
        try:
            resource_list = []
            url = "https://pecl.php.net/package/swoole"
            soup = BeautifulSoup(httpx.get(url).text, "html.parser")
            for a in soup.find_all("a"):
                if a.text.startswith("swoole-") and a.text.endswith(".tgz") and "rc" not in a.text.lower():
                    resource_list.append({
                        "version": a.text.replace("swoole-", "").replace(".tgz", ""),
                        "url": f"https://pecl.php.net" + a["href"] if a["href"].startswith("/") else a["href"],
                    })
            return resource_list[:ALLOWED_NUMBER_OF_VERSIONS]
        except httpx.ReadTimeout:
            tried += 1
            print(f"Retrying {tried}/{MAX_TRIES}")
    print("pcel.php.net is down. Failed to fetch swoole versions.")
    return []
