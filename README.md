# WeekdayChallengeScraper
A small python script to scrape github and fetch the latest beginner-py.com weekday challenge! 


### Sample Usage
```python
from WeekdayChallenge import WeekdayChallenge

def is_palindrome(string):
    return string == string[::-1]

challenge = WeekdayChallenge()
print(challenge.title, challenge.description)

challenge.submit(is_palindrome)
```

### Installation Via PyPi
```python
pip install WeekdayChallenge
```
