from bing_search_api import BingSearchAPI
my_key = "MEL5FOrb1H5G1E78YY8N5mkfcvUK2hNBYsZl1aAEEbE"
 
def main():
    print(search("Hello", 3))

def search(query_string, num_results):
    bing = BingSearchAPI(my_key)
    params = {'ImageFilters':'"Face:Face"',
              '$format': 'json',
              '$top': num_results,
              '$skip': 0}
    results = bing.search('web',query_string,params).json() # requests 1.0+ 

    return [result['Url'] for result in results['d']['results'][0]['Web']]
 
if __name__ == "__main__":
    main()