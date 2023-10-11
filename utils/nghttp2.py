import httpx


def make_cache() -> list:
    release_list = []
    url = "https://api.github.com/repos/nghttp2/nghttp2/releases"
    response = httpx.get(url).json()
    non_pre_releases = [release for release in response if not release["prerelease"]][:10]

    for release in non_pre_releases:
        for asset in release["assets"]:
            if "tar.gz" in asset["name"]:
                release_list.append({
                    "url": asset["browser_download_url"],
                    "file_name": asset["name"],
                    "gpg": asset["browser_download_url"] + ".asc",
                    "md5": "/".join(asset["browser_download_url"].split("/")[:-1]) + "/checksums.txt"
                })
    return release_list
