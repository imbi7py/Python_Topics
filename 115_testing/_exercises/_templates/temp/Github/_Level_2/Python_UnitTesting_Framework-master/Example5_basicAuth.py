____ selenium ______ webdriver
______ unittest
______ requests



c_ Auth(unittest.TestCase):

    @classmethod
    ___ setUpClass(cls):
        global driver
        driver _ webdriver.Chrome()
        driver.get("http://the-internet.herokuapp.com/")

    ___ test_A_Links
        # driver.find_element_by_link_text("Broken Images").click()
        # time.sleep(4)
        # alert = driver.switch_to_alert()
        # alert.dismiss()

        links _ driver.find_elements_by_css_selector("a")
        for link in links:
            r _ requests.head(link.get_attribute('href'))
            print(link.get_attribute('href'), r.status_code)

    @classmethod
    ___ tearDownClass(cls):
        # driver.quit()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
