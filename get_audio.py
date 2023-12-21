import requests
from bs4 import BeautifulSoup
import pyperclip 

def download_audio(word):
    print(word)
    url = f"https://www.ldoceonline.com/dictionary/{word}"
    response = requests.get(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36'
            })
    if response.status_code != 200:
        return "Error: Unable to access the page."
    
    soup = BeautifulSoup(response.content, 'html.parser')
    audio_tag = soup.find('span', {'class': 'amefile'})
    if not audio_tag or not audio_tag.get('data-src-mp3'):
        return "Error: Audio file not found."

    audio_url = audio_tag['data-src-mp3']
    #print(audio_url)
    audio_response = requests.get(audio_url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36'
            })
    if audio_response.status_code != 200:
        return "Error: Unable to download audio file."

    file_path = f"/home/ri/Desktop/vocab/audios/{word}.mp3"
    with open(file_path, 'wb') as file:
        file.write(audio_response.content)
    
    return file_path

# Example usage
# file_path = download_audio("flesh")
# print(file_path)
 
def download_audio_from_clipboard():
    # Get word from clipboard
    word = pyperclip.paste()
    if not word:
        return "Error: No word found in the clipboard."

    # Proceed with the existing download_audio function
    return download_audio(word)

# Example usage
# file_path = download_audio_from_clipboard()
# print(file_path)

download_audio_from_clipboard()
