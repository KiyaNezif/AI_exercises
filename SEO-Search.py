# Exercise 1: https://www.wiseowl.co.uk/ai/exercises/ai-artificial-intelligence/coding-python/5287/


# AI SEO search tool
#This project is a simple Python tool that retrieves the top search results from Google based on a given search term. It demonstrates how AI and automation can be used to support SEO research and keyword analysis.
# The tool uses the google search to top search results for a given search term and prints the URLs of those results.
from itertools import count
from unittest import result

from duckduckgo_search import DDGS
from ddgs import DDGS

#set a variable for the search term and the number of results to retrieve
seo= "AI training courses in the UK "
num_urls = 20

#testing the variables by printing them to the console
print("Search term:", seo)
print("Number of URLs:", num_urls)

 #using DDGS to perform the search and retrieve the top results
with DDGS() as ddgs:
    res = ddgs.text(seo, max_results=num_urls)
    for result in res:
        print(result['href'])
