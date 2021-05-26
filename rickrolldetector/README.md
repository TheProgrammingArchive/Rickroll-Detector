# Rickroll-Detector
Identify rickroll links whether it's a direct YT link or a bit.ly link or a shorturl.at link or even a redirect

## Purpose of the project
Prevent yourself from getting rickrolled through links (If you're annoyed by them) <br/>

## Frameworks used
Selenium for python

## Requirements
Py >= 3.7 <br>
Chrome Browser <br>
Requests library and selenium for python. <br />
Git-scm

## Setup
Install python on windows from https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe (__MAKE SURE TO CLICK ADD PYTHON TO PATH DURING INSTALLATION__)
Install python on linux using: ```sudo apt install python3```
Install pip on linux using: ```sudo apt install python3-pip```

Install selenium using: ```pip3 install selenium``` (Linux) __or__ ```pip install selenium``` (Windows)
Install requests using: ```pip3 install requests``` (Linux) __or__ ```pip install requests``` (Windows)

If you get an output ```'dk' is not recognized as an internal or external command, operable program or batch file.``` on windows. It means python wasn't added to PATH. <br />
Refer https://geek-university.com/python/add-python-to-the-windows-path/ on how to add python to PATH.

Clone the repository to your favoured location using the command: ``` git clone https://github.com/TheProgrammingArchive/Rickroll-Detector/ ```

The Folder structure should look like this <br>
```
RickrollDetector
├── LICENSE
├── README.md
└── rickroll_detector
    ├── find_identity.py
    ├── installer.py
    └── sources.py
```

Run the installer using the command ```installer.py``` (Windows) __OR__ ```python3 installer.py``` (Linux).

The Folder structure should now look like this on Windows<br>
```
RickrollDetector
├── LICENSE
├── README.md
└── rickroll_detector
    ├── ChromeDriver
    │   └── chromedriver.exe
    ├── Chromedriver.zip
    ├── find_identity.py
    ├── installer.py
    └── sources.py
```

Linux 
```
RickrollDetector
├── LICENSE
├── README.md
└── rickroll_detector
    ├── ChromeDriver
    │   └── chromedriver
    ├── Chromedriver.zip
    ├── find_identity.py
    ├── installer.py
    └── sources.py
```
If using linux, navigate to the ChromeDriver folder using ```cd ChromeDriver``` and execute the command ```chmod +x chromedriver```, this will set chromedriver as an executable <br>
__If this isn't done then the find_identity.py will fail on running__

You can now start using the script  <br>
For usage refer to the USAGE section

## Usage
__PROVIDED LINK MUST CONTAIN HTTPS AND BE PROVIDED IN QUOTES<br>
"https://www.youtube.com/watch?v=dQw4w9WgXcQ" OR "https://shorturl.at/lnBNU" OR  "https://bit.ly/3mUuDXA"__ (***THESE ARE LINKS THAT LEAD TO RICK ASTLEY'S MUSIC VIDEO***)

Linux <br>
```
ubuntu@yt:~/rickroll-detector/rickroll-detector$ python3 find_identity.py -option "link"
```

Windows <br>
```
C:\pathtodetector\rickroll_detector> find_identity.py -option "link"
```

## Options
### find_identity.py -mc "link":
Searches for a certain music tag in the description

### find_identity.py -c "link": 
Searches for a certain SME tag in the video to check if it's a rickroll or not

### find_identity.py -cmt "link"
Searches for any mentions about rickrolls in the comment section of the video

### find_identity.py -t "link"
Searches for certain keywords in the video title to determine if it's a rickroll or not

### find_identity.py -pl "link"
Sometimes rickroll videos are taken from certain rickroll playlists. Checks for certain keywords in the playlist name, if nothing was found returns 'No playlist found'

### find_identity.py -plv "link"
Prints a list of all the videos in a playlist of a video if found, if the video isn't in a playlist returns 'No playlist found'

### find_identity.py -dsc "link"
Prints description of the video.

### find_identity.py -d "link"
Prints details of the video such as title, view count, date uploaded, like count, dislike count 
```
['Title:', 'Rick Astley - Never Gonna Give You Up (Video)', 'Views:', '918,026,549 views', 'Date:', '24 Oct 2009', 'Likes:', '9.2M', 'Dislikes: ', '272K']
```

### find_identity.py -od "link"
Prints the name of the channel and subscriber count 

```
['Channel name:', 'Official Rick Astley', 'Subscriber count:', '2.04M subscribers']
```

### find_identity.py -chnc "link"
Searches for the name of certain flagged channels and alerts the user if the link is a rickroll

## Effective searching
The program will take some time to produce output as it wait for all the web elements to be loaded, but waiting is much better than being rickrolled :D <br>
It is recommended to search for certain parameters first if you feel a link is suspicious, this will help you get results faster <br>

1. __find_identity.py -chnc "link"__, if it doesn't flag then move to [2].
2. __find_identity.py -t "link"__
3. __find_identity.py -mc "link"__
4. __find_identity.py -c "link"__
5. __find_identity.py -cmt "link"__
5. __find_identity.py -pl "link"___
6. __find_identity.py -plv "link"__
7. __find_identity.py -dsc "link"__
8. __find_identity.py -d "link"__
9. __find_identity.py -od "link"__
