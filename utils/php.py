import httpx
from bs4 import BeautifulSoup


def older_php_cache_maker() -> list:
    version_list = []
    php_release_page = httpx.get("https://www.php.net/releases/").content
    php_release_bs = BeautifulSoup(php_release_page, "html.parser")
    releases_bs_list = php_release_bs.find_all("li")
    for release_bs in releases_bs_list:
        if "(tar.gz)" in release_bs.text and "Download" not in release_bs.text:
            metadata = release_bs.text.split(" ")
            if len(metadata) == 4:
                version_num = metadata[1]
                sha256 = metadata[3].replace("\n", "")
                url = release_bs.find("a")["href"]
                if url.startswith("/"):
                    url = "https://www.php.net" + url
                version_list.append({"version": version_num, "url": url, "sha256": sha256,
                                     "file_name": url.split("/")[-1]})
    return version_list


def latest_php_cache_maker() -> list:
    version_list = []
    php_release_page = httpx.get("https://www.php.net/downloads.php").content
    php_release_bs = BeautifulSoup(php_release_page, "html.parser")
    releases_bs_list = php_release_bs.find_all("div", class_="content-box")
    for release_bs in releases_bs_list:
        resource_list = release_bs.find_all("li")
        for resource in resource_list:
            if ".tar.gz" in resource.text:
                version_num = resource.find("a").text.replace("php-", "").replace(".tar.gz", "")
                url = resource.find("a")["href"]
                sha256 = resource.find("span", class_="sha256").text
                if url.startswith("/"):
                    url = "https://www.php.net" + url
                version_list.append({"version": version_num, "url": url, "sha256": sha256,
                                     "file_name": url.split("/")[-1]})
    return version_list


def make_cache():
    return latest_php_cache_maker() + older_php_cache_maker()
