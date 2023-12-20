import requests
from bs4 import BeautifulSoup
import sys
import pyperclip

def translate_word(word):
    url = f"http://tahlilgaran.org/TDictionary/WebApp/?q={word}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        translation_div = soup.find('div', class_='p-fa')
        if translation_div:
            return translation_div.get_text(strip=True)
        else:
            return "No translation found."
    else:
        return "Error in fetching data."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        word = sys.argv[1]
        translation = translate_word(word)
        print(translation)
        pyperclip.copy(translation)
        #print("Translation copied to clipboard.")
    else:
        print("No word provided for translation.")
