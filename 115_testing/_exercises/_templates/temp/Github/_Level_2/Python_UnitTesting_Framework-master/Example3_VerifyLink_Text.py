____ selenium ______ webdriver
______ unittest
______ time
____ selenium.webdriver.common.by ______ By


c_ Internet(unittest.TestCase):

    @classmethod
    ___ setUpClass(cls):
        global driver
        driver _ webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com/")

    ___ test_A_Links
        driver.find_element_by_link_text("A/B Testing").click()
        driver.implicitly_wait(5)
        ABTestURL _ driver.current_url

        assertEqual(ABTestURL, 'http://the-internet.herokuapp.com/abtest')

        TextComparsion _ driver.find_element_by_xpath("//p")
        assertEqual(TextComparsion.text,
                         'Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through).')

        print(TextComparsion.text)

    @classmethods
    ___ tearDownClass(cls):
        driver.quit()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
