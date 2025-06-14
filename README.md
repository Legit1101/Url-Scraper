![URL Scraper](https://github.com/Legit1101/Url-Scraper/blob/main/Url-Scraper.png)

# Url-Scraper
URL Scraper Tool — A lightweight script to extract all links from a webpage. Use it for SEO, bug bounty, penetration testing, or data collection. Saves links in TXT or CSV format for easy reuse, saving you time and simplifying your workflow.

# URL Scraper Tool

URL Scraper Tool — Extract all links from a webpage.

## Description

URL Scraper Tool lets you extract all links from a webpage.  
It parses the HTML of a webpage and saves links to a text or CSV file.

## Installation

git clone https://github.com/Legit1101/Url-Scraper.git

cd urlscraper

pip install -r requirements.txt

## Usage

python3 urlscraper.py -u http://example.com -o links.txt -c links.csv

## Command-Line Arguments:

 -h, --help            show this help message and exit
 
 -f, --file FILE       File with URLs to scan (each on a new line)
 
 -u, --url URL         Single URL to scan (if not using --file)
 
 -r, --threads THREADS
                        Number of threads for faster scanning (default 5)
                        
 -o, --output OUTPUT   File to save links in TXT format
 
 -c, --csv CSV         File to save links in CSV format
 
 -j, --json JSON       File to save links in JSON format
 
 -t, --report          Generate a report after scanning

Example: python3 urlscraper.py -f urls.txt -r 10 -o links.txt -c links.csv -j links.json -t

## Credit:

Tool by LEGIT
Instagram: @th3cyberside
LinkedIn: https://www.linkedin.com/in/krishna-patwa/
