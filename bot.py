from selenium import webdriver
import time
from username_instagram import username, password
from selenium.webdriver.common.keys import Keys

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(5)
        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

   
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(3)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"first Count: {followerCount}")

        action = webdriver.ActionChains(self.browser)
        
        while True:
            if followerCount < 13:
                dialog.click()
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(2)
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(2)

                newCount = len(dialog.find_elements_by_css_selector("li"))

                if followerCount != newCount:
                    followerCount = newCount
                    print(f"updated Count: {newCount}")
                    time.sleep(3)
                
            else:
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(2)
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(2)
                
                newCount = len(dialog.find_elements_by_css_selector("li"))

                if followerCount != newCount:
                    followerCount = newCount
                    print(f"updated Count: {newCount}")
                    time.sleep(3)
                    pass
                else:
                    break



        followers = dialog.find_elements_by_css_selector("li")
        followerList = []
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)

        with open("followers.txt", "w", encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")

    def getFollow(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text != "Takip et":
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten Takiptesin.")

    def unFollowUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)
        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text == "Takiptesin":
            followButton.click()
            time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div/span").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()
       
        
        
run = Instagram(username,password)
run.signIn()
run.getFollowers()
# run.getFollow("instagramusername")
# liste = ["instagramusername", "instagramusername"]

# for user in liste:
    # run.getFollow(user)
    # time.sleep(3)

# run.unFollowUser("instagramusername")

