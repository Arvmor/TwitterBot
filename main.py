#!/usr/bin/env python3
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
from os import system
import credentials


def signal_handler(signal, frame):
    driver.quit()
    system(f'rm /tmp/{argv[1]}Twitter*')
    exit(0)


def login():  # login
    driver.get("https://twitter.com/login")
    sleep(15)
    while True:
        driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys(credentials.account[int(argv[1])][2])
        driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys(credentials.account[int(argv[1])][1])
        driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div').click()
        sleep(2)
        try:
            if driver.find_element(By.XPATH, '/html/body/div[2]/div/p[3]/strong').text != '':
                driver.find_element(By.XPATH, '/html/body/div[2]/div/form/input[8]').send_keys(
                    f"09{credentials.account[int(argv[1])][3]}")
                sleep(2)
                driver.find_element(
                    By.XPATH, '/html/body/div[2]/div/form/input[9]').click()
                sleep(5)
                driver.get("https://twitter.com/login")
                break
            # if driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/span').text != "":
            #     driver.find_element(
            #         By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys(credentials.account[int(argv[1])][2])
            #     driver.find_element(
            #         By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys(credentials.account[int(argv[1])][1])
            #     sleep(2)
            #     driver.find_element(
            #         By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div').click()
            #     sleep(2)
            #     break
        except:
            pass
        break


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
            By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[3]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div').click()
        sleep(1)
        driver.find_element(
            By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[2]').click()
        sleep(1)
        driver.find_element(
            By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]').click()
    sleep(2)


def retweet():
    # retweet function with many tweet sources which allows the bot to pick fresh tweets. with 1/10 chance.
    retweetChance = choice(range(10))
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    if retweetChance == 1:
        print("Retweet: True")
        ProfileToSelectTweet = choice(
            range(len(credentials.retweetSource)))
        driver.get(
            f"https://twitter.com/{credentials.retweetSource[ProfileToSelectTweet]}")
        sleep(15)
        driver.find_element(
            By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[3]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div').location_once_scrolled_into_view
        driver.find_element(
            By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[3]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div').click()
        sleep(3)
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
    driver.find_element(
        By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/span').send_keys(tweetText[0])
    if int(argv[1]) != 2:
        if tweetText[1] == "image":
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/input').send_keys(f'/tmp/{argv[1]}TwitterImage.jpg')
            sleep(120)
        elif tweetText[1] == "video":
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/input').send_keys(f'/tmp/{argv[1]}TwitterVideo.mp4')
            sleep(300)
        sleep(2)
        driver.find_element(
            By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]').click()
    else:
        if tweetText[1] == "image":
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[1]/input').send_keys(f'/tmp/{argv[1]}TwitterImage.jpg')
            sleep(120)
        elif tweetText[1] == "video":
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[1]/input').send_keys(f'/tmp/{argv[1]}TwitterVideo.mp4')
            sleep(300)
        sleep(2)
        driver.find_element(
            By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]').click()
    sleep(2)


def pickpost():
    # it will pick a random post from telegram channel which in here is our tweet source
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    postNumbers = choice(range(171509))
    driver.get(f"https://t.me/OfficialPersianTwitter/{postNumbers}")
    sleep(10)
    try:
        driver.switch_to.frame(
            driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div[2]/div[1]/iframe",
            )
        )
    except:
        if choice(range(5)) == 1:
            tweetText = credentials.errorText[choice(
                range(len(credentials.errorText)))]
            return tweetText, "None"
        else:
            tweetText = ''
            return tweetText, "None"
    tweetText = driver.find_element(
        By.XPATH, '/html/body/div/div[2]/div[2]').text.strip()
    ch = -24
    while abs(ch) != len(tweetText):
        if tweetText[ch] == '》' or tweetText[ch] == '×' or tweetText[ch] == '•' or tweetText[ch] == '»' or tweetText[ch] == '*' or tweetText[ch] == '※' or tweetText[ch] == '☆':
            tweetText = tweetText[:ch]
        ch -= 1
    tweetText = tweetText.strip()
    ch = -1
    while abs(ch) != len(tweetText):
        if tweetText[ch] == '×' or tweetText[ch] == '•' or tweetText[ch] == '*' or tweetText[ch] == '※' or tweetText[ch] == '☆':
            tweetText = tweetText[:ch]
        ch -= 1
    tweetText = tweetText.strip()
    try:
        if driver.find_element(
                By.XPATH, '/html/body/div/div[2]/a/div[1]/video'):
            videoURL = driver.find_element(
                By.XPATH, '/html/body/div/div[2]/a/div[1]/video').get_attribute("src")
            download(videoURL, f'/tmp/{argv[1]}TwitterVideo.mp4')
            return tweetText, "video"
    except:
        try:
            if driver.find_element(
                    By.XPATH, '/html/body/div/div[2]/a').get_attribute("style")[37:-3] != '':
                imageURL = driver.find_element(
                    By.XPATH, '/html/body/div/div[2]/a').get_attribute("style")[37:-3].strip()
                download(imageURL, f'/tmp/{argv[1]}TwitterImage.jpg')
                return tweetText, "image"
        except:
            return tweetText, "None"


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
        By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div['+str(acc)+']/div/div/div/div[2]/div[1]/div[2]/div').click()
    while(followed != 20):
        try:
            sleep(1)
            acc += 1
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div['+str(acc-2)+']/div/div/div/div[2]/div[1]/div[2]/div').location_once_scrolled_into_view
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div['+str(acc)+']/div/div/div/div[2]/div[1]/div[2]/div').click()
            followed += 1
        except:
            errors += 1
            if errors >= 3:
                break
            if driver.find_elements(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[1]'):
                driver.find_element(
                    By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[1]').click()
                sleep(4)


# Variables
TotalRunTime = 28
runtimehour = 0
tweeted = False
chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--log-level=OFF")


signal(SIGINT, signal_handler)  # Handle Ctrl-C
driver = webdriver.Chrome(
    "chromedriver", options=chrome_options)  # driver settings

# Main code
login()
while True:
    if runtimehour == TotalRunTime:
        runtimehour = 0
        sleep(choice(range(34200, 37800)))
        if int(argv[2]) == 1:  # unfollow not followed-back
            try:
                unfollow2()
                clear()
                unfollow()
                clear()
            except Exception as excep:
                print(excep)
    while True:
        try:
            # selects a random post and then tweet it
            if tweeted == False:
                sleep(2)
                tweet(pickpost())
                clear()
            tweeted = True
            sleep(2)
            # retweet with 1/10 chance
            retweet()
            clear()
            # pin the last tweet with 1% chance
            pintweet()
            clear()
            #  following Proccess
            follow_Proccess()
            clear()
            # checks for runtime hour
            runtimehour += 1
            tweeted = False
            print(f"All done ! {runtimehour}/{TotalRunTime}")
            if runtimehour == TotalRunTime:
                break
            # here you can set the delay time
            system(f'rm /tmp/{argv[1]}Twitter*')
            driver.quit()
            sleep(choice(range(1700, 1800)))
            reload(credentials)
            driver = webdriver.Chrome("chromedriver", options=chrome_options)
            login()
        except Exception as excep:
            print(excep)
