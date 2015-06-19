import urllib.parse as urllib
from hashlib import sha1


HTTP_DATE_FORMAT = "%a, %d %b %Y %H:%M:%S %Z"


def gen_digest(text):
    return sha1(bytes(text, "utf-8")).hexdigest()


def name_it(bookurl, url):
    """Generate a name from url.
    
    """
    if not isinstance(bookurl, urllib.ParseResult):
        bookurl = urllib.urlparse(bookurl)
    if isinstance(url, urllib.ParseResult):
        url = url.geturl()
    bookurl = "".join(bookurl[2:])
    name = url.split(bookurl,1)[1]
    name = name.rsplit(".vcf",1)[0]
    name = urllib.unquote(name)
    return name


def path_it(cache_dir, name):
    """Generate a path from name.
    
    """
    if str(cache_dir) in name and name.endswith(".vcf"):
        return name
    return cache_dir.joinpath(name + ".vcf")


def url_from_etree(node):
    """Get url form an etree-parsed result of PROPFIND.
    
    """
    return node[0].text


def url_it(bookurl, name):
    if name.startswith("http"):
        return name
    return bookurl.geturl() + urllib.quote(name)
