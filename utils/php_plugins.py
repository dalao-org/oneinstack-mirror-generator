import httpx
from bs4 import BeautifulSoup

MAX_TRIES = 10
ALLOWED_NUMBER_OF_VERSIONS = 3


def make_cache(package_name: str, file_prefix: str) -> list:
    tried = 0
    while tried < MAX_TRIES:
        try:
            resource_list = []
            url = f"https://pecl.php.net/package/{package_name}"
            soup = BeautifulSoup(httpx.get(url).text, "html.parser")
            for a in soup.find_all("a"):
                if a.text.startswith(f"{file_prefix}-") and a.text.endswith(".tgz"):
                    resource_list.append({
                        "version": a.text.replace(f"{file_prefix}-", "").replace(".tgz", ""),
                        "url": f"https://pecl.php.net" + a["href"] if a["href"].startswith("/") else a["href"],
                    })
            return resource_list[:ALLOWED_NUMBER_OF_VERSIONS]
        except httpx.ReadTimeout:
            tried += 1
            print(f"Retrying {tried}/{MAX_TRIES}")
    print(f"pcel.php.net is down. Failed to fetch {package_name}.")
    return []
