import requests
from bs4 import BeautifulSoup

class WeekdayChallenge:
    def __init__(self):
        # Initializing soup object
        self.page = requests.get("https://github.com/beginnerpy-com/challenges/tree/main/weekday")
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        
        # Collecting useful data
        self.challenge_readme = self.fetch_challenge_data()
        self.tests = self.challenge_readme.find_all("pre")[-1].text
        self.info = self.challenge_readme.text.replace(self.tests, "")
        
        self.title = self.challenge_readme.find("h1").text
        self.description = self.challenge_readme.find("p").text
        self.function_name = self.tests[(self.tests.find("def") + 4):self.tests.find("(")]
        
    def fetch_challenge_data(self):
        """ Return the challenge's README.md file as a bs4 element """
        
        # Fetching all challenge containers
        challenges = self.soup.find_all("a",  { "class": "js-navigation-open Link--primary" })
        
        # Getting the last element's text (e.g. challenge_202.md)
        challenge = challenges[-1].text
        
        # Scraping the challenge's repository
        challenge_page = requests.get(f"https://github.com/beginnerpy-com/challenges/blob/main/weekday/{challenge}")
        challenge_soup = BeautifulSoup(challenge_page.content, 'html.parser')
        
        # Returning README.md
        return challenge_soup.find("div", {"id": "readme"})
    
    def submit(self, function):
        """ Executes the challenge's tests with the provided function"""
        
        # Replacing the placeholder function's name
        tests = self.tests.replace(self.function_name, "function", 1)
        
        exec(tests, function.__globals__)