from utils import (curl, fail2ban, mysql, nginx, php, phpmyadmin, redis, cacert, acme_sh, nghttp2, postgresql, python,
                   httpd, apr, imagemagick, openresty, memcached, lua_nginx_module, php_plugins, pip, tengine, xcache,
                   boost, github, pure_ftpd, htop, misc)
import json
import os


def main():
    os.makedirs("output", exist_ok=True)
    resource_list = []
    resource_list += curl.make_cache()
    resource_list += fail2ban.make_cache()
    resource_list += mysql.make_cache()
    resource_list += nginx.make_cache()
    resource_list += php.make_cache()
    resource_list += phpmyadmin.make_cache()
    resource_list += redis.make_cache()
    resource_list += cacert.make_cache()
    resource_list += acme_sh.make_cache()
    resource_list += nghttp2.make_cache()
    resource_list += postgresql.make_cache()
    resource_list += python.make_cache()
    resource_list += httpd.make_cache()
    resource_list += apr.make_cache()
    resource_list += imagemagick.make_cache()
    resource_list += openresty.make_cache()
    resource_list += memcached.make_cache()
    resource_list += lua_nginx_module.make_cache()
    resource_list += pip.make_cache()
    resource_list += tengine.make_cache()
    resource_list += xcache.make_cache()
    resource_list += boost.make_cache()
    resource_list += github.download_repo_by_tag("openresty", "lua-resty-core",
                                                 "tar.gz", True)
    resource_list += pure_ftpd.make_cache()
    resource_list += htop.make_cache()
    resource_list += github.get_single_package_from_release("jemalloc", "jemalloc")
    resource_list += github.download_repo_by_tag("openresty", "lua-resty-lrucache",
                                                 "tar.gz", True)
    resource_list += github.download_repo_by_tag("openresty", "luajit2",
                                                 "tar.gz", True)
    resource_list += github.download_repo_by_tag("openresty", "lua-cjson",
                                                 "tar.gz", True)
    resource_list += github.get_package_from_release_with_regular_expression("gperftools",
                                                                             "gperftools",
                                                                             r"gperftools-\d+.\d+.tar.gz",
                                                                             3)
    resource_list += github.get_package_from_release_with_regular_expression("unicode-org",
                                                                             "icu",
                                                                             r"(icu4c-)[\d|\-|\_]+(src\.tgz)",
                                                                             3)
    # gdrive package is changed!!!
    resource_list += github.get_package_from_release_with_regular_expression("glotlabs",
                                                                             "gdrive",
                                                                             r"linux",
                                                                             1)
    resource_list += github.get_package_from_release_with_regular_expression("nih-at",
                                                                             "libzip",
                                                                             r"\.tar\.gz",
                                                                             5)
    resource_list += github.get_package_from_release_with_regular_expression("jedisct1",
                                                                             "libsodium",
                                                                             r"\d+\.tar\.gz",
                                                                             5)
    resource_list += misc.make_cache()

    resource_list += php_plugins.make_cache("APCU", "apcu")
    resource_list += php_plugins.make_cache("gmagick", "gmagick")
    resource_list += php_plugins.make_cache("imagick", "imagick")
    resource_list += php_plugins.make_cache("memcache", "memcache")
    resource_list += php_plugins.make_cache("mongodb", "mongodb")
    resource_list += php_plugins.make_cache("swoole", "swoole")
    resource_list += php_plugins.make_cache("YAF", "yaf")
    resource_list += php_plugins.make_cache("xdebug", "xdebug")
    with open(r"./output/resources.json", "w+") as f:
        f.write(json.dumps(resource_list, indent=4))

    redirect_rules_file = open(r"./output/_redirects", "w+")
    for resource in resource_list:
        if "file_name" in resource.keys():
            rule = f"/src/{resource['file_name']} {resource["url"]} 301"
        else:
            file_name = resource["url"].split("/")[-1]
            rule = f"/src/{file_name} {resource["url"]} 301"
        redirect_rules_file.write(rule + "\n")
    redirect_rules_file.close()


if __name__ == "__main__":
    main()
