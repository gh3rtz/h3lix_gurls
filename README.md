<h1>H3lix G-Urls</h1>
This Python script can be used to retrieve URLs from the Wayback Machine for a given domain. 
<strong>Installation:</strong> To install the required packages, run the following command:

<p><code>pip install -r requirements.txt</code></p>
<strong>Usage:</strong> To retrieve Wayback Machine URLs for a single domain, use the following command:

<p><code>python gurls.py -d domain.com</code></p>
To retrieve Wayback Machine URLs for multiple domains from a file, use the following command:

<p><code>python gurls.py -l domains.txt</code></p>
<strong>Additional options include:</strong>

<ul>
  <li><code>-o, --output</code>: The output file to write URLs to.</li>
  <li><code>-v, --verbose</code>: Print verbose output.</li>
  <li><code>-n, --limit</code>: Limit the number of URLs to retrieve.</li>
  <li><code>-e, --endpoint</code>: The Wayback Machine API endpoint URL to use. Default is http://web.archive.org.</li>
  <li><code>-u, --user-agent</code>: The user agent string to use for HTTP requests. Default is Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3.</li>
  <li><code>-p, --proxy</code>: The proxy server to use for HTTP requests.</li>
</ul>
<strong>Example:</strong> To retrieve the first 100 Wayback Machine URLs for example.com and write them to a file called urls.txt with verbose output, use the following command:

<p><code>python waybackurls.py -d example.com -o urls.txt -v -n 100</code></p>
