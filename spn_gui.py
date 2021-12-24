# -*- coding: utf-8 -*-
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
# v1.0.0 22nd Decemner 2021 Wrapped the inputs and outputs in tkinter to produce a GUI.
# v1.1.0 24th December 2021 Deleted clear button. Added focus to entry, bound <Enter> to data retrieval + multiple UI enhancements

# Import required modules
import tkinter as tk
from tkhtmlview import HTMLLabel
import yfinance as yf
from datetime import datetime

# Main window
window = tk.Tk()
window.iconbitmap("icon.ico") # Icon for app

# Create a function which will output data to the "Price" label
def retrieve_price_data():
    choice = ticker_input.get() # try defining as global along with "news"
    stock = yf.Ticker(choice) # try defining as global along with "news"

    try: 
        shortname = stock.info["shortName"] # try defining as global along with "news" and retype this line to just read "stock.info["shortName"]"
    except KeyError:
        null_ticker=("\nNo Stock matching the symbol " + "'" + choice + "'" + " was found.\n\n")
        price_pane["text"] = null_ticker
        status_bar["text"] = "Please try again."
    
    price_strapline = ("$" + choice + " (" + shortname + ") Price Data:\n\n")

    # Get current and previous day's close stock prices as well as the local currency for the stock
    price = round(float(stock.info["regularMarketPrice"]), 2)
    price_str = str(price)
    closing_price = float(stock.info["previousClose"])
    closing_price_str = str(closing_price)
    local_curr = stock.info["currency"]

    # Display the current stock price
    current_price_intro = ("The current stock price for ") # followed by the variable "shortname"
    the_word_is = (" is: ") # followed by variables "price" and "local_curr"
    
    # Display the last closing price
    new_line = ("\n")
    previous_close_intro = ("Yesterday the stock closed at: ")

    # Calculate the difference between the current price and yesterdays closing prices as a percentage change and if it's increased or decreased
    diff = round((price / closing_price - 1)*100, 2)
    string_diff = str(diff)

    # Create a string to describe the change in price over the past day based on increase, decrease or no change in price and print a true statement
    if diff == 0:
        cond_string = ("Since the last market close" + stock + "'s price has changed by 0.00%")
    elif diff < 0:
        cond_string = ("In the last day the price has decreased by " + string_diff + "%")
    else:
        cond_string = ("In the last day the price has increased by " + string_diff + "%")

    price_pane["text"] = price_strapline + current_price_intro + shortname + the_word_is + price_str + local_curr + new_line + previous_close_intro + closing_price_str + new_line + cond_string

# Create a function which will output data to the "News" label
def retrieve_news_data():
    
    choice = ticker_input.get() # try defining as global along with "news"
    stock = yf.Ticker(choice) # try defining as global along with "news"
    try: 
        shortname = stock.info["shortName"] # try defining as global along with "news" and retype this line to just read "stock.info["shortName"]"
    except KeyError:
        print("\nNo Stock matching the symbol " + "'" + choice + "'" + " was found. Please try again.\n\n")
    
    # Heading for the news articles which are to be returned
    news_strapline=("$" + choice + " (" + shortname + ") News Articles:\n\n")

    # Create a variable to store the news articles which are in the format of a list of dictionaries in yfinance
    pub_dict = stock.get_news()

    # Error handling in case fewer than 5 news items are found
    try: 
        article_0 = dict(pub_dict[0])
    except IndexError:
        article_0 = "No News"

    try: 
        article_1 = dict(pub_dict[1])
    except IndexError:
        article_1 = "No News"

    try: 
        article_2 = dict(pub_dict[2])
    except IndexError:
        article_2 = "No News"

    try: 
        article_3 = dict(pub_dict[3])
    except IndexError:
        article_3 = "No News"

    try: 
        article_4 = dict(pub_dict[4])
    except IndexError:
        article_4 = "No News"

    # Error handing in case no news items are found (untested - commented out)
    # def no_news():
    #     if article_0 == ("No News") and article_1 == ("No News") and article_2 == ("No News") and article_3 == ("No News") and article_4 == ("No News"):
    #         print("There is no recent news available via Yahoo Finance for this company.")

    # Select the keys inside each of the lists to include in the news article print out and print each list of articles separated by a line break
    # Expanded in v0.0.5 to include formatted and bespoke Keys and formatting of the Unix TimeStamp
    # First Article
    dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
    wanted_keys_0 = ("title","publisher","link","providerPublishTime")
    article_0_result = dictfilt(article_0, wanted_keys_0)

    for key, value in article_0_result.items():
        if key == ("providerPublishTime"):
            unix_timestamp = int(value)
            publish_date_intro_0 = ("Date & Time :")
            date_time_result_0 = datetime.utcfromtimestamp(unix_timestamp).strftime(" %b %d %Y @ %H:%M")
        elif key == ("title"):
            headline_0 = ("\nHeadline : ")
            headline_value_0 = (value)
        elif key == ("publisher"):
            publisher_0 = ("\nPublisher : ")
            publisher_value_0 = (value)
        elif key == ("link"):
            web_link_0 = ("\nWeb Link : ")
            web_link_value_0 = (value)

    dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
    wanted_keys_1 = ("title","publisher","link","providerPublishTime")
    article_1_result = dictfilt(article_1, wanted_keys_1)

    for key, value in article_1_result.items():
        if key == ("providerPublishTime"):
            unix_timestamp = int(value)
            publish_date_intro_1 = ("\n\nDate & Time :")
            date_time_result_1 = datetime.utcfromtimestamp(unix_timestamp).strftime(" %b %d %Y @ %H:%M")
        elif key == ("title"):
            headline_1 = ("\nHeadline : ")
            headline_value_1 = (value)
        elif key == ("publisher"):
            publisher_1 = ("\nPublisher : ")
            publisher_value_1 = (value)
        elif key == ("link"):
            web_link_1 = ("\nWeb Link : ")
            web_link_value_1 = (value)

    dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
    wanted_keys_2 = ("title","publisher","link","providerPublishTime")
    article_2_result = dictfilt(article_2, wanted_keys_2)

    for key, value in article_2_result.items():
        if key == ("providerPublishTime"):
            unix_timestamp = int(value)
            publish_date_intro_2 = ("\n\nDate & Time :")
            date_time_result_2 = datetime.utcfromtimestamp(unix_timestamp).strftime(" %b %d %Y @ %H:%M")
        elif key == ("title"):
            headline_2 = ("\nHeadline : ")
            headline_value_2 = (value)
        elif key == ("publisher"):
            publisher_2 = ("\nPublisher : ")
            publisher_value_2 = (value)
        elif key == ("link"):
            web_link_2 = ("\nWeb Link : ")
            web_link_value_2 = (value)

    dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
    wanted_keys_3 = ("title","publisher","link","providerPublishTime")
    article_3_result = dictfilt(article_3, wanted_keys_3)

    for key, value in article_3_result.items():
        if key == ("providerPublishTime"):
            unix_timestamp = int(value)
            publish_date_intro_3 = ("\n\nDate & Time :")
            date_time_result_3 = datetime.utcfromtimestamp(unix_timestamp).strftime(" %b %d %Y @ %H:%M")
        elif key == ("title"):
            headline_3 = ("\nHeadline : ")
            headline_value_3 = (value)
        elif key == ("publisher"):
            publisher_3 = ("\nPublisher : ")
            publisher_value_3 = (value)
        elif key == ("link"):
            web_link_3 = ("\nWeb Link : ")
            web_link_value_3 = (value)

    dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
    wanted_keys_4 = ("title","publisher","link","providerPublishTime")
    article_4_result = dictfilt(article_4, wanted_keys_4)

    for key, value in article_4_result.items():
        if key == ("providerPublishTime"):
            unix_timestamp = int(value)
            publish_date_intro_4 = ("\n\nDate & Time :")
            date_time_result_4 = datetime.utcfromtimestamp(unix_timestamp).strftime(" %b %d %Y @ %H:%M")
        elif key == ("title"):
            headline_4 = ("\nHeadline : ")
            headline_value_4 = (value)
        elif key == ("publisher"):
            publisher_4 = ("\nPublisher : ")
            publisher_value_4 = (value)
        elif key == ("link"):
            web_link_4 = ("\nWeb Link : ")
            web_link_value_4 = (value)


    news_pane["text"] = news_strapline + publish_date_intro_0 + date_time_result_0 + headline_0 + headline_value_0 + publisher_0 + publisher_value_0 + web_link_0 + web_link_value_0 + \
        publish_date_intro_1 + date_time_result_1 + headline_1 + headline_value_1 + publisher_1 + publisher_value_1 + web_link_1 + web_link_value_1 + \
            publish_date_intro_2 + date_time_result_2 + headline_2 + headline_value_2 + publisher_2 + publisher_value_2 + web_link_2 + web_link_value_2 + publish_date_intro_3 + \
              date_time_result_3 + headline_3 + headline_value_3 + publisher_3 + publisher_value_3 + web_link_3 + web_link_value_3 + publish_date_intro_4 + \
                date_time_result_4 + headline_4 + headline_value_4 + publisher_4 + publisher_value_4 + web_link_4 + web_link_value_4
   
    status_bar.configure(text="$" + choice + " (" + shortname + ") Stock Price & News Retrieved")

# Retrieve Price and News data when the enter key is selected
def do_it(event):
    status_bar["text"] = "Retrieving Data!"
    retrieve_price_data()
    retrieve_news_data()
window.bind('<Return>', do_it)

# MAIN APPLICATION WINDOW

# Give the application a name and set it's size
window.title("Stock Price & News")
window.geometry("900x840")
# window.configure(bg="#999999")
# window.overrideredirect(True)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=3)
window.rowconfigure(1, weight=7)
window.rowconfigure(2, weight=30)
window.rowconfigure(3, weight=1)

# SECTIONS OF THE APP WINDOW

frame_0=tk.Frame(window, borderwidth=1, relief="ridge") # Top frame containing search elements
frame_1=tk.Frame(window, borderwidth=1, relief="ridge") # Price data pane
frame_2=tk.Frame(window, borderwidth=1, relief="ridge") # News data pane
frame_3=tk.Frame(window, borderwidth=1) # Status bar

# Configure the frames
frame_0.grid(row=0, columnspan=3, sticky="NSEW", ipadx=5, padx=5, pady=5)
frame_1.grid(row=1, columnspan=3, sticky="NSEW", ipadx=5, padx=5)
frame_2.grid(row=2, columnspan=3, sticky="NSEW", ipadx=5, padx=5, pady=5)
frame_3.grid(row=3, columnspan=3, sticky="NSEW", ipadx=5, padx=5)

# Create a ticker label and control its behavior
lbl_0 = tk.Label(text="Enter A Ticker :")
lbl_0.grid(row=0, column=0, columnspan=1, padx=5, pady=5, ipadx=5, ipady=5)

# Create a ticker input field and control its behavior
ticker_input = tk.Entry(text="")
ticker_input.grid(row=0, column=1, columnspan=1, sticky=tk.E + tk.W, padx=5, pady=5)
ticker_input.focus()

# Create a search button and control its behavior
search_btn = tk.Button(borderwidth=1, relief="ridge", text="Search", command=lambda:[retrieve_price_data(),retrieve_news_data()], bg="#DFDFDF")
search_btn.grid(row=0, column=2, columnspan=1, sticky=tk.E + tk.W, padx=45, ipadx=0, ipady=6)

# Create a price lael and control its behavior
price_pane = tk.Label(text="Price Info Will Be Shown Here")
price_pane.grid(row=1, column=0, columnspan=3, sticky=tk.N, padx=1, pady=10, ipadx=5, ipady=5)

# Create a price lael and control its behavior
news_pane=tk.Label(text="News Articles Will Be Shown Here")
news_pane.grid(row=2, column=0, columnspan=3, sticky=tk.N, padx=1, pady=10, ipadx=5, ipady=5)

# Add a status bar to the applicaiton
status_bar = tk.Label(text="Ready For User Input")
status_bar.grid(row=3, column=1, columnspan=1, sticky=tk.W + tk.N, ipadx=5, ipady=7)

# Application Decoration
logo=HTMLLabel(height=1, width=15, html='<a style="font-size: 8px;color:black;text-decoration:none;text-align:right" href="http://ResonanceIT.co.uk">www.resonanceit.co.uk</a>')
logo.grid(row=3, column=2, rowspan=1, columnspan=1, sticky=tk.E + tk.W + tk.N, ipadx=5, ipady=5)

# TEST STRINGS FOR MAKING NEWS URL's ACTIVE IN LATER RELEASE
# news_url_prefix=('<a style="font-size: 8px;color:black;text-decoration:none;text-align:right" href="')
# news_article_url=("http://resonanceit.co.uk")
# news_url_appendix=('">www.resonanceit.co.uk</a>')
# melange=(news_url_prefix + news_article_url + news_url_appendix)
# print(melange)

# End of app
window.mainloop()
