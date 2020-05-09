______ unittest
____ unittest.mock ______ Mock

______ requests_mock

____ app.mocking_better ______ CurrencyConvertor, CURRENCY_CONVERSION_API_URL


c_ TestCurrency(unittest.TestCase):
    ___ test_get_exchange_rate_without_mocking
        """
        Actually NOT a unit test but rather a system test (connecting to external third party service)
        """
        convertor _ CurrencyConvertor()
        result _ convertor.get_exchange_rate('EUR', 'CZK')
        assertIsInstance(result, float)

    ___ test_get_exchange_rate_with_mocking
        """
        Mocked version of previous test
        """
        mocked_response _ """
                {
                    "base":"EUR",
                    "date":"2018-06-27",
                    "rates":{
                        "AUD":1.5725,
                        "BGN":1.9558,
                        "BRL":4.4152,
                        "CAD":1.5443,
                        "CHF":1.1536,
                        "CNY":7.6649,
                        "CZK":25.777
                    }
                }
                """

        convertor _ CurrencyConvertor()

        with requests_mock.mock() as m:
            m.get('{currency_conversion_api_url}/latest?base=EUR'.f..(
                currency_conversion_api_url_CURRENCY_CONVERSION_API_URL), text_mocked_response)
            result _ convertor.convert_currency('EUR', 'CZK', 100)

        assertIsInstance(result, float)
        assertAlmostEqual(result, 2577.7)

    ___ test_convert_currency__mocking
        convertor _ CurrencyConvertor()
        convertor.get_exchange_rate _ Mock(return_value_25.777)
        result _ convertor.convert_currency('EUR', 'CZK', 100)
        assertIsInstance(result, float)
        assertAlmostEqual(result, 2577.7)
