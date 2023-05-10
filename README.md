H3lix G-Urls

This Python script retrieves URLs from the Wayback Machine for a given domain.

Installation
To install the required packages, run the following command:
pip install -r requirements.txt

Usage: python waybackurls.py -d domain.com

To retrieve Wayback Machine URLs for multiple domains from a file, run the following command: python waybackurls.py -l domains.txt

Additional options include:
-o, --output: The output file to write URLs to.
-v, --verbose: Print verbose output.
-n, --limit: Limit the number of URLs to retrieve.
-e, --endpoint: The Wayback Machine API endpoint URL to use. Default is http://web.archive.org.
-u, --user-agent: The user agent string to use for HTTP requests. Default is Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3.
-p, --proxy: The proxy server to use for HTTP requests.

Example: python waybackurls.py -d example.com -o urls.txt -v -n 100

This will retrieve the first 100 Wayback Machine URLs for example.com and write them to a file called urls.txt. Verbose output will be printed to the console.
