import httpx


def make_cache():
    release_list = []

    url = "https://api.github.com/repos/openssl/openssl/releases"
    non_pre_release = [r for r in httpx.get(url).json() if not r["prerelease"]]
    for release in non_pre_release:
        version_name = release["name"].lower().replace("openssl ", "")
        for asset in release["assets"]:
            if asset["name"].endswith(".tar.gz"):
                release_list.append({
                    "version": version_name,
                    "url": asset["browser_download_url"],
                    "sha256": asset["browser_download_url"]+".sha256",
                    "sha1": asset["browser_download_url"] + ".sha1",
                    "pgp": asset["browser_download_url"]+".asc"
                })
                break
    return release_list
