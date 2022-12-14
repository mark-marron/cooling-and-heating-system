from random import randint
from bs4 import BeautifulSoup
import requests


class TempSensor:

    """
    intializes variable outside_temp
    """
    def __init__(self):
        self._temp = None
        self._outside_temp = randint(0, 30)

    '''
    Uses a web crawler to get the current temperature in cork city and returns this value
    '''
    def get_outside_temp(self):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/58.0.3029.110 Safari/537.3 '
                }
        req = requests.get(
           f'https://www.google.com/search?q=+cork+weather+&oq=+cork+weather+&aqs=chrome.0.35i39l2j0l4j46j69i60'
           f'.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
        
        soup = BeautifulSoup(req.text, 'html.parser')
        temperature = soup.select('#wob_tm')[0].getText().strip()
        self._temp = temperature
      
        return self._temp
