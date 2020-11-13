# WikiBot (Version 1.7.9)

## General

### Presentation

WikiBot is a discord bot which makes wikipedia research, translation of texts and more…

The last version was released on the 13 of November 2020.

### License

This code was provided with license GNU General Public License v3.0.

### Adding WikiBot

For adding WikiBot to your server, please [click here](https://discord.com/api/oauth2/authorize?client_id=731043686682591263&permissions=8&scope=bot).

## Features and command

### Get a list of random articles from wikipedia

`/r number_of_random_article [& language]`

### Get the summary of an article from wikipedia

`/p name_of_article [& language]`

`/p+ name_of_the_article [& language]`
This last function apply an automatic correction on the title given.

### Make a research on wikipedia

`/s search_terms [& language]`

### Translate a text

`/t text_to_translate [& destination_language [ language]]`

### Talk with the bot (ELIZA chatbot implementation)

`/e message`

### Get the last news

`/n the_newspaper's_name [& number_of_newspaper_articles [+]]`

### Get the weather

The weather forecasts are provided by the OpenWeather's API.

`/w the_city_name [& day_of_the_forecast]`

The day parameter allow you to see the day. 0 is today, 1 tomorrow… The maximum is 7.


## language parameter

This argument allows you to choose the language of article on wikipedia or the destination language for translations. This parameter is optional, per default language is set on english. For change this, please use ISO abbreviations.

## Exemple

### Wikipedia handlings

`/r 1 & de` 
Returns a random article in german.

`/p Paris & fr`
Returns the Paris's wikipedia page in french.

If you have a doubt on the spelling of your search, use `/p+ …`.

`/s Sea`
Returns a list of wikipedia pages in english about the 'sea'.

### Translation

`/t Bonjour, je suis un bot`
Returns the text translated in english.

`/t Hi, I'm fine, nice to meet you ! & de`
Returns the text translated in german.

`/t Quomodo vales ? & en la`
Returns the translated text from latin to english.

### ELIZA chatbot

ELIZA only understand english.

`/e Hello`
Is a good way to start a conversation.

### The newspaper

`/n The Lancet`
Returns the last article of the Lancet.

`/n The Lancet & 2`
Returns the two last articles of The Lancet.

`/n The Lancet & 2+`
Returns the second article only.


### The weather

`/w Paris & 1`
Returns the weather for Paris tomorrow.
