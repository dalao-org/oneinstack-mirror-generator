import httpx
from bs4 import BeautifulSoup

ALLOWED_NUMBER_OF_RELEASES = 10


def make_cache() -> list:
    release_list = []
    url = "https://ftp.postgresql.org/pub/source/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, "html.parser").find("pre")
    versions = soup.find_all("a")
    version_num_list = []
    for version in versions:
        if any(s for s in ["..", "beta", "rc"] if s in version.text):
            continue
        try:
            version_text = float(version.text.replace("/", "").replace("v", ""))
            version_num_list.append(version_text)
        except ValueError:
            continue
    version_num_list = sorted(version_num_list, reverse=True)[:ALLOWED_NUMBER_OF_RELEASES]
    for version in version_num_list:
        release_list.append({
            "url": f"https://ftp.postgresql.org/pub/source/v{version}/postgresql-{version}.tar.gz",
            "file_name": f"postgresql-{version}.tar.gz",
            "md5": f"https://ftp.postgresql.org/pub/source/v{version}/postgresql-{version}.tar.gz.md5",
            "sha256": f"https://ftp.postgresql.org/pub/source/v{version}/postgresql-{version}.tar.gz.sha256",
        })
    return release_list
