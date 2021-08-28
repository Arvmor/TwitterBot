#!/usr/bin/env python3.6
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from signal import signal, SIGINT
from time import sleep
from random import choice
from sys import path, argv
from importlib import reload
from wget import download
from os import system, listdir
import credentials

# Variables
TotalRunTime = 12
runtimehour = 0
fireFox_options = webdriver.FirefoxOptions()

# fireFox_options.add_argument("--headless")
fireFox_options.add_argument("--no-sandbox")
fireFox_options.add_argument("--disable-dev-shm-usage")
fireFox_options.add_argument("--log-level=3")
fireFox_options.add_argument("--log-level=OFF")
fireFox_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")



def signal_handler(signal, frame):
    driver.quit()
    system(f'rm /tmp/{argv[1]}Twitter*')
    exit(0)


def login():  # login
    global driver
    driver.get("https://twitter.com/login")
    sleep(15)
    while True:
        try:
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(credentials.account[int(argv[1])][0])
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(credentials.account[int(argv[1])][1])
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()
            sleep(2)
            break
        except:
            print('error on login trying again !')
            driver.quit()
            driver = webdriver.Firefox(executable_path=r'geckodriver', options=fireFox_options)
            driver.get("https://twitter.com/login")
            sleep(15)


def unfollow2():
    # you have to authorize your account with below api IF you want to unfollow people
    # there is a high chance to get LIMIT while using below api
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.unfollowspy.com/twittersignin.php')
    sleep(20)
    driver.get('https://www.unfollowspy.com/notfollow.php')
    sleep(15)
    userPerPage = 0
    totalUnFollowed = 0
    while totalUnFollowed != 100:
        while userPerPage != 20:
            driver.find_element(
                By.XPATH, '//*[@id="actionbutton'+str(userPerPage)+'"]').location_once_scrolled_into_view
            driver.find_element(
                By.XPATH, '//*[@id="actionbutton'+str(userPerPage)+'"]').click()
            userPerPage += 1
            totalUnFollowed += 1
            sleep(4)
        userPerPage = 0
        driver.get('https://www.unfollowspy.com/notfollow.php')
        sleep(15)


def unfollow():
    # you have to authorize your account with below api IF you want to unfollow people
    # there is a high chance to get LIMIT while using below api
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://iunfollow.com/accounts/twitter/login/?next=/nonfollow')
    sleep(15)
    usersToUnFollow = 100
    while usersToUnFollow != 51:
        driver.find_element(
            By.XPATH, '/html/body/div[2]/div/section[2]/div/div/div/div[2]/ul/li['+str(usersToUnFollow)+']/div[2]/button[1]').location_once_scrolled_into_view
        driver.find_element(
            By.XPATH, '/html/body/div[2]/div/section[2]/div/div/div/div[2]/ul/li['+str(usersToUnFollow)+']/div[2]/button[1]').click()
        usersToUnFollow -= 1
        sleep(2)


def pintweet():
    # pin function with 1% chance.
    pin = choice(range(100))
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    if pin == 1:
        print("Pin : True")
        driver.get(
            f"https://twitter.com/{credentials.account[int(argv[1])][0]}")
        sleep(15)
        # basically pinning the last tweet
        driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[2]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div').click()
        sleep(1)
        driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[2]').click()
        sleep(1)
        driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]').click()
    sleep(2)


def retweet():
    # retweet function with many tweet sources which allows the bot to pick fresh tweets. with 1/10 chance.
    retweetChance = choice(range(1))
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    if True:
        print("Retweet: True")
        ProfileToSelectTweet = choice(
            range(len(credentials.retweetSource)))
        driver.get(
            f"https://twitter.com/{credentials.retweetSource[ProfileToSelectTweet]}")
        sleep(15)
        try: # If it had pin
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[3]').location_once_scrolled_into_view
            ret = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[3]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div')))
            ret.click()
            sleep(5)
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div').click()
        except: # If it didn't have pin
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[2]').location_once_scrolled_into_view
            ret = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div')))
            ret.click()
            sleep(5)
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div').click()


def clear():  # will close useless tabs
    sleep(1)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def tweet(tweetText):
    # tweet function, it will tweet whatever is in the tweetText variable
    driver.get('https://twitter.com/compose/tweet')
    sleep(15)
    for pic in tweetText[1]:
        driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[1]/input').send_keys(f'/Users/arvin/Desktop/Coding/GitHub/TwitterBot/data/{pic}')
        sleep(5)
    driver.find_element(
        By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div').send_keys(tweetText[0] + choice(credentials.footer))
    sleep(2)
    element = driver.find_element(
        By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
    driver.execute_script("arguments[0].click();", element)
    sleep(2)


def pickpost():
    pickedPhotos = []
    hoeName = choice(listdir('data/'))
    for _ in range(choice([3,4])):
        pickedPhotos.append(hoeName+'/'+choice(listdir('data/'+hoeName)))
    tweetText = choice(credentials.texts) + f'.\n.\n.\nCredit💌: {hoeName} '
    return tweetText, pickedPhotos


def follow_Proccess():
    # will randomly pick one of these below sources and then follow their n last followers
    randomNumber = choice(range(len(credentials.followIdList)))
    driver.execute_script("window.open('');")
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.get(
        f"https://twitter.com/{credentials.followIdList[randomNumber]}/followers")
    sleep(30)
    # starts following
    acc = 1
    followed = 0
    errors = 0
    driver.find_element(
        By.XPATH, f'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[{acc}]/div/div/div/div[2]/div[1]/div[2]/div').click()
    while(followed != 20):
        try:
            sleep(1)
            acc += 1
            driver.find_element(
                By.XPATH, f'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[{acc-2}]/div/div/div/div[2]/div[1]/div[2]/div').location_once_scrolled_into_view
            driver.find_element(
                By.XPATH, f'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[{acc}]/div/div/div/div[2]/div[1]/div[2]/div').click()
            followed += 1
        except:
            errors += 1
            if errors >= 8:
                break
            if driver.find_elements(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[1]'):
                driver.find_element(
                    By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[1]').click()
                sleep(4)


signal(SIGINT, signal_handler)  # Handle Ctrl-C
driver = webdriver.Firefox(executable_path=r'geckodriver', options=fireFox_options)

# Main code
login()
while True:
    if runtimehour == TotalRunTime:
        runtimehour = 0
        sleep(21600)

    while True:
        try:
            # selects a random post and then tweet it
            sleep(2)
            tweet(pickpost())
            # clear()
            sleep(2)
            # retweet with 1/10 chance
            for _ in range(choice([0,0,1,1,2,3])):
                retweet()
                clear()
            # pin the last tweet with 1% chance
            # pintweet()
            # clear()
            #  following Proccess
            follow_Proccess()
            clear()
            # checks for runtime hour
            runtimehour += 1
            print(f"All done ! {runtimehour}/{TotalRunTime}")
            if runtimehour == TotalRunTime:
                break
            # here you can set the delay time
            driver.quit()
            sleep(choice(range(1800, 1900)))
            reload(credentials)
            driver = webdriver.Firefox(executable_path=r'geckodriver', options=fireFox_options)
            login()
        except Exception as excep:
            print(excep)
