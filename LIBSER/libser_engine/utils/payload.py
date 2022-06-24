
from nltk.tokenize import RegexpTokenizer
import random
#from json import dumps


escape_codes = {
    '%20': ' ',
    '%3C': '<',
    '%23': '#',
    '%25': '%',
    '%2B': '+',
    '%7B': '{',
    '%7D': '}',
    '%7C': '|',
    '%5B': '[',
    '%5D': ']',
    '%3B': ';',
    '%2F': '/',
    '%3F': '?',
    '%3A': ':',
    '%40': '@',
    '%3D': '=',
    '%26': '&',
    '%24': '$',
    '%3E': '>',
    '%2D': '-'
}


# user-agenst
ua = {
#'android': 'LIBSER/libser_engine/utils/ua/android_webkit.txt',
2: 'LIBSER/libser_engine/utils/ua/Chrome.txt',
3: 'LIBSER/libser_engine/utils/ua/Edge.txt',
#'firefox': 'LIBSER/libser_engine/utils/ua/Firefox.txt',
#'intenet_explorer': 'LIBSER/libser_engine/utils/ua/Internet+Explorer.txt',
4: 'LIBSER/libser_engine/utils/ua/Opera.txt',
#'safari': 'LIBSER/libser_engine/utils/ua/Safari.txt'
}

sec_ch_ua = {
    2: '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"', # chrome
    3: '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"', #edge
    4: '"Opera";v="81", " Not;A Brand";v="99", "Chromium";v="95"' # opera
}

ua_edge_3 = None
ua_chrome_2 = None
ua_opera_4 = None

for user_agent in ua:
    agents_data = open(ua[user_agent]).read()
    tok = RegexpTokenizer(r'\n', gaps=True)
    agents_ = tok.tokenize(agents_data)
    if user_agent == 2:
        ua_chrome_2 = agents_
    elif user_agent == 3:
        ua_edge_3 = agents_
    elif user_agent == 4:
        ua_opera_4 = agents_


class Headers:
    def __init__(self):
        self.choose_browser = random.randint(2, 4)
        self.secchua = sec_ch_ua[self.choose_browser]

        if self.choose_browser == 2: self.header = ua_chrome_2[random.randint(0, 848)]
        elif self.choose_browser == 3: self.header = ua_edge_3[random.randint(0, 7)]
        elif self.choose_browser == 4:self.header = ua_opera_4[random.randint(0, 991)]


    def duckduckgo_parm(self):

        self.payload = {
            'Upgrade-Insecure-Requests': '1',
            'Sec-Ch-Ua': self.secchua,
            'Sec-Ch-Ua-Mobile': '?0',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': self.header,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Cache-Control': 'max-age=0',
            'Sec-Fetch-Dest': 'document',
            'Connection': 'keep-alive',
        }
        self.cookie =  cookies = {'Cookies': '-'}
        
        return self.payload, self.cookie
    
    def google_parm(self):

        self.payload = {
            'Cookie': 'YES+srp.gws',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.header,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Dest': 'document',
            'Sec-Ch-Ua': self.secchua,
            'Sec-Ch-Ua-Mobile': '?0',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive',
        }
        return self.payload
