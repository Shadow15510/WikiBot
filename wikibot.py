# --------------------------------------------------
# WikiBot (Version 1.2)
# by Sha-Chan~
# last version released on the 31 of July 2020
#
# code provided with licence :
# GNU General Public Licence v3.0
# --------------------------------------------------

import discord
import os
import wikilib as wl
from random import randint

client = discord.Client()
token = os.environ["token"]


def make_embed(title, description, field, color = randint(0, 16777215), image = None, in_line = False):
 
  answer = discord.Embed(title=title, description=description, color=color)

  for i in field:
    answer.add_field(name=i[0], value=i[1], inline=in_line)
    
  if image:
    answer.set_image(url=image)
  return answer

@client.event
async def on_message(message):
  msg_content, rep = message.content, None
  
  if message.author == client.user or msg_content[0] != "/": return None

  msg_content = list(msg_content[1:].partition("#"))

  msg_content[0] = msg_content[0].rstrip()

  language = msg_content[2].replace(" ", "")
  
  if not language:
    language = "en"
  wl.wikipedia.set_lang(language)

  if not msg_content[0].find("r "):
    rep = make_embed(*wl.page_random(msg_content[0][2:]))
    
  elif not msg_content[0].find("a "):
    rep = make_embed(*wl.page_read(msg_content[0][2:]))

  elif not msg_content[0].find("s "):
    rep = make_embed(*wl.page_search(msg_content[0][2:]))

  elif not msg_content[0].find("t "):
    rep = make_embed(wl.translation(msg_content[0][2:], language), True)

  elif not msg_content[0].find("e "):
    rep = wl.eliza_call(msg_content[0][2:])

  elif msg_content[0] == "help":
    rep = discord.Embed(title="Help heading", description="List of available commands", color=randint(0, 16777215))
    rep.add_field(name="Random selection of articles", value="`/r < nb > [# < language >]`", inline=False)
    rep.add_field(name="Get an article", value="`/a < title > [# < language >]`", inline=False)
    rep.add_field(name="Translate a text", value="`/t < text > [# < language >]`", inline=False)
    rep.add_field(name="Make a research on wikipedia", value="`/s < search_terms > [# < language >]`", inline=False)
    rep.add_field(name="Talk with Eliza", value="`/e < message >`", inline=False)

  if not rep: return None
  
  if type(rep) == str:
    await message.channel.send(rep)
  else:
    await message.channel.send(embed = rep)

@client.event
async def on_ready():
  print("Online.")

client.run(token)
