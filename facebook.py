lgm=open('facebookDetails.txt')
lgm = lgm.read()
lgm = lgm.split('\n')
mail = lgm[0]
pw = lgm[1]
msg = lgm[2]

from selenium import webdriver
import time
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=chrome_options)
driver.get('https://www.facebook.com/')
driver.implicitly_wait(100)
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys(mail)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/input').send_keys(pw)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
#My HOme page
driver.implicitly_wait(1)
while(1):
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[4]/a/span/span').click()
        break
    except:
        continue
        
# Select friends
while(1):
    try:
        driver.execute_script("window.scrollBy(0,400)","")
        break
    except:
        continue

while(1):
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div/div[3]/div/div/div/div/div[1]/div/div/div/div[1]/h2/span/div/div[2]/div/div[2]/div/a/span/span').click()
        break
    except:
        continue
print('First Phase')
while(1):
    try:
        noofFriends = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/a[3]/div/span/span[2]').text
        noofFriends = int(noofFriends)
        print(noofFriends)
        break
    except:
        continue
print('Second Phase')
hrefsofFriends = []
for i in range(1,noofFriends):
    try:
        href = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div[3]/div['+str(i)+']/div[2]/div[1]/a').get_attribute('href')
        hrefsofFriends.append(href)
    except:
        driver.execute_script("window.scrollBy(0,400)","")
print('Third Phase')
# Select a friend and put msg

time.sleep(5)
for i in hrefsofFriends:
    driver.get(i)
    #msger select
    while(1):
        try:
            driver.execute_script("window.scrollBy(0,800)","")
            break
        except:
            continue
#     time.sleep(5)
    while(1):
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/div[2]/span/span').click()
            break
        except:
            continue
    
    # put msg
    while(1):
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(msg)
#             time.sleep(5)
            break
        except:
            continue
    # send
    while(1):
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/span[2]/div/div').submit()
            break
        except:
            continue
time.sleep(5)
driver.quit()
print('Finished')