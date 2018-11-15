import os
from selenium import webdriver
import threading
import time
from numpy.random import choice

username = "[BS USER]"
access_key = "[BS KEY]"

url = "http://rentalcars.com"

current_dir = os.getcwd()
running_threads = 0
number_of_times_run = 0

cors = ["NL", "ES", "SE", "GB", "US"]
cor_weights = [0.2, 0.2, 0.2, 0.2, 0.2]

desired_caps = [
    {
        'browserName': 'iPhone',
        'device': 'iPhone 7',
        'realMobile': 'true',
        'os_version': '10.3',
        'browserstack.local': True,
        'setAcceptInsecureCerts': True
    },
    {
        'browser': 'Chrome',
        'browser_version': '65.0',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '1920x1080',
        'browserstack.local': True,
        'setAcceptInsecureCerts': True
    }]
cap_weights = [0.5, 0.5]


def GenerateCor():
    return choice(cors, p=cor_weights)


def GenerateRemoteDriverConfig():
    return choice(desired_caps, p=cap_weights)


class ThreadedStuff(object):
    def __init__(self):
        self.cor = GenerateCor()
        self.desired_capabilities = GenerateRemoteDriverConfig()

    def DoStuff(self):
        threading.Thread(target=self.VisitLandingPage, args=(self.cor,)).start()

    def VisitLandingPage(self, cor):
        global running_threads
        global number_of_times_run
        # driver = webdriver.Chrome(current_dir + '/chromedriver')
        driver = webdriver.Remote(
            command_executor='https://' + username + ':' + access_key + '@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=self.desired_capabilities)
        driver.get(url + "?cor=" + cor)
        driver.quit()
        number_of_times_run = number_of_times_run + 1
        running_threads = running_threads - 1


if __name__ == "__main__":
    t_end = time.time() + 60 * 30
    while time.time() < t_end:
        if running_threads <= 2:
            running_threads = running_threads + 1
            ThreadedStuff().DoStuff()

    print("Number of times run: " + str(number_of_times_run))
