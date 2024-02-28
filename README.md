
# YTL Power Stock and News Sentiment Analysis

## Project Description
This project involves the analysis of YTL Power's stock performance over a period of one year. 
Additionally, sentiment analysis was performed on news articles related to the stock, using the TextBlob library, to assess the general sentiment around the company's news.

## Installation
To run the notebooks, ensure you have Jupyter Notebook or JupyterLab installed. You can install the necessary libraries by running:
```bash
pip install pandas matplotlib textblob
```

## Usage
Seperated Django website in ads_miniproject folder and Jupyter notebook in base folder.
To analyze the stock data, run the `ytl_stock_analysis.ipynb` notebook. 
For news sentiment analysis, run the `news_scraping.ipynb` notebook.

## Screenshoots
- This is the home page when you first start in local host http://127.0.0.1:8000/ <br />
![Home Page before login](https://github.com/tecnatjy/dse-mini-project-web-scrapping/blob/dev/ads_miniproject/static/Screenshot%202024-02-28%2014194-8.png)<br />
- Go to the login page, if you do not have any account, please click on the Register button.
![Login page](https://github.com/tecnatjy/dse-mini-project-web-scrapping/blob/dev/ads_miniproject/static/Screenshot%202024-02-28%2014201-5.png)<br />
- Register a new account with a alphanumeric password that is more than 8 characters.
![Registration page](https://github.com/tecnatjy/dse-mini-project-web-scrapping/blob/dev/ads_miniproject/static/Screenshot%202024-02-28%2014210-4.png)<br />
- Type in the username and password that you register for loging in to the home page.
![Login page with username and password](https://github.com/tecnatjy/dse-mini-project-web-scrapping/blob/dev/ads_miniproject/static/Screenshot%202024-02-28%20141844.png)<br />
- This if after you login with the correct username and password.
![Home Page after login](https://github.com/tecnatjy/dse-mini-project-web-scrapping/blob/dev/ads_miniproject/static/Screenshot%202024-02-28%20141917.png)

## Findings
- The stock price of YTL Power has shown an upward trend over the year.
- There were significant spikes in trading volume, which correlated with changes in the stock price.
- The sentiment analysis of the news content showed a generally positive sentiment with an average polarity score of 0.23.

## Future Improvements
Future analyses could benefit from the inclusion of news publication dates to correlate news sentiment with stock price changes more accurately. 
Additionally, more sophisticated natural language processing techniques could be employed to understand the context of the news better.

