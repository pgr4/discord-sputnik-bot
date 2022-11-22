import os
import discord
from discord.ext import commands
from http_requests import make_request
from discord_formatter import send_in_codeblock, clean_command
from yt_music import get_album_info
import re

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='sputnik',intents=intents)
bot.remove_command('help')

class ArtistResult:
    def __init__(self, artist_name, album_title, a, rating, number_of_votes):
        self.artist_name = artist_name
        self.album_title = album_title
        self.a = a
        self.rating = rating
        self.number_of_votes = number_of_votes
    
    def __str__(self) -> str:
        if self.rating < 1.75:
            return f'The people have spoken; {self.artist_name}\'s album "{self.album_title}" is trash. Rating: {str(self.rating)} with {str(self.number_of_votes)} Votes'
        elif self.rating < 2.5:
            return f'{self.artist_name}\'s album "{self.album_title}" sucks. Rating: {str(self.rating)} with {str(self.number_of_votes)} Votes'
        elif self.rating < 3:
            return f'{self.artist_name}\'s album "{self.album_title}" is mid. Rating: {str(self.rating)} with {str(self.number_of_votes)} Votes'
        elif self.rating < 3.5:
            return f'{self.artist_name}\'s album "{self.album_title}" is dece. Rating: {str(self.rating)} with {str(self.number_of_votes)} Votes'
        elif self.rating < 4:
            return f'{self.artist_name}\'s album "{self.album_title}" is A tier. Rating: {str(self.rating)} with {str(self.number_of_votes)} Votes'
        elif self.rating < 4.25:
            return f'{self.artist_name}\'s album "{self.album_title}" is nearly GOATed. Rating: {str(self.rating)} with {str(self.number_of_votes)} Votes'
        else:
            return f'{self.artist_name}\'s album "{self.album_title}" is GOATed. Rating: {str(self.rating)} with {str(self.number_of_votes)} Votes'

def href_clean(value: str):
    return re.sub('[^0-9a-zA-Z]+', '', value)

def get_href(artist_name: str, album_title: str) -> str:
    return f'{href_clean(artist_name)}{href_clean(album_title)}'.lower()

def get_matching_a(artist_name: str, album_title: str) -> ArtistResult:
    band_request = make_request(f'https://www.sputnikmusic.com/search_results.php?search_in=Bands&search_text={artist_name}')
    a_match = None
    for a in band_request.find_all('a', href=True):
        if get_href(artist_name, album_title) in href_clean(a['href']).lower():
            # Ignore the image link
            if a.next_element.name == 'font':
                rating = float(a.find_parent('td').find('table').find('b').text)
                number_of_votes = int(a.find_parent('td').find('table').find_all('font')[1].text.replace('Votes', '').replace(',', '').strip())
                return ArtistResult(artist_name, album_title, a, rating, number_of_votes)
    return None

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Example Command = 'sputnikrating illmatic'
@bot.command(name='rating')
async def on_get_sputnik_rating(command):
    album_info = get_album_info(clean_command(command))
    
    album_title = album_info['title']
    artist_name = album_info['artists'][0]['name']
    
    result = get_matching_a(artist_name, album_title)
             
    if result != None:
       await send_in_codeblock(command, str(result)) 
    else:
        print(f'Not Found {artist_name} - "{album_title}"')  


# Example Command = 'sputnikreview illmatic'
@bot.command(name='review')
async def on_get_sputnik_rating(command):
    album_info = get_album_info(clean_command(command))
    
    album_title = album_info['title']
    artist_name = album_info['artists'][0]['name']
    
    result = get_matching_a(artist_name, album_title)
    
    album_href = result.a['href']
    
    # we need to go to the href
    # Example: https://www.sputnikmusic.com/review/46056/Nas-Illmatic/
    album_request = make_request(f'https://www.sputnikmusic.com{album_href}')
    
    # Should probably grab the rating & the loser who took the time to review this    
    review_text = album_request.find('div', {'id': 'leftColumn'})
    
    if len(review_text) > 1990:
        await send_in_codeblock(command, f'{review_text.text[:1990]}...') 
    else:
        await send_in_codeblock(command, review_text.text[:1990]) 
    
    

    
bot.run(TOKEN)