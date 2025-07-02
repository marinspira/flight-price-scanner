# Flight Price Scraper

This project is an **automated flight price scraper** using Selenium WebDriver with Microsoft Edge. It navigates to Google Flights URLs for predefined routes and extracts flight prices for up to 60 different dates, printing the information in the console.

## Features

- Automatically navigates to Google Flights pages for specific routes.
- Interacts with dynamic page elements (date selection).
- Extracts available flight prices and their corresponding dates.
- Limits extraction to the first 60 dates to avoid overloading.
- Uses `webdriver_manager` to automatically manage the Edge driver installation.

## Technologies Used

- Python 3
- Selenium WebDriver
- Microsoft Edge Chromium Driver
- Webdriver Manager for driver setup automation

## How to Use

- Make sure you have Python 3 installed.
   ```bash
   source venv/bin/activate
   pip install selenium webdriver-manager
   python trip.py
   ```