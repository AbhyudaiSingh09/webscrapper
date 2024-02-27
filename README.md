
```markdown
# Commodity Prices Scraper

## Overview

This project contains a Python script for scraping current commodity prices (Crude Oil, Gold, and Silver) from Yahoo Finance's trending tickers page. It utilizes Selenium for web automation and SQLite for data storage.

For an interactive experience and to run the code directly in your browser, you are encouraged to view this project on Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Axs7941/webscrapper/blob/master/webScrapper.ipynb)

## Prerequisites

Before running this script, ensure you have the following installed:
- Python 3.x
- Selenium WebDriver
- Chromium WebDriver
- SQLite3

## Installation

### Install Selenium

```bash
pip install selenium
```

### Install Chromium WebDriver

```bash
apt-get update
apt install chromium-chromedriver
cp /usr/lib/chromium-browser/chromedriver /usr/bin
```

### Setting up the Environment

Add Chromium WebDriver to your system path:

```python
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
```

## Usage

To run the script, navigate to the script's directory and execute the following command:

```bash
python webScraper.py
```

## How It Works

1. The script initializes a headless Chrome browser using Selenium.
2. It navigates to the Yahoo Finance trending tickers page.
3. The script clicks the next button on the carousel to ensure all tickers are loaded.
4. It waits for the commodity prices to be visible and then extracts their rates using regular expressions.
5. The extracted rates are written to a text file named `commodity_prices.txt`.
6. Finally, the rates are stored in an SQLite database named `CommodityDatabase.db`.

## Output

The script outputs:
- A text file `commodity_prices.txt` containing the latest rates of Crude Oil, Gold, and Silver.
- An SQLite database `CommodityDatabase.db` with a table `CommodityTable` that stores the rates.

## Troubleshooting

Ensure you have all the necessary permissions and dependencies installed. If you encounter any issues with the Selenium WebDriver, check that the version of the WebDriver matches your Chrome browser's version.
```

