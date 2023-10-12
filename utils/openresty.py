import httpx


ALLOWED_NUMBER_OF_RELEASES = 3


def make_cache() -> list:
    release_list = []
    url = "https://api.github.com/repos/openresty/openresty/releases"
    response = httpx.get(url).json()
    non_pre_releases = [release for release in response if not release["prerelease"]]
    non_pre_releases = [r["name"].replace("v", "") for r in non_pre_releases[:ALLOWED_NUMBER_OF_RELEASES]]
    for release in non_pre_releases:
        release_list.append({
            "version": release,
            "file_name": f"openresty-{release}.tar.gz",
            "url": f"https://openresty.org/download/openresty-{release}.tar.gz",
            "pgp": f"https://openresty.org/download/openresty-{release}.tar.gz.asc"
        })
    return release_list
