# Generated by Selenium IDE
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import smtplib

carriers = {
    'att': '@mms.att.net',
    'tmobile': ' @tmomail.net',
    'verizon': '@vtext.com',
    'sprint': '@page.nextel.com'
}


def send(message):
    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_number = 'YOUR_PHONE_NUMBER{}'.format(carriers['att'])
    auth = ('YOUR_EMAIL', 'EMAIL_PASSWORD')

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail(auth[0], to_number, message)
    return


class TestSatchecker():
    def setup_method(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.vars = {}
        self.actions = ActionChains(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_satchecker(self):

        dateAndLoc = {"November": "", "December": "", "March": ""}

        self.driver.get("https://account.collegeboard.org/login/login")
        self.driver.set_window_size(1720, 1349)
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "#content").click()
        self.driver.find_element(By.ID, "username").send_keys("COLLEGEBOARD_USERNAME")
        self.driver.find_element(By.ID, "password").send_keys("COLLEGEBOARD_PASSWORD")
        self.driver.find_element(By.ID, "#content").click()
        print("logged in")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-width-label").click()
        self.driver.find_element(By.XPATH, '//*[@id="cb-atlas-header-1"]/div[1]/div/div[2]/div/a[1]').click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .cb-item-title").click()
        print("reached landing")
        self.driver.find_element(By.ID, "actionRegisterAnother").click()
        self.driver.find_element(By.ID, "authenticatePage").click()
        self.driver.find_element(By.ID, "gradeLevel").click()
        dropdown = self.driver.find_element(By.ID, "gradeLevel")
        dropdown.find_element(By.XPATH, "//option[. = '11th grade']").click()
        self.driver.find_element(By.ID, "gradeLevel").click()
        self.driver.find_element(By.ID, "continue").click()
        self.driver.find_element(By.ID, "updateLater").click()
        self.driver.find_element(By.ID, "agreeTerms").click()
        self.driver.find_element(By.ID, "continue").click()

        # self.driver.find_element(By.ID, "feeWaiverNo").click()
        # self.driver.find_element(By.ID, "essayAddOnYes").click()
        # if len(self.driver.find_elements(By.ID, "optDeclineSAS")) > 0:
        #     self.driver.find_element(By.ID, "optDeclineSAS").click()
        # elif len(self.driver.find_elements(By.ID, "optDeclineQAS")) > 0:
        #     self.driver.find_element(By.ID, "optDeclineQAS").click()
        # self.driver.find_element(By.ID, "continue").click()
        # print("reached locations page")
        # self.driver.find_element(By.ID, "searchByZipOrCountry").click()
        # self.driver.find_element(By.ID, "js-s2-expandTheSearch").click()
        # time.sleep(0.5)
        # self.driver.find_element(By.ID, "showAvailableOnly").click()
        # if self.driver.find_elements(By.XPATH, '//*[@id="testCenterSearchResults"]/tbody/tr')[0].text == "No matching records found":
        #     print("no dateAndLoc")
        #     send("nothing yet for " + self.driver.find_element(By.ID, "confirmDateTest").text)
        #     time.sleep(1.5)
        # else:
        #     print("dateAndLoc found")
        #     send(str(len(self.driver.find_elements(By.XPATH, '//*[@id="testCenterSearchResults"]/tbody/tr'))) + " dateAndLoc found for " + self.driver.find_element(By.ID, "confirmDateTest").text)
        #     elements = self.driver.find_elements(By.XPATH, '//*[@id="testCenterSearchResults"]/tbody/tr')
        #     for i in range(len(elements)):
        #         send(elements[i].text)

        # selectedTestAdminYYYYMM

        for month in dateAndLoc:
            radioID = ""
            month_num = str(time.strptime(month, "%B").tm_mon)
            if len(month_num) == 1:
                month_num = "0" + month_num
            if int(month_num) < 8:
                radioID = "selectedTestAdminYYYYMM_" + "2021" + month_num + "2021" + month_num
            else:
                radioID = "selectedTestAdminYYYYMM_" + "2020" + month_num + "2020" + month_num


            print(radioID)
            button = self.driver.find_element(By.ID, radioID)
            # self.actions.move_to_element(button).perform()
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            button.click()

            self.driver.find_element(By.ID, "feeWaiverNo").click()
            self.driver.find_element(By.ID, "essayAddOnYes").click()
            if self.driver.find_elements(By.ID, "optDeclineSAS")[0].is_displayed():
                self.driver.find_element(By.ID, "optDeclineSAS").click()
            elif self.driver.find_elements(By.ID, "optDeclineQAS")[0].is_displayed():
                self.driver.find_element(By.ID, "optDeclineQAS").click()
            self.driver.find_element(By.ID, "continue").click()
            print("reached locations page")
            self.driver.find_element(By.ID, "searchByZipOrCountry").click()
            self.driver.find_element(By.ID, "js-s2-expandTheSearch").click()
            time.sleep(0.5)
            self.driver.find_element(By.ID, "showAvailableOnly").click()
            if self.driver.find_elements(By.XPATH, '//*[@id="testCenterSearchResults"]/tbody/tr')[
                0].text == "No matching records found":
                print("no dates")
                dateAndLoc[month] = str(dateAndLoc[month]) + "nothing yet for " + self.driver.find_element(By.ID,
                                                                                                           "confirmDateTest").text
                time.sleep(1.5)
            else:
                print("dates found")
                dateAndLoc[month] = str(dateAndLoc[month]) + str(
                    len(self.driver.find_elements(By.XPATH, '//*[@id="testCenterSearchResults"]/tbody/tr'))) + \
                                    " dates found for " + str(
                    self.driver.find_element(By.ID, "confirmDateTest").text) + "\n"
                send(str(len(self.driver.find_elements(By.XPATH,
                                                       '//*[@id="testCenterSearchResults"]/tbody/tr'))) + " dates found for " + self.driver.find_element(
                    By.ID, "confirmDateTest").text)
                elements = self.driver.find_elements(By.XPATH, '//*[@id="testCenterSearchResults"]/tbody/tr')

                for i in range(len(elements)):
                    dateAndLoc[month] = dateAndLoc[month] + month + "   " + elements[i].text + "\n"

            self.driver.find_element(By.XPATH, '//*[@id="js-middle-chooseyourtest&date"]/div[1]/a').click()
            time.sleep(5)


        self.driver.find_element(By.ID, "cancelBtn").click()
        print("cancelled")
        time.sleep(5)
        # self.driver.find_element(By.XPATH, '//*[starts-with(@id="deleteMyRegistration")]').click()
        self.driver.find_element(By.ID, "deleteMyRegistration1").click()
        self.driver.switch_to.alert.accept()
        print("deleted")
        time.sleep(5)

        finalstr = ""
        for i in dateAndLoc:
            finalstr += str(dateAndLoc[i]) + "\n\n"
        print(finalstr)


# send("completed the test for SAT")

checker = TestSatchecker()

checker.setup_method()
checker.test_satchecker()
checker.teardown_method()
