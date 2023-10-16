def make_cache() -> list:
    resource_list = []
    url_list = ["https://www.sourceguardian.com/loaders/download/loaders.linux-x86_64.tar.gz",
                "https://www.sourceguardian.com/loaders/download/loaders.linux-armhf.tar.gz",
                "https://www.sourceguardian.com/loaders/download/loaders.linux-aarch64.tar.gz",
                "https://github.com/kmvan/x-prober/releases/latest/download/prober.php",
                # Ocp is no longer maintained
                "https://gist.githubusercontent.com/ck-on/4959032/raw/ocp.php",
                # Ioncube provides official direct download link for the latest version
                "https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz",
                "https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86.tar.gz",
                "https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_aarch64.tar.gz",
                "https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_armv7l.tar.gz",
                # pcre is discontinued; pcre2 is the successor
                "https://versaweb.dl.sourceforge.net/project/pcre/pcre/8.45/pcre-8.45.tar.gz",
                # libmemcached is no longer maintained
                "https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz"]
    for url in url_list:
        resource_list.append({
            "url": url,
            "file_name": url.split("/")[-1]
        })
    return resource_list
