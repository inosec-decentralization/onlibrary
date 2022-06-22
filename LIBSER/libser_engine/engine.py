
import urllib3
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
from string import punctuation
from utils import payload
from utils.exception import GoogleCaptcha, GoogleCookiePolicies
from utils.agent import user_agent
import re

filetype = ('pdf','doc','xls','ppt','odp','ods','docx','xlsx','pptx')


class Extract():

	#____________________________________________
	#Duckduckgo
	#-------------------------------------------
	def duckduckgo_search(self, qury: str):
		
		self.qury = qury
		self.paylod, self.cookie = payload.Headers().duckduckgo_parm()

		link = []
		try:
			self.link = 'https://html.duckduckgo.com/html/?q=' + self.qury.replace(' ', '+') # + '&ai=software'
			req = requests.get(self.link, headers=self.paylod, allow_redirects=False, timeout=5)
			self.data = req.text
			status = req.status_code

            # data extrcation from search page
			if status == 200:
				soup = BeautifulSoup(self.data, 'html.parser')

				for link_ in soup.find_all('a', href=True):
					lnks = link_['href']

					try:
						q = lnks.split('=')[1]
						w = q.split('&rut')[0]
						escp = payload.escape_codes
						for e in escp:
							if e in w:
								w = w.replace(e, escp[e])
						link.append(w)
					
					except: None
                
				filter_link = []
				# removing a similar link
				for k in link:
					if 'duckduckgo.com'not in k:
						if k not in filter_link:
							filter_link.append(k)
				
				return filter_link
			
			elif status == 403: return False

		except: return False

	#______________________________________
	# Google API
	#-------------------------------------
	def google_search(self, target, total, filetype):
		self.word = target
		self.filetype = filetype
		self.counter = 50
		self.quantity = "100"
	
		urllib3.disable_warnings()

		documents = []
		start = 0
		num = 50 if total > 50 else total
		iterations = int(total/50)
		if (total%50) != 0:
			iterations += 1

		url_base = f"https://www.google.com"
		#cookies = {"CONSENT": "YES+srp.gws"}

		header = payload.Headers().google_parm()
		
		while (start < iterations) and (len(documents) < total):
			try:
				'''
				url = url_base + f"/search?num="+self.quantity+"&start=" + str(self.counter) + "&hl=en&meta=&q=filetype:"+self.filetype+"%20allintext:" + self.word
				
				response = requests.get(url, headers=header, timeout=5, verify=False, allow_redirects=False)
				text = response.text
				content = respomse.content
				print(text)
				
				if response.status_code == 302 and ("htps://www.google.com/webhp" in text or "https://consent.google.com" in text):
					raise GoogleCookiePolicies()
				if "detected unusual traffic" in text:
					raise GoogleCaptcha()'''
				
				f = open('duck.txt', 'r')
				content = f.read()
				f.close()
				
				soup = BeautifulSoup(content, features="lxml")
				links = soup.findAll("a")
				for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
					link = re.split(":(?=http)",link["href"].replace("/url?q=",""))
					documents.append(link)

					if len(documents) >= total:
						break

			except Exception as ex:
				raise ex #It's left over... but it stays there
			start += 1
		return documents


#print(Extract().duckduckgo_search('mental maths'))
a = Extract().google_search('india', 30, 'pdf')
for q in a:
	print(q)


#page = requests.get("https://www.google.dz/search?q=see")
#soup = BeautifulSoup(page.content)
#import re
#links = soup.findAll("a")
#for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
#	print(re.split(":(?=http)",link["href"].replace("/url?q=","")))


