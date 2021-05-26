import requests
import zipfile
import platform
import sys

chrome_version = '91.0.4472.19'

def install_chrome_driver_package(link):
    chromedriver_content = requests.get(link)

    chromedriver_file = open('Chromedriver.zip', 'wb')
    chromedriver_file.write(chromedriver_content.content)
    chromedriver_file.close()

    with zipfile.ZipFile('Chromedriver.zip') as zip_file:
        zip_file.extractall('ChromeDriver')

if __name__ == '__main__':
    print('Installing dependencies')
    if 'Windows' in platform.system():
        install_chrome_driver_package(f'https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_win32.zip')

    elif 'Linux' in platform.system():
        install_chrome_driver_package(f'https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_linux64.zip')

    else:
        install_chrome_driver_package(f'https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_mac64.zip')
    print('Installation complete')
