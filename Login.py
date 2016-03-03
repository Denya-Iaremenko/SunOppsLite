import os
from time import sleep

import unittest

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH('/Users/Denys/Dropbox/APK+IPO/SunOpps Lite/SunOpps Lite Android STG v2.9.0(45).apk')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    #def tearDown(self):
        # end the session
        #self.driver.quit()

    def test_find_elements(self):
        el = self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]")
        el.send_keys("sp@1-m.com")

        els = self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[2]")
        els.send_keys("Test11")


        self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]").click()





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
