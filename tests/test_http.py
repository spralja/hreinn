import unittest

from hreinn import http



class ResponseStatusTestCase(unittest.TestCase):
    # the Status() constructor takes in either:
    # * 2 positional arguments (http_version and status_code)
    # * 3 positional arguments (http_version, status_code, and reason_phrase)
    # * 2 keyword arguments (http_version and status_code)
    # * 3 keyword arguments (http_version, status_code, and reason_phrase)
    # * 1 positional arguemnt, a dictionary that is to be interpreted as unpacked
    # i. e.
    # (\, http_version, status_code, reason_phrase='')
    # (*, http_version, status_code, reason_phrase='')
    # (kwargs)

    # Constructor Tests

    def test_constructor00(self):
        status = http.Response.Status('1.1', 404, 'Not Found')
        self.assertEqual(str(status), 'HTTP/1.1 404 Not Found')

    def test_constructor01(self):
        status = http.Response.Status('1.1', 200, 'OK')
        self.assertEqual(str(status), 'HTTP/1.1 200 OK')

    def test_constructor02(self):
        status = http.Response.Status(http_version='1.1', status_code=200, reason_phrase='OK')
        self.assertEqual(str(status), 'HTTP/1.1 200 OK')

    def test_constructor03(self):
        status = http.Response.Status('1.1', 200)
        self.assertEqual(str(status), 'HTTP/1.1 200 ')

    def test_constructor04(self):
        status = http.Response.Status(http_version='1.1', status_code=200)
        self.assertEqual(str(status), 'HTTP/1.1 200 ')

    def test_constructor05(self):
        status = http.Response.Status({'http-version': '1.1', 'status-code': 200, 'reason-phrase':'OK'})
        self.assertEqual(str(status), 'HTTP/1.1 200 OK')

    def test_constructor06(self):
        status = http.Response.Status({'http-version': '1.1', 'status-code': 200})
        self.assertEqual(str(status), 'HTTP/1.1 200 ')

    def test_constructor07(self):
        status = http.Response.Status({'http_version': '1.1', 'status_code': 200})
        self.assertEqual(str(status), 'HTTP/1.1 200 ')

    def test_constructor08(self):
        status = http.Response.Status({'http_version': '1.1', 'status-code': 200})
        self.assertEqual(str(status), 'HTTP/1.1 200 ')

    def test_constructor09(self):
        status = http.Response.Status(**{'http-version': '1.1', 'status-code': 200})
        self.assertEqual(str(status), 'HTTP/1.1 200 ')

    # Constructor Test with illegal arguments

    def test_constructor_exception00(self):
        with self.assertRaises(TypeError):
            status = http.Response.Status()

    def test_constructor_exception01(self):
        with self.assertRaises(TypeError):
            status = http.Response.Status('1.1', 200, 'OK', 'comment')

    def test_constructor_exception02(self):
        with self.assertRaises(TypeError):
            status = http.Response.Status(http_version='1.1', status_code=200, reason_phrase='OK', comment='comment')

    def test_constructor_exception03(self):
        with self.assertRaises(TypeError):
            status = http.Response.Status(http_version='1.1', status_code=200, comment='comment')

    def test_constructor_exception04(self):
        with self.assertRaises(TypeError):
            status = http.Response.Status('1.1', status_code=200)
    
    def test_constructor_exception05(self):
        with self.assertRaises(TypeError):
            status = http.Response.Status(http_version='1.1')

    def test_constructor_exception06(self):
        with self.assertRaises(TypeError):
            status = http.Response.Status({})

    def test_constructor_exception07(self):
        with self.assertRaises(TypeError):
            status = http.Response.Status(
                {'http-version': '1.1', 'status-code': 200, 'reason-phrase': 'OK', 'comment': 'comment'}
            )
    
    def test_constructor_exception08(self):
        with self.assertRaises(TypeError):
            status = http.Response.Status({'http-version': '1.1', 'status-code': 200, 'comment': 'comment'})
    
    def test_constructor_exception09(self):
        with self.assertRaises(TypeError):
            status = http.Response.Status({'http-version': '1.1'})

    def test_constructor_exception10(self):
        with self.assertRaises(TypeError):
            status = http.Response.Status('tests')

    # Subscript access

    def test_subscript_access00(self):
        status = http.Response.Status('1.1', 200, 'OK')
        self.assertEqual(status['http_version'], '1.1')
        self.assertEqual(status['status_code'], 200)
        self.assertEqual(status['reason_phrase'], 'OK')

    def test_subscript_access01(self):
        status = http.Response.Status('1.1', 404, 'Not Found')
        self.assertEqual(status['http-version'], '1.1')
        self.assertEqual(status['status-code'], 404)
        self.assertEqual(status['reason-phrase'], 'Not Found')

    # Subscript assignment

    def test_subscript_assignment00(self):
        status = http.Response.Status('1.1', 404, 'Not Found')
        
        status['status-code'] = 200
        status['reason-phrase'] = 'OK'

        self.assertEqual(status['status-code'], 200)
        self.assertEqual(status['reason-phrase'], 'OK')
    
    def test_subscript_assignment01(self):
        status = http.Response.Status('1.1', 200, 'OK')

        with self.assertRaises(KeyError):
            status['comment'] = 'comment'

    # Subscript deletion

    def test_subscript_deletion00(self):
        status = http.Response.Status('1.1', 404, 'Not Found')

        with self.assertRaises(TypeError):
            del status['status-code']

    def test_subscript_deletion01(self):
        status = http.Response.Status('1.1', 404, 'Not Found')

        with self.assertRaises(TypeError):
            status.pop('http-version')

    def test_subscript_deleteion02(self):
        status = http.Response.Status('1.1', 404, 'Not Found')
        
        with self.assertRaises(TypeError):
            status.popitem()

    def test_subscript_deletion03(self):
        status = http.Response.Status('1.1', 404, 'Not Found')

        with self.assertRaises(TypeError):
            status.update({'comment': 'comment'})

    # Dictionary Update

    def test_subscript_update00(self):
        status = http.Response.Status('1.1', 404, 'Not Found')

        status.update({'status-code': 200, 'reason-phrase': 'OK'})

        self.assertEqual(status.status_code, 200)
        self.assertEqual(status.reason_phrase, 'OK')

    # Other Dictonary functions ???

class ResponseHeaderTestCase(unittest.TestCase):
    '''
    no tests for now as there is not complex functionallity, and its hard to test the __str__ method, 
    #    becuase the order of the header fields isn't consistent, and doesn't have to be
    '''

class DateTestCase(unittest.TestCase):
    '''
    test tostr
    '''
   

    def test_str00(self):
        from datetime import timezone, timedelta
        date = http.Date(2022, 9, 8, 18, 9, 59, tzinfo=timezone(timedelta(hours=-3)))
        self.assertEqual('Thu, 08 Sep 2022 21:09:59 GMT', str(date))
        

class ResponseTestCase(unittest.TestCase):
    '''
    Constructor should allow for any combination of dictionary-like objects or tuples concrete instances of Header/Status
    '''

    # again to inconsistent
