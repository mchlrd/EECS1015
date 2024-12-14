import doctest

def validate_url(url: str) -> bool:

    """
    Return True if the URL is valid, otherwise return False.
    >>> validate_url("https://example.com")
    True
    >>> validate_url("http://1website.org")
    True
    >>> validate_url("https://example..com")
    False
    >>> validate_url("http://domain.co..uk")
    False
    >>> validate_url("invalid-url")
    False
    >>> validate_url("ftp://example.com")
    False
    """

    # Strip whitespace from both ends

    url = url.strip()

    # Check if the length is greater than 12

    valid_length = len(url) >= 12

    # Check if it starts with "http://" or "https://"

    starts_with_http = url.startswith('http://') or url.startswith('https://')

    # Check if there is at least one dot and no consecutive dots

    has_dot = url.count(".") == 1 and url.count('..') == 0

    return valid_length and starts_with_http and has_dot



doctest.testmod()