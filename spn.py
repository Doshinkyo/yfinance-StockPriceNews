# This script will ask it's user for a stock ticker symbol and return some stock price info and the most recent news stories (5 max) available from the yfinance Python module
# Aim is to revise this script so that the Unix Timestamp (providerPublishTime) is converted to a readable date in each news article printed out
# Script requires the Python installed and the yfinance module. The module can be installed by executing the command "pip install yfinance" from a terminal

# Change History
# v0.0.1 16th December 2021 Initial version of script to retrieve 5 news stories for a stock ticker
# v0.0.2 16th December 2021 Added stock price info
# v0.0.3 17th December 2021 Error handing for “IndexError" if fewer than 5 news stories are available. Moved stock price towards the top of the script output
# v0.0.4 17th December 2021 Added logic for more natural language on price change
# v0.0.5 20th December 2021 Achieved aim of making Unix TimeStamps readable and replaced keys from dictionary with formatted titles e.g. "title" became "Headline"
# v0.0.6 20th December 2021 Adedd error handling for invalid ticker entry and bespoke message for stocks with no news (untested feature).

# Import required modules
import yfinance as yf

# Module for readable unix timestamp conversion
from datetime import datetime

print("\n ***** Stock Price & News Version 0.0.5 Written by http://ResonanceIT.co.uk *****\n")

# Ask the user to enter a Stock symbol and store it in the "choice" variable
choice = input("Enter a Ticker symbol to retrieve news and stock price info for a company\n\n")

# Store the entered stock ticker as the variable "stock"

stock = yf.Ticker(choice)

# Store the company name for the user supplied ticker in the variable "shortname" and erro handle if an invalid ticker was chosen
try: 
    shortname = stock.info["shortName"]
except KeyError:
    print("\nNo Stock matching the symbol " + "'" + choice + "'" + " was found. Please try again.\n\n")
    exit()

# Get current and previous day's close stock prices as well as the local currency for the stock
price = round(float(stock.info["regularMarketPrice"]), 2)
closingPrice = float(stock.info["previousClose"])
localCurr = stock.info["currency"]

# Display the current stock price
print("\nThe current stock price for " + shortname + " is:", end=" ")
print(price, end=" ")
print(localCurr)

# Display the last closing price
print("Yesterday the stock closed at:", end=" ")
print(closingPrice, end=" ")
print(localCurr)

# Calculate the difference between the current price and yesterdays closing prices as a percentage change and if it's increased or decreased
diff = round((price / closingPrice - 1)*100, 2)
stringDiff = str(diff)

# Create a string to describe the change in price over the past day based on increase, decrease or no change in price and print a true statement
if diff == 0:
    condString = "Since the last market close" + stock + "'s price has changed by 0.00%"
    print(condString)
elif diff < 0:
    condString = "decreased"
    print("In the last day the price has " + condString + " by " + stringDiff + "%")
else:
    condString = "increased"
    print("In the last day the price has " + condString + " by " + stringDiff + "%")

# Heading for the news articles which are to be returned
print("\n" + "The most recent news stories, accessible from Yahoo Finance, for: " + shortname + " are:\n")

# Create a variable to store the news articles which are in the format of a list of dictionaries in yfinance
news = stock.news

# Error handling in case no news items are found
try: 
    article_0 = dict(news[0])
except IndexError:
    article_0 = "No News"

try: 
    article_1 = dict(news[1])
except IndexError:
    article_1 = "No News"

try: 
    article_2 = dict(news[2])
except IndexError:
    article_2 = "No News"

try: 
    article_3 = dict(news[3])
except IndexError:
    article_3 = "No News"

try: 
    article_4 = dict(news[4])
except IndexError:
    article_4 = "No News"

def no_news():
    if article_0 == ("No News") and article_1 == ("No News") and article_2 == ("No News") and article_3 == ("No News") and article_4 == ("No News"):
        print("There is no recent news available via Yahoo Finance for this company.")

# Select the keys inside each of the lists to include in the news article print out and print each list of articles separated by a line break
# Expanded in v0.0.5 to include formatted and bespoke Keys and formatting of the Unix TimeStamp
# First Article
dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
wanted_keys_0 = ("title","publisher","link","providerPublishTime")
article_0_result = dictfilt(article_0, wanted_keys_0)

for key, value in article_0_result.items():
    if key == ("providerPublishTime"):
        unix_timestamp = int(value)
        print("Date & Time", ":", datetime.utcfromtimestamp(unix_timestamp).strftime(" %b %d %Y @ %H:%M"))
    elif key == ("title"):
        print("Headline", '   : ', value)
    elif key == ("publisher"):
        print("Publisher", '  : ', value)
    elif key == ("link"):
        print("Web Link", '   : ', value)
print("\n")

dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
wanted_keys_1 = ("title","publisher","link","providerPublishTime")
article_1_result = dictfilt(article_1, wanted_keys_1)
for key, value in article_1_result.items():
    if key == ("providerPublishTime"):
        unix_timestamp = int(value)
        print("Date & Time", ":", datetime.utcfromtimestamp(unix_timestamp).strftime(" %b %d %Y @ %H:%M"))
    elif key == ("title"):
        print("Headline", '   : ', value)
    elif key == ("publisher"):
        print("Publisher", '  : ', value)
    elif key == ("link"):
        print("Web Link", '   : ', value)
print("\n")

dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
wanted_keys_2 = ("title","publisher","link","providerPublishTime")
article_2_result = dictfilt(article_2, wanted_keys_2)
for key, value in article_2_result.items():
    if key == ("providerPublishTime"):
        unix_timestamp = int(value)
        print("Date & Time", ":", datetime.utcfromtimestamp(unix_timestamp).strftime(" %b %d %Y @ %H:%M"))
    elif key == ("title"):
        print("Headline", '   : ', value)
    elif key == ("publisher"):
        print("Publisher", '  : ', value)
    elif key == ("link"):
        print("Web Link", '   : ', value)
print("\n")

dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
wanted_keys_3 = ("title","publisher","link","providerPublishTime")
article_3_result = dictfilt(article_3, wanted_keys_3)
for key, value in article_3_result.items():
    if key == ("providerPublishTime"):
        unix_timestamp = int(value)
        print("Date & Time", ":", datetime.utcfromtimestamp(unix_timestamp).strftime(" %b %d %Y @ %H:%M"))
    elif key == ("title"):
        print("Headline", '   : ', value)
    elif key == ("publisher"):
        print("Publisher", '  : ', value)
    elif key == ("link"):
        print("Web Link", '   : ', value)
print("\n")

dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
wanted_keys_4 = ("title","publisher","link","providerPublishTime")
article_4_result = dictfilt(article_4, wanted_keys_4)
for key, value in article_4_result.items():
    if key == ("providerPublishTime"):
        unix_timestamp = int(value)
        print("Date & Time", ":", datetime.utcfromtimestamp(unix_timestamp).strftime(" %b %d %Y @ %H:%M"))
    elif key == ("title"):
        print("Headline", '   : ', value)
    elif key == ("publisher"):
        print("Publisher", '  : ', value)
    elif key == ("link"):
        print("Web Link", '   : ', value)
print("\n")
