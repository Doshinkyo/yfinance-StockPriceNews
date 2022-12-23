# Developed using Python 3.11.1, this app retrieves Stock price info and latest published news articles from Yahoo Finance. Users must enter a valid ticker symbol. Developed using the Modues flet & yfinance

# Import required Modules
import flet as ft
import yfinance as yf
from datetime import datetime

# Define the applicaiton
def main(page: ft.Page):

    # Apply the main pages settings 
    page.title = "Stock Price & News"
    page.window_height = 900
    page.window_width = 775

    # Create a Text field for the user to ender a ticker Symbol
    ticker_symbol = ft.TextField(label="Ticker Symbol", autofocus=True, width=550)

    # Define a function to reset the page if a user wants to  either clear the page or return results for another ticker
    def reset(r):
        page.controls.clear()
        page.add(
        ft.Row([ticker_symbol, 
        ft.ElevatedButton("Get News", on_click=btn_click),
        ft.ElevatedButton("Reset", on_click=reset)], wrap=True),
        )
        ticker_symbol.value = ""
        page.update()

    # The primary function which retrieves data from Yahoo when the "Get Data" button is pressed
    def btn_click(e):

        # Create dictionaries and variables which store news articles, ticker symbols and yahoo data for the chosen stock
        articles = []
        ticker = ticker_symbol.value
        info = yf.Ticker(ticker).info
        news = yf.Ticker(ticker_symbol.value).get_news()

        # Reset the main page, to clear out the entered ticker symbol and all data from any preveous retrieval request
        reset(reset)

        # Check the ticker entered and display some info, either to assist with errors or to detail stock price data
        ticker_checks = 0
        while ticker_checks == 0:
            if len(ticker) == 0:
                page.add(ft.Text(" "))
                page.add(ft.Text(f"You must enter a ticker symbol to retrieve Stock price and news!", weight="bold", size=18))
                page.add(ft.Text(" "))
                ticker_checks +=1
            if ticker_checks == 0 and info is None:
                page.add(ft.Text(" "))
                page.add(ft.Text(f'No info found for: "{ticker}". Displaying latest Yahoo Finance news instead.', weight="bold", size=18))
                page.add(ft.Text(" "))
                ticker_checks +=1
            if ticker_checks == 0:
                shortName = (info["shortName"])
                close = (info["regularMarketPreviousClose"])
                ask = (info["ask"])
                logo_url = (info["logo_url"])
                changeFloat = ((ask / close) - 1) * 100
                change = (round(changeFloat, 2))
                page.add(ft.Text(" "))
                page.add(ft.Text(f"Retrieving latest stock data and news for: ${ticker.upper()}", weight="bold", size=18))
                page.add(ft.Row([ft.Image(src=f"{logo_url}", width=40, height=40), ft.Text(f"{shortName} stock last closed at {close} and is now at {ask}, which represents a {change}'%' change.")], wrap=True))
                page.add(ft.Text(" "))
                ticker_checks +=1

        # Retrieve a limited number of the latest news items for the ticker
        count = 0
        while count < 5:
            try: 
                article = dict(news[count])
                articles.append(article)
                count += 1
            except IndexError:
                pass
        
        # Define a function to launch web links to artickes in a browser
        def open_url(e):
            page.launch_url(e.data)

        # Add the details for news articles to the page 
        for index in range(len(articles)):
            publish_time = articles[index]["providerPublishTime"]
            formatted_datestamp = str(datetime.utcfromtimestamp(publish_time).strftime(" %b %d %Y @ %H:%M"))
            page.add(ft.Row([ft.Text(articles[index]["publisher"], weight="bold"), ft.Text(f": Published {formatted_datestamp}.")]))
            page.add(ft.Text(articles[index]["title"]))
            page.add(ft.Markdown((articles[index]["link"]), extension_set="gitHubWeb", on_tap_link=open_url, expand=True, selectable=True))
        page.update()

    # Add the desired elements to the page
    page.add(
        ft.Row([ticker_symbol, 
        ft.ElevatedButton("Get Data", on_click=btn_click),
        ft.ElevatedButton("Reset", on_click=reset)], wrap=True),
        )

# Comment out one of the two lines below. Swich which line is commented out to change the app from loading in a browser to loading as a Desktop App. 
# ft.app(port=8888, target=main, view=ft.WEB_BROWSER)
ft.app(target=main)
