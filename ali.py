from serpapi.google_search_results import GoogleSearchResults

params = {
  "q": "Python programming language",
  "location": "Austin, Texas",
  "hl": "en",
  "gl": "us",
  "api_key": "YOUR_API_KEY"
}

client = GoogleSearchResults(params)
data = client.get_json()

# Use the data to access the search results
