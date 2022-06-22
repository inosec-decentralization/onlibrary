

import sqlite3

def reverse(lst):
    return [ele for ele in reversed(lst)]

class get_db():
    def __init__(self):
        self.conn_ = sqlite3.connect('database/data.db')

    def in_db(self, data):
        self.data_ = str(data)
        if 1==1:#try:
            cursor = self.conn_.cursor()
            #cursor.execute('create table search (sno text not null, data text not null)')
            cursor.execute("insert into search values(?, ?)", ('.', self.data_))
            self.conn_.commit()
            self.conn_.close()
            return True
        
        #except: return False

    def out_db(self):
        try:
            cursor = self.conn_.cursor()
            cursor.execute("select data from search where sno='.'")
            data = cursor.fetchall()
            self.conn_.close()
            if len(data) != 0:
                # reverse the list
                data_ = reverse(data)
                return data_
            else:
                return False
        except: return None


class search():
    def __init__(self, keyword):
        self.keyword = keyword

    def google_search(keyword):
        link = []
        try:
            for j in search (query, lang='en', tbs='0', safe='off', num=40, start=0, stop=41, pause=2.0, extra_params=None, user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"):
                link.append(str(j))
        except: None
        return link

    def get_result(self):
        links = google_search(self.keyword)
        
        if len(links) != 0:
            return res
        else: return None

'''
def sear():
    
    s = ['chemical enginerring book', 'mechanical enginerring book', 'industrial enginerring book', 'civil enginerring book', 'electrical enginerring book', 'aerospace enginerring book', 'aeronautics enginerring book', 'technology']
    for i in range(0, len(s)):
        name = s[i] + ".html"
        query = str(s[i]) + " filetype:pdf"
        f = open(name, 'w')
        f.write(htm)
        f.close()
        print("\n\n\n" + s[i] + "\n--------------\n")
        for j in search (query, lang='en', tbs='0', safe='off', num=100, start=0, stop=100, pause=2.0, extra_params=None, user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"):
            herf = '<a href="' + str(j) + '" class="hero-bun">book</a>'
            print(herf)
'''
