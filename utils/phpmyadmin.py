import httpx
from bs4 import BeautifulSoup


def make_cache() -> list:
    release_list = []
    release_page = httpx.get("https://www.phpmyadmin.net/downloads/").content
    release_page = BeautifulSoup(release_page, "html.parser")
    releases_download_table = release_page.find_all("table", class_="table-condensed")
    for release in releases_download_table:
        this_version_dl_list = release.find("tbody").find_all("tr")
        for resource in this_version_dl_list:
            if ".tar.gz" in resource.text and "all-languages" in resource.text:
                if "snapshot" not in resource.text and "latest" not in resource.text:
                    download_metadata = resource.find_all("td")[0].find("a")
                    print(download_metadata)
                    url = download_metadata["href"]
                    version = download_metadata.text.replace("phpMyAdmin-", "").replace("-all-languages.tar.gz", "")
                    sha256 = download_metadata["data-sha256"]
                    release_list.append({"version": version, "url": url, "sha256": sha256})
    return release_list
