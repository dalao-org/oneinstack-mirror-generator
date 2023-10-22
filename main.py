import time

from utils import (curl, fail2ban, mysql, nginx, php, phpmyadmin, redis, cacert, acme_sh, nghttp2, postgresql, python,
                   httpd, apr, imagemagick, openresty, memcached, lua_nginx_module, php_plugins, pip, tengine, xcache,
                   boost, github, pure_ftpd, htop, misc, freetype, libiconv, bison, openssl)
import json
import os


def main():
    mode = os.environ.get("MODE", "PROD")
    if mode == "PROD":
        os.makedirs("output", exist_ok=True)
        resource_list = []
        latest_meta_list = []

        curl_output = curl.make_cache()
        resource_list += curl_output[0]
        latest_meta_list.append(curl_output[1])

        resource_list += fail2ban.make_cache()

        mysql_output = mysql.make_cache()
        resource_list += mysql_output[0]
        latest_meta_list += mysql_output[1]

        nginx_output = nginx.make_cache()
        resource_list += nginx_output[0]
        latest_meta_list.append(nginx_output[1])

        php_output = php.make_cache()
        resource_list += php_output[0]
        latest_meta_list += php_output[1]

        phpmyadmin_output = phpmyadmin.make_cache()
        resource_list += phpmyadmin_output[0]
        latest_meta_list += phpmyadmin_output[1]

        resource_list += redis.make_cache()
        resource_list += cacert.make_cache()
        resource_list += acme_sh.make_cache()

        nghttp2_output = nghttp2.make_cache()
        resource_list += nghttp2_output[0]
        latest_meta_list.append(nghttp2_output[1])

        postgresql_output = postgresql.make_cache()
        resource_list += postgresql_output[0]
        latest_meta_list.append(postgresql_output[1])

        resource_list += python.make_cache()

        httpd_output = httpd.make_cache()
        resource_list += httpd_output[0]
        latest_meta_list.append(httpd_output[1])

        apr_output = apr.make_cache()
        resource_list += apr_output[0]
        latest_meta_list += apr_output[1]

        resource_list += imagemagick.make_cache()

        openresty_output = openresty.make_cache()
        resource_list += openresty_output[0]
        latest_meta_list.append(openresty_output[1])

        resource_list += memcached.make_cache()
        resource_list += lua_nginx_module.make_cache()
        resource_list += pip.make_cache()

        tengine_output = tengine.make_cache()
        resource_list += tengine_output[0]
        latest_meta_list.append(tengine_output[1])

        resource_list += xcache.make_cache()
        resource_list += boost.make_cache()

        openssl_output = openssl.make_cache()
        resource_list += openssl_output[0]
        latest_meta_list += openssl_output[1]

        resource_list += github.download_repo_by_tag("openresty", "lua-resty-core", "tar.gz", True)
        resource_list += pure_ftpd.make_cache()
        resource_list += htop.make_cache()
        resource_list += github.get_single_package_from_release("jemalloc", "jemalloc")
        resource_list += github.download_repo_by_tag("openresty", "lua-resty-lrucache", "tar.gz", True)
        resource_list += github.download_repo_by_tag("openresty", "luajit2", "tar.gz", True)
        resource_list += github.download_repo_by_tag("openresty", "lua-cjson", "tar.gz", True)
        resource_list += github.get_package_from_release_with_regular_expression("gperftools",
                                                                                 "gperftools",
                                                                                 r"gperftools-\d+.\d+.tar.gz",
                                                                                 3)

        icu_output = github.get_package_from_release_with_regular_expression("unicode-org",
                                                                             "icu",
                                                                             r"(icu4c-)[\d|\-|\_]+(src\.tgz)",
                                                                             3,
                                                                             "icu4c")
        resource_list += icu_output[0]
        latest_meta_list.append(icu_output[1])

        # gdrive package is changed!!!
        resource_list += github.get_package_from_release_with_regular_expression("glotlabs",
                                                                                 "gdrive",
                                                                                 r"linux",
                                                                                 1)
        libzip_output = github.get_package_from_release_with_regular_expression("nih-at",
                                                                                "libzip",
                                                                                r"\.tar\.gz",
                                                                                5,
                                                                                "libzip_ver")
        resource_list += libzip_output[0]
        latest_meta_list.append(libzip_output[1])

        libsodium_output = github.get_package_from_release_with_regular_expression("jedisct1",
                                                                                   "libsodium",
                                                                                   r"\d+\.tar\.gz",
                                                                                   5,
                                                                                   "libsodium_ver")
        resource_list += libsodium_output[0]
        latest_meta_list.append(libsodium_output[1])

        # Name changed!!! Was argon2-20190702.tar.gz and 20190702.tar.gz
        argon2_output = github.download_repo_by_tag("P-H-C", "phc-winner-argon2",
                                                    archive_type="tar.gz", filter_blacklist=True,
                                                    latest_meta_name="argon2_ver")
        resource_list += argon2_output[0]
        latest_meta_list.append(argon2_output[1])

        freetype_output = freetype.make_cache()
        resource_list += freetype_output[0]
        latest_meta_list.append(freetype_output[1])

        resource_list += github.get_package_from_release_with_regular_expression("libevent",
                                                                                 "libevent",
                                                                                 r"\.tar\.gz$",
                                                                                 5)
        resource_list += github.download_repo_by_tag("jokkedk", "webgrind", "zip", False)
        # ngx_devel_kit name changed!!!
        resource_list += github.download_repo_by_tag("vision5", "ngx_devel_kit", "tar.gz", False)
        resource_list += github.get_package_from_release_with_regular_expression("kkos", "oniguruma",
                                                                                 r"\.tar\.gz$", 5)
        resource_list += github.get_package_from_release_with_regular_expression("dropbox", "dbxcli",
                                                                                 r"dbxcli-linux-arm", 1)
        resource_list += github.get_package_from_release_with_regular_expression("dropbox", "dbxcli",
                                                                                 r"dbxcli-linux-amd64", 1)
        resource_list += bison.make_cache()

        libiconv_output = libiconv.make_cache()
        resource_list += libiconv_output[0]
        latest_meta_list.append(libiconv_output[1])

        misc_output = misc.make_cache()
        resource_list += misc_output[0]
        latest_meta_list += misc_output[1]

        resource_list += php_plugins.make_cache("APCU", "apcu")
        resource_list += php_plugins.make_cache("gmagick", "gmagick")
        resource_list += php_plugins.make_cache("imagick", "imagick")
        resource_list += php_plugins.make_cache("memcache", "memcache")
        resource_list += php_plugins.make_cache("mongodb", "mongodb")
        resource_list += php_plugins.make_cache("swoole", "swoole")
        resource_list += php_plugins.make_cache("YAF", "yaf")
        resource_list += php_plugins.make_cache("xdebug", "xdebug")
        resource_list += php_plugins.make_cache("mongo", "mongo")

        with open(r"./output/resources.json", "w+") as f:
            f.write(json.dumps(resource_list, indent=4))
        with open(r"./output/latest_meta.json", "w+") as f:
            f.write(json.dumps(latest_meta_list, indent=4))
    else:
        print("Mode is not PROD, skipping resource list generation.")
        with open(r"./output/resources.json", "r") as f:
            resource_list = json.loads(f.read())
        with open(r"./output/latest_meta.json", "r") as f:
            latest_meta_list = json.loads(f.read())

    redirect_rules_file = open(r"./output/_redirects", "w+")
    redirect_rules_html = open(r"./output/index.html", "w+")
    redirect_rules_html.write("""<!DOCTYPE html>
    <html>
    <head>
    <title>Oneinstack Mirror</title>
    </head>
    <body>
    
    <h1>Oneinstack Mirror</h1>
    <p>This page is generated by <a href="https://github.com/dalao-org/oneinstack-mirror-generator">oneinstack-mirror-generator</a></p>
    <p>A suggested version file can be found in <a href="/suggest_versions.txt">suggest_versions.txt.</a></p>
    """
                              )
    for resource in resource_list:
        if "file_name" in resource.keys():
            file_name = resource['file_name']
        else:
            file_name = resource["url"].split("/")[-1]
        rule = f"/src/{file_name} {resource["url"]} 301"
        redirect_rules_file.write(rule + "\n")
        redirect_rules_html.write(f'    <a href="{resource["url"]}">{file_name}</a><br>\n')
    redirect_rules_file.close()
    redirect_rules_html.write("""</body>
    </html>
    """)
    redirect_rules_html.close()

    # Generate suggest_versions.txt
    with open(r"./output/suggest_versions.txt", "w+") as f:
        for meta in latest_meta_list:
            f.write(f"{meta['version_file_name']}={meta['version']}\n")


if __name__ == "__main__":
    main()
