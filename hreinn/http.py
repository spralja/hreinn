from datetime import datetime, timezone


class Date(datetime):
    '''
    HTTP-Date

    This is a wrapper class for datetime.datetime.
    It can be converted to a string in the HTTP-Date string format (as UTC)
    '''

    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Date
    # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    STRFTIME = '%a %d %b %Y %H:%M:%S GMT'

    def __str__(self):
        return self.astimezone(timezone.utc).strftime(self.STRFTIME)


class Response:
    '''
    This is a class that builds a HTTP response object
    It can be converted to a string in the appropriate format or in the bytes format
        with encode
    '''

    # https://www.rfc-editor.org/rfc/rfc7231#section-7

    class Status:
        '''
        This is a class that builds a HTTP response status object
        It can be converted to a string in the appropriate format
        '''
        http_version: str
        status_code: int
        reason_phrase: str

        def __init__(self, http_version, status_code, reason_phrase):
            self.http_version = http_version
            self.status_code = status_code
            self.reason_phrase = reason_phrase

        def __str__(self):
            return f'HTTP/{self.http_version} {self.status_code} {self.reason_phrase}'
    

    class Header(dict):
        '''
        This is a class that builds a HTTP response header
        It is a subclass of dict and has all of its functionality
        It can be converted to a string in the appropriate format
        '''
        date: Date

        def __str__(self):
            return '\r\n'.join(
                    f'{field}: {value}' for field, value in self.items()
                ) + '\r\n'
    
    status: Status
    header: Header
    body: str

    def __init__(self, status, header, body=''):
        self.status = status
        self.header = header
        self.body = body

    def __str__(self):
        return '\r\n'.join((str(self.status), str(self.header), self.body, ''))
        return f'{self.header}{self.body}\r\n'

    def encode(self):
        return str(self).encode()
