# CS5830 Final Project - NBA All Star Analysis

**Group 7**

Jeremy Young

Siddharth Bhawsar

Gavin Eddington

## Web Scraper

Our [basketball-reference.com](https://basketball-reference.com) web scraper is located under the [basketball_scraper](./basketball_scraper/) directory. After installing the appropriate library (`pip install scrapy`) you can call `scrapy crawl stats` to generate the dataset yourself. The dataset contains game stats for every NBA player throughout every season played. 

## Wikipedia Script

To generate our "popularity" dataset, we used the `pageviewapi` to gather the average page visits in the last 30 days for every player's Wikipedia page. After installing the correct library (`pip install pageviewapi`), run the script (`python wikipageviews.py`) to generate the dataset.