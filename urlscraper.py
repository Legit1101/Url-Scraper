import requests
from bs4 import BeautifulSoup
import argparse
import csv
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

def extract_links(url, proxy=None):
    links = set()
    try:
        if proxy:
            response = requests.get(url, proxies=proxy, timeout=10)
        else:
            response = requests.get(url, timeout=10)

        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            links.add(a['href'])

    except Exception as e:
        print(f"Error while retrieving {url}: {e}")

    return links


def main():
    parser = argparse.ArgumentParser(
        description='URL Scraper Tool - Extract all links from multiple webpages',
        epilog='Example:\n  python3 urlscraper.py -f urls.txt -r 10 -o links.txt -c links.csv -j links.json -t'
    )
    parser.add_argument('-f', '--file', help='File with URLs to scan (each on a new line)', required=False)
    parser.add_argument('-u', '--url', help='Single URL to scan (if not using --file)', required=False)
    parser.add_argument('-r', '--threads', help='Number of threads for faster scanning (default 5)', default=5, type=int)
    parser.add_argument('-o', '--output', help='File to save links in TXT format')
    parser.add_argument('-c', '--csv', help='File to save links in CSV format')
    parser.add_argument('-j', '--json', help='File to save links in JSON format')
    parser.add_argument('-t', '--report', action='store_true', help='Generate a report after scanning')

    args = parser.parse_args()

    urls = set()

    if not args.file and not args.url:
        print("Error: Please provide a URL with -u or --url, or a file with URLs using -f or --file.")
        print("For help, use -h or --help.")
        print("\nExample:")
        print("  python3 urlscraper.py -f urls.txt -r 10 -o links.txt -c links.csv -j links.json -t")
        return

    if args.file:
        try:
            with open(args.file, 'r') as f:
                for line in f:
                    url = line.strip()
                    if url:
                        urls.add(url)
        except Exception as e:
            print(f"Error reading from {args.file}: {e}")

    if args.url:
        urls.add(args.url)

    results = {}  # {url: set(links)}
    invalid_count = 0

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_to_url = {executor.submit(extract_links, url): url for url in urls}

        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                links = future.result()
                results[url] = links
                print(f"Links found on {url}:")
                for link in links:
                    print(link)
                print()
            except Exception as e:
                print(f"Error retrieving from {url}: {e}")
                invalid_count += 1

    if args.output:
        with open(args.output, 'w') as f:
            for url, links in results.items():
                f.write(f"URL: {url}\n")
                for link in links:
                    f.write(link + '\n')
                f.write('\n')
        print(f"Links successfully saved to {args.output}")

    if args.csv:
        with open(args.csv, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['URL', 'Links'])

            for url, links in results.items():
                for link in links:
                    writer.writerow([url, link])

        print(f"Links successfully saved to CSV {args.csv}")

    if args.json:
        with open(args.json, 'w') as f:
            json.dump({url: list(links) for url, links in results.items()}, f, indent=4)
        print(f"Links successfully saved to JSON {args.json}")

    if args.report:
        report_file = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        with open(report_file, "w") as f:
            f.write("URL Scraper Report\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total URLs scanned: {len(urls)}\n")
            f.write(f"Invalid URLs: {invalid_count}\n")
            f.write("Links found per URL:\n")

            for url, links in results.items():
                f.write(f"- {url}: {len(links)} links\n")

        print(f"Report successfully saved to {report_file}")

    print("\nTool by LEGIT")
    print("Instagram: @th3cyberside")
    print("LinkedIn: https://www.linkedin.com/in/krishna-patwa/")


if __name__ == "__main__":
    main()
