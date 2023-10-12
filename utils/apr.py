import httpx
from bs4 import BeautifulSoup

ALLOWED_NUMBER_OF_VERSIONS = 3
BLACK_LIST_WORD = ["alpha", "beta", "deps", "rc", "win32"]


def make_cache() -> list:
    resource_list = []
    url = "https://archive.apache.org/dist/apr/"
    soup = BeautifulSoup(httpx.get(url).text, "html.parser")
    file_list = []
    for a in soup.find_all("a"):
        if a.text.startswith("apr-") and a.text.endswith(".tar.gz"):
            if "apr-util" not in a.text and "apr-iconv" not in a.text:
                if not any(word for word in BLACK_LIST_WORD if word in a.text):
                    file_list.append(a.text.replace(".tar.gz", "").replace("apr-", ""))
    file_list.sort(key=lambda x: [int(c) for c in x.split(".")])
    file_list.reverse()
    file_list = file_list[:ALLOWED_NUMBER_OF_VERSIONS]
    for file in file_list:
        resource_list.append(
            {
                "url": f"https://archive.apache.org/dist/apr/apr-{file}.tar.gz",
                "file_name": f"apr-{file}.tar.gz",
                "version": file,
                "gpg": f"https://archive.apache.org/dist/apr/apr-{file}.tar.gz.asc",
                "sha256": f"https://archive.apache.org/dist/apr/apr-{file}.tar.gz.sha256",
            }
        )

    file_list = []
    for a in soup.find_all("a"):
        if a.text.startswith("apr-util") and a.text.endswith(".tar.gz"):
            if not any(word for word in BLACK_LIST_WORD if word in a.text):
                file_list.append(a.text.replace(".tar.gz", "").replace("apr-util-", ""))
    file_list.sort(key=lambda x: [int(c) for c in x.split(".")])
    file_list.reverse()
    file_list = file_list[:ALLOWED_NUMBER_OF_VERSIONS]
    for file in file_list:
        resource_list.append(
            {
                "url": f"https://archive.apache.org/dist/apr/apr-util-{file}.tar.gz",
                "file_name": f"apr-{file}.tar.gz",
                "version": file,
                "gpg": f"https://archive.apache.org/dist/apr/apr-util-{file}.tar.gz.asc",
                "sha256": f"https://archive.apache.org/dist/apr/apr-util-{file}.tar.gz.sha256",
            }
        )
    return resource_list
