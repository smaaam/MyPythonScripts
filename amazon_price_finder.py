import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text)
    soup.select('') #find the css path for here
    return elems[0].text.strip() #To get rid of the whitespace







getAmazonPrice() #Pass a amazon URL
print('The price is ' + price)
