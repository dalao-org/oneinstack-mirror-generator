def make_cache() -> list:
    resource_list = []
    url_list = ["https://www.sourceguardian.com/loaders/download/loaders.linux-x86_64.tar.gz",
                "https://www.sourceguardian.com/loaders/download/loaders.linux-armhf.tar.gz",
                "https://www.sourceguardian.com/loaders/download/loaders.linux-aarch64.tar.gz",
                "https://github.com/kmvan/x-prober/releases/latest/download/prober.php",
                "https://gist.githubusercontent.com/ck-on/4959032/raw/ocp.php"]
    for url in url_list:
        resource_list.append({
            "url": url,
            "file_name": url.split("/")[-1]
        })
    return resource_list
