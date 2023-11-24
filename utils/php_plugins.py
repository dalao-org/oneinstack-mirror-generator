import time
from typing import Tuple, List, Dict, Any
from base_logger import logger
import httpx
from bs4 import BeautifulSoup

MAX_TRIES = 50
BLACKLIST_WORD = ["alpha", "beta", "rc", "test"]


def make_cache(package_name: str, file_prefix: str, allow_unstable_version: bool = False,
               latest_meta_name: str = None) \
                -> tuple[list[dict[str, str | Any]], dict[str, str] | None] | list[Any]:
    tried = 0
    while tried < MAX_TRIES:
        try:
            resource_list = []
            url = f"https://pecl.php.net/package/{package_name}"
            soup = BeautifulSoup(httpx.get(url).text, "html.parser")
            for a in soup.find_all("a"):
                if a.text.startswith(f"{file_prefix}-") and a.text.endswith(".tgz"):
                    if not allow_unstable_version:
                        if any(word in a.text.lower() for word in BLACKLIST_WORD):
                            continue
                    resource_list.append({
                        "version": a.text.replace(f"{file_prefix}-", "").replace(".tgz", ""),
                        "url": f"https://pecl.php.net" + a["href"] if a["href"].startswith("/") else a["href"],
                        "file_name": a.text
                    })
            if latest_meta_name:
                latest_meta = {"version_file_name": latest_meta_name, "version": resource_list[0]["version"]}
            else:
                latest_meta = None
            return resource_list, latest_meta
        except httpx.ReadTimeout:
            tried += 1
            logger.exception(f"Retrying to download PHP plugin {package_name}: {tried}/{MAX_TRIES}")
            if tried >= 0.6 * MAX_TRIES:
                time.sleep(30)
            else:
                time.sleep(5)
    logger.error(f"pcel.php.net is down. Failed to fetch {package_name}.")
    return []
