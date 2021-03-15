from distutils.core import setup

setup(
  name = 'WeekdayChallenge',        
  packages = ['WeekdayChallenge'], 
  version = '0.1',    
  license='MIT',  
  description = 'A small python script to scrape github and fetch the latest beginner-py.com weekday challenge!',
  author = 'Pioyi',                   
  author_email = 'katiforis@outlook.com',  
  url = 'https://github.com/pioyi/WeekdayChallengeScraper', 
  download_url = 'https://github.com/pioyi/WeekdayChallengeScraper/archive/v_01.tar.gz',
  keywords = ['beginnerpy', 'automation'], 
  install_requires = [       
    'requests',
    'beautifulsoup4',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',  
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)