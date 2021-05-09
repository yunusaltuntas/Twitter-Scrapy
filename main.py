from selenium  import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
class Twitter:
	def __init__(self):
		ua = UserAgent()
		userAgent = ua.random
		print(userAgent)
		chrome_options=Options()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument(f'user-agent={userAgent}')
		chrome_options.add_argument("start-maximized")
		chrome_options.add_argument("disable-infobars")
		chrome_options.add_argument("--disable-extensions")
		chrome_options.add_argument("--disable-gpu")
		chrome_options.add_argument("--disable-dev-shm-usage")
		chrome_options.add_argument("--no-sandbox")
		self.driver=webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=chrome_options)
	def explore(self,word,example=1):
		url="https://twitter.com/search?f=live&q="+word+"%20min_retweets%3A100%20until%3A2020-09-18%20since%3A2020-09-11&src=typed_query"
		self.driver.implicitly_wait(3)
		self.driver.get(url)
		page=self.driver.page_source
		with open("./text.html","w") as file:
			file.write(page)

		for i in range(example):
			self.driver.implicitly_wait(3)
			if i!=0:
				word=self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div["+str(2*i)+"]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div").text
				yield word
			try:
				word=self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div["+str(2*i+1)+"]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div").text
				yield word
			except:
				print("except",flush=True)
				html = self.driver.find_element_by_tag_name('html')
				html.send_keys(Keys.PAGE_DOWN)
			
		#html = driver.find_element_by_tag_name('html')
		#html.send_keys(Keys.PAGE_DOWN)
		page=self.driver.page_source
		"""with open("./text.html","w") as file:
			file.write(page)
		"""
if __name__ == '__main__':
	twt=Twitter()
	for i in twt.explore("bug",3):
		print(i,flush=True)