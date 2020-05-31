import re

"""
Write a function that when given a URL as a string,
parses out just the domain name and returns it as a string. For example:
domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""


def domain_name(url):
    print(url)
    www = re.findall(r"(www\.?\w+)", url)
    http = re.findall(r"(://[a-zA-Z0-9-]*[^.])", url)
    domain = re.findall(r"[a-zA-Z0-9-]+[^.]", url)
    if www:
        return www[0][4:]
    elif http:
        return http[0][3:]
    else:
        return domain[0]
