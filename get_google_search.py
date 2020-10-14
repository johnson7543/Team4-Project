import requests

# get the API KEY here: https://developers.google.com/custom-search/v1/overview
API_KEY = "AIzaSyD0Jz7sfKdq_vJI21azx4Rr67_6Ew3xio4"
# get your Search Engine ID on your CSE control panel
SEARCH_ENGINE_ID = "011581237149803790891:kvvffq2br44"
# the search query you want
query = "中原美食"
# using the first page
page = 1
# constructing the URL
# doc: https://developers.google.com/custom-search/v1/using_rest
# calculating start, (page=2) => (start=11), (page=3) => (start=21)
start = (page - 1) * 10 + 1
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
#&start={start}
# make the API request
data = requests.get(url).json()
print(data)
# get the result items
search_items = data.get("items")
# iterate over 10 results found
for i, search_item in enumerate(search_items, start=1):
    # get the page title
    title = search_item.get("title")
    # page snippet
    snippet = search_item.get("snippet")
    # alternatively, you can get the HTML snippet (bolded keywords)
    html_snippet = search_item.get("htmlSnippet")
    # extract the page url
    link = search_item.get("link")
    # print the results
    print("="*10, f"Result #{i+start-1}", "="*10)
    print("Title:", title)
    print("Description:", snippet)
    print("URL:", link, "\n")
    
    
    


