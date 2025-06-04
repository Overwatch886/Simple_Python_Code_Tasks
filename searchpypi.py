headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}
# Importing Modules
import sys, requests, bs4
search_key = None
if len(sys.argv) > 1:
    search_key = ' '.join(sys.argv[1:])
web_page = f"https://en.m.wikipedia.org/wiki/{search_key}"
# Retriving Content From Webpage
web_page = requests.get(web_page)
#with open("/storage/EFD6-7824/Documents/Coding_Files/hello.html", "wb") as #PlayFile:
        # Saving webpage content to hello.html
   #     for chunk in web_page.iter_content(1024):
#            PlayFile.write(chunk)

# Retrieve search result links.
soup = bs4.BeautifulSoup(web_page.content, 'html.parser')
# Searching for Links to The Search results
link_elems = soup.find_all('a', title = lambda x: x and 'None' in x)
# Printing out all search results
for link in link_elems :
    print(link.attrs['href'])
    