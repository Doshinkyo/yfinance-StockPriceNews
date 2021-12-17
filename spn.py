# This script will ask it's user for a stock ticker symbol and return some stock price info and the most recent news stories (5 max) available from the yfinance Python module
# Aim is to revise this script so that the Unix Timestamp (providerPublishTime) is converted to a readable date in each news article printed out
# Script requires the Python installed and the yfinance module. The module can be installed by executing the command "pip install yfinance" from a terminal

# Change History
# v0.0.1 16th December 2021 Initial version of script to retrieve 5 news stories for a stock ticker
# v0.0.2 16th December 2021 Added stock price info
# v0.0.3 17th December 2021 Error handing for “IndexError" if fewer than 5 news stories are available. Moved stock price towards the top of the script output
# v0.0.4 17th December 2021 Added logic for more natural language on price change

# Import required modules
import yfinance as yf

# Module not required in current version of the script
# from datetime import datetime

print("\n ***** Stock Price & News Version 0.0.4 Written by http://ResonanceIT.co.uk *****\n")

# Ask the user to enter a Stock symbol and store it in the "choice" variable
choice = input("Enter a Ticker symbol to retrieve news and stock price info for a company\n\n")

# Store the entered stock ticker as the variable "stock"
stock = yf.Ticker(choice)

# Store the company name for the user supplied ticker in the variable "shortname"
shortname = stock.info["shortName"]

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
print("\n" + "Most recent news stories accessible from Yahoo Finance for: " + shortname + " are:\n")

# Create a variable to store the news articles which are in the format of a list of dictionaries in yfinance
news = stock.news

# Break the 'list of dictionaries' from the "news" variable into 5 individual un-nested lists so that they can have their keys and values broken out onto individual lines
try: 
    article0 = dict(news[0])
except IndexError:
    article0 = "No News"

try: 
    article1 = dict(news[1])
except IndexError:
    article1 = "No News"

try: 
    article2 = dict(news[2])
except IndexError:
    article2 = "No News"

try: 
    article3 = dict(news[3])
except IndexError:
    article3 = "No News"

try: 
    article4 = dict(news[4])
except IndexError:
    article4 = "No News"

# Select the keys inside each of the lists to include in the news article print out and print each list of articles separated by a line break
# First Article
dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
wanted_keys0 = ("title","publisher","link","providerPublishTime")
article0result = dictfilt(article0, wanted_keys0)
for key, value in article0result.items():
    print(key, ' : ', value)
print("\n")

# Second Article
dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
wanted_keys1 = ("title","publisher","link","providerPublishTime")
article1result = dictfilt(article1, wanted_keys1)
for key, value in article1result.items():
    print(key, ' : ', value)
print("\n")

# Third Article
dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
wanted_keys2 = ("title","publisher","link","providerPublishTime")
article2result = dictfilt(article2, wanted_keys2)
for key, value in article2result.items():
    print(key, ' : ', value)
print("\n")

# Fourth Article
dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
wanted_keys3 = ("title","publisher","link","providerPublishTime")
article3result = dictfilt(article3, wanted_keys3)
for key, value in article3result.items():
    print(key, ' : ', value)
print("\n")

# Fith Article
dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
wanted_keys4 = ("title","publisher","link","providerPublishTime")
article4result = dictfilt(article4, wanted_keys4)
for key, value in article4result.items():
    print(key, ' : ', value)
print("\n")
