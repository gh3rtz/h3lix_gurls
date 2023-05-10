import logging
import requests
import sys
from datetime import datetime
from art import text2art
from termcolor import colored
import argparse
import atexit

# Define the function to display the "Exiting..." message
def exit_handler():
    print(colored("Exiting... Bye-Bye", "red"))

# Register the exit handler function to be called when the program exits
atexit.register(exit_handler)

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# ASCII art for "Givari Hertz"
ascii_art = text2art("Givari Hertz")
instagram_handle = "Twitter: @gh3rtz    Instagram: @givarirmdn"

# Print the ASCII art and Instagram handle in green color
print(colored(ascii_art, "green"))
print(colored(instagram_handle, "green"))


def get_waybackurls(domain, output_file=None, limit=None, verbose=False, api_endpoint=None, user_agent=None, proxy=None):
    headers = {
        'User-Agent': user_agent or 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    proxies = {
        'http': proxy,
        'https': proxy
    } if proxy else None
    url = f"{api_endpoint or 'http://web.archive.org'}/cdx/search/cdx?url={domain}/*&output=txt&fl=original&collapse=urlkey"
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            urls = response.text.split("\n")
            if verbose:
                logger.info(f"Found {len(urls)} URLs for {domain}")
            if output_file:
                with open(output_file, "a") as f:
                    for url in urls:
                        f.write(f"{url}\n")
            if limit:
                urls = urls[:limit]
            return urls
        else:
            logger.warning(f"Failed to retrieve Wayback Machine URLs for {domain}. Status code: {response.status_code}")
            return []
    except Exception as e:
        logger.error(f"Failed to retrieve Wayback Machine URLs for {domain}. Error message: {e}")
        return []


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get Wayback Machine URLs for a domain")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--domain", help="The domain to search")
    group.add_argument("-l", "--list", help="A file containing a list of domains")

    parser.add_argument("-o", "--output", help="The output file to write URLs to")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print verbose output")
    parser.add_argument("-n", "--limit", type=int, help="Limit the number of URLs to retrieve")
    parser.add_argument("-e", "--endpoint", default='http://web.archive.org', help="The Wayback Machine API endpoint URL to use")
    parser.add_argument("-u", "--user-agent", default='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', help="The user agent string to use for HTTP requests")
    parser.add_argument("-p", "--proxy", help="The proxy server to use for HTTP requests")
    
    args = parser.parse_args()

    if args.domain:
        urls = get_waybackurls(args.domain, output_file=args.output, limit=args.limit, verbose=args.verbose)
        for url in urls:
            print(url)
    elif args.list:
        with open(args.list) as f:
            for line in f:
                domain = line.strip()
                urls = get_waybackurls(domain, output_file=args.output, limit=args.limit, verbose=args.verbose)
                for url in urls:
                    print(colored(url, "green"))
    else:
        parser.print_help()
        sys.exit(1)

    if args.output and args.verbose:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(colored(f"Wrote URLs to {args.output} at {timestamp}", "green"))
    
    print(colored("Happy Hacking ^_^", "red"))