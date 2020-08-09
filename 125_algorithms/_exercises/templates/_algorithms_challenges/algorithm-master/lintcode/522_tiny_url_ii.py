______ random


class TinyUrl2:
    ___ __init__(self
        self.chars = [str(i) for i in range(10)]
        self.chars.extend(chr(i) for i in range(ord('a'), ord('z') + 1))
        self.chars.extend(chr(i) for i in range(ord('A'), ord('Z') + 1))

        self.host = 'http://tiny.url/'
        self.size = 6
        self.lg2st = {}
        self.st2lg = {}

        self.custom_lg2st = {}
        self.custom_st2lg = {}

    ___ createCustom(self, url, key
        """
        :type url: str
        :type key: str
        :rtype: str
        """
        __ not url or not key:
            r_ 'error'

        __ (
            url in self.custom_lg2st and
            key in self.custom_st2lg

            r_ self.get_tiny_url(key)

        __ (
            url not in self.custom_lg2st and
            key not in self.custom_st2lg

            self.custom_lg2st[url] = key
            self.custom_st2lg[key] = url
            r_ self.get_tiny_url(key)

        r_ 'error'

    ___ longToShort(self, url
        """
        :type url: str
        :rtype: str
        """
        __ not url:
            r_ 'error'
        __ url in self.lg2st:
            r_ self.get_tiny_url(self.lg2st[url])
        __ url in self.custom_lg2st:
            r_ self.get_tiny_url(self.custom_lg2st[url])

        key = self.get_hash_key(self.size)
        w___ key in self.st2lg:
            key = self.get_hash_key(self.size)

        self.lg2st[url] = key
        self.st2lg[key] = url
        r_ self.get_tiny_url(key)

    ___ shortToLong(self, url
        """
        :type url: str
        :rtype: str
        """
        __ not url:
            r_ 'error'

        key = url.replace(self.host, '')

        __ key in self.st2lg:
            r_ self.st2lg[key]
        __ key in self.custom_st2lg:
            r_ self.custom_st2lg[key]

        r_ 'error'

    ___ get_tiny_url(self, hash_key
        r_ '{}{}'.format(self.host, hash_key)

    ___ get_hash_key(self, size
        r_ ''.join(
            random.choice(self.chars)
            for _ in range(size)
        )
