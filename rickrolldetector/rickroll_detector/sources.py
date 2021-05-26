from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import platform


# noinspection
class IdentifyLink:
    def __init__(self, yt_link):
        self.link = yt_link

        self.options = Options()
        self.options.add_argument("--mute-audio")
        self.options.add_argument("--window-size=1440, 900")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--headless")
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])

        if 'Windows' in platform.system():
            self.PATH = 'ChromeDriver\chromedriver.exe'

        else:
            self.PATH = 'ChromeDriver/chromedriver'

        self.driver_link = webdriver.Chrome(self.PATH, options=self.options)

        try:
            self.driver_link.get(yt_link)

        except Exception as E:
            print('This link was probably not a YT link or was invalid!')
            self.driver_link.quit()

    def get_link_details(self):
        time.sleep(1)
        try:
            page_content = WebDriverWait(self.driver_link, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="info"]'))
            )

            time.sleep(1)
            for stuff in page_content:
                video_info = []

                title = stuff.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string')
                video_info.append(title.text)

                view_count = stuff.find_element_by_xpath('//*[@id="count"]/ytd-video-view-count-renderer')
                video_info.append(view_count.text)

                uploaded_on = stuff.find_element_by_xpath('//*[@id="date"]/yt-formatted-string')
                video_info.append(uploaded_on.text)

                likes_count = stuff.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div[2]/ytd-toggle-button-renderer[1]/a/yt-formatted-string')
                video_info.append(likes_count.text)

                dislikes_count = stuff.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div[2]/ytd-toggle-button-renderer[2]/a/yt-formatted-string')
                video_info.append(dislikes_count.text)

            return video_info

        except Exception as E:
            self.driver_link.quit()
            print(E)
            return ('The Link you provided was probably not valid or the video was taken down!')

    def other_details(self):
        try:
            details = WebDriverWait(self.driver_link, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="top-row"]/ytd-video-owner-renderer'))
            )

            details = details.text.split('\n')
            return details

        except Exception as E:
            self.driver_link.quit()

    def comments(self):
        try:
            main_page = WebDriverWait(self.driver_link, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "body"))
            )

            x = 0
            for _ in range(18):
                main_page.send_keys(Keys.DOWN)
                x = x + 1
                if x == 1:
                    main_page.send_keys(Keys.SPACE)
                    time.sleep(1)

                else:
                    continue

            comments = WebDriverWait(self.driver_link, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="content-text"]'))
            )

            comments_ = []
            for stuff in comments:
                comments_.append(stuff.text)

            return comments_

        except Exception as E:
            print(E)
            return None
            self.driver_link.close()

    def copyright(self):
        try:
            read_more = WebDriverWait(self.driver_link, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "body"))
            )

            x = 0
            for iter_ in range(10):
                read_more.send_keys(Keys.DOWN)

                x = x + 1
                if x == 1:
                    time.sleep(1)
                    read_more.send_keys(Keys.SPACE)

                else:
                    continue

            try:
                button = WebDriverWait(self.driver_link, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="more"]/yt-formatted-string'))
                )

                time.sleep(1)
                button.click()
                time.sleep(1)

                copyright = WebDriverWait(self.driver_link, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/yt-formatted-string/a'))
                )
                return copyright.text

            except Exception as E:
                pass

        except Exception as E:
            return 'No copyright found'
            self.driver_link.quit()

    def playlist_name(self):
        try:
            playlist_videos = WebDriverWait(self.driver_link, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="playlist-items"]'))
            )

            playlist_name = WebDriverWait(self.driver_link, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="header-description"]/h3'))
            )

            playlist_videos_ = []
            for videos_ in playlist_videos:
                playlist_videos_.append(videos_.text)

            return playlist_videos_, playlist_name.text

        except Exception as E:
            self.driver_link.quit()
            return 'This video was probably not inside a playlist', None

    def total_description(self):
        try:
            main_page = WebDriverWait(self.driver_link, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "body"))
            )

            x = 0
            for _ in range(10):
                main_page.send_keys(Keys.DOWN)

                x = x + 1
                if x == 1:
                    time.sleep(1)
                    main_page.send_keys(Keys.SPACE)
                else:
                    continue

            try:
                button = main_page.find_element_by_xpath('//*[@id="more"]/yt-formatted-string')
                time.sleep(2)
                button.click()

            except Exception as E:
                pass
            
            time.sleep(2)
            description = WebDriverWait(self.driver_link, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/ytd-expander'))
            )
            return description.text

        except Exception as E:
            return 'No description found'
            self.driver_link.quit()

    def close_driver(self):
        self.driver_link.quit()
