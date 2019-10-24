from packages import *


class FromSmashAPI:
    # option is True for headless browser
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    # url for fromsmash
    url = "https://fromsmash.com/"
    # xpath of clicks needed
    xpath_make_link = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div"
    xpath_transfer_mode_link = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/span"
    xpath_transfer_mode_email = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/span"
    xpath_get_link = "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/span/div/div/div[2]/div/input"
    # default information
    senders_email = ""
    receivers_email = ""
    title = "FILES FOR YOU"
    message = "Hi, This Is Unofficial FromSmashAPI"

    def __init__(self):
        self.browser.get(self.url)
        xpath_agree = "/html/body/div[1]/div/div/div/div[4]/div/div[1]/div[8]/div"
        self.browser.find_element_by_xpath(xpath_agree).click()
        WebDriverWait(self.browser, 5)

    def add_title(self, title):
        self.title = title

    def add_message(self, message):
        self.message = message

    def add_senders_email(self, senders_email):
        self.senders_email = senders_email

    def add_receivers_email(self, receivers_email):
        self.receivers_email = receivers_email

    def upload_file(self, filepath, mode):
        print("1")
        xpath_upload = "/html/body/div[1]/div/div/div/div[3]/div/div/input"
        upload = self.browser.find_element_by_xpath(xpath_upload)
        upload.send_keys(filepath)
        WebDriverWait(self.browser, 5)
        print("2")
        self.mode_of_transfer(mode)
        print("3")
        if mode == 2:
            WebDriverWait(self.browser, 200).until(lambda x: x.find_element_by_xpath(self.xpath_get_link))
            link = self.browser.find_element_by_xpath(self.xpath_get_link).get_attribute('value')
            print("4")
            return link
        elif mode == 1:
            print("Email Is Sent On " + str(self.receivers_email) + " By " + str(self.senders_email))

    def upload_multiple_files(self, filepath_list, mode):
        path_upload = "/html/body/div[1]/div/div/div/div[3]/div/div/input"
        upload = self.browser.find_element_by_xpath(path_upload)
        for x in filepath_list:
            upload.send_keys(x)
        WebDriverWait(self.browser, 5)
        self.mode_of_transfer(mode)
        n = len(filepath_list)
        if mode == 2:
            WebDriverWait(self.browser, n*200).until(lambda x: x.find_element_by_xpath(self.xpath_get_link))
            link = self.browser.find_element_by_xpath(self.xpath_get_link).get_attribute('value')
            print("4")
            return link
        elif mode == 1:
            print("Email Is Sent On " + str(self.receivers_email) + " By " + str(self.senders_email))

    def mode_of_transfer(self, mode):
        print("2.1")
        if mode == 1:
            print("2.2")
            self.browser.find_element_by_xpath(self.xpath_transfer_mode_email).click()
            print("2.3")
            xpath_contact_email = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/form/div[1]/div[1]/div/div[2]/div/input[1]"
            xpath_your_email = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/input"
            xpath_message = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/form/div[1]/div[6]/textarea"
            self.browser.find_element_by_xpath(xpath_your_email).send_keys(self.senders_email)
            self.browser.find_element_by_xpath(xpath_contact_email).send_keys(self.receivers_email)
            self.browser.find_element_by_xpath(xpath_message).send_keys(self.message)
            print("2.4")
            send_mail = self.browser.find_element_by_xpath(self.xpath_make_link)
            self.browser.execute_script("arguments[0].click();", send_mail)
            print("2.5")

        elif mode == 2:
            print("2.2")
            self.browser.find_element_by_xpath(self.xpath_transfer_mode_link).click()
            print("2.3")
            xpath_email = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/form/div[1]/div[3]/input"
            xpath_title = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/form/div[1]/div[1]/input"
            self.browser.find_element_by_xpath(xpath_title).send_keys(self.title)
            self.browser.find_element_by_xpath(xpath_email).send_keys(self.receivers_email)
            print("2.4")
            make_link = self.browser.find_element_by_xpath(self.xpath_make_link)
            self.browser.execute_script("arguments[0].click();", make_link)
            print("2.5")
