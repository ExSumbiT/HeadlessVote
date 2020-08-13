from selenium import webdriver
import pickle, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import schedule


def vote():
    def minecratrating():
        driver.get("http://minecraftrating.ru/projects/excalibur-craft/")
        driver.find_element_by_css_selector("body > div.wrapper-main > "
                                            "div.container.container-main.page-server.project-page > div.content "
                                            "> div.promotion-back > div.form-group.form-vote > form > "
                                            "input").send_keys()  # your nickname
        driver.find_element_by_css_selector("body > div.wrapper-main > "
                                            "div.container.container-main.page-server.project-page > div.content "
                                            "> div.promotion-back > div.form-group.form-vote > form > "
                                            "button").click()
        driver.refresh()

    def mctop():
        driver.get("https://mctop.su/servers/1088/servers/?voting=1088")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            driver.add_cookie(cookie)
        driver.get("https://mctop.su/accounts/vk/login/?process=login")
        driver.get("https://mctop.su/servers/1088/servers/?voting=1088")
        wait.until(ec.visibility_of_element_located((By.ID, 'nick'))).send_keys()  # your nickname
        driver.find_element_by_css_selector("#voteModal > div > div > div.modal-body > form > button").click()

    def topcraft():
        driver.get("https://topcraft.ru/servers/308/?voting=308")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            driver.add_cookie(cookie)
        driver.get("https://topcraft.ru/accounts/vk/login/?process=login")
        driver.get("https://topcraft.ru/servers/308/?voting=308")
        wait.until(ec.visibility_of_element_located((By.ID, 'nick'))).send_keys()  # your nickname
        driver.find_element_by_css_selector("#voteModal > div.modal-dialog > div > div.modal-body > form > div > "
                                            "button").click()

    def mcrate():
        driver.get("http://oauth.vk.com/authorize?client_id=3059117&redirect_uri=http://mcrate.su/add/rate?idp"
                   "=4396&response_type=code")
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#add-project > tbody > tr > td:nth-child(2) > '
                                                                      'input[type=text]'))).send_keys()  # your nickname
        driver.find_element_by_id("buttonrate").click()

    # PROXY = "183.89.117.174:8080"

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_options)
    driver.get("http://vk.com")
    wait = WebDriverWait(driver, 10)
    driver.find_element_by_id("index_email").send_keys()  # VK login
    driver.find_element_by_id("index_pass").send_keys()  # VK password
    driver.find_element_by_id("index_login_button").click()
    driver.get("http://vk.com/feed")
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

    minecratrating()
    mctop()
    topcraft()
    mcrate()
    driver.close()


schedule.every().day.at("21:05").do(vote)
while True:
    schedule.run_pending()
    time.sleep(1)
