#%%
import requests

# First define the API URL, the origin of the data
base_url = "data.riksdagen.se"
endpoint_url = "dokumentlista"
url = "http://" + base_url + "/" + endpoint_url  + "/"

# %%

# Define search parameters
params = {
    'sok': 'skatt',
    'doktyp': 'mot',
    'utformat': 'json'
}

# Fetch the data
response = requests.get(url, params=params)

# Retrieve the data
 # The method used depends on the data formats
data = response.json()

# %%
# Get the actual documents
documents = data['dokumentlista']['dokument']

# Inspect a document
print(documents[0])

#%%
import pandas as pd

def extract_authors(document):

    return document['dokintressent']['intressent']


authors = extract_authors(documents[0])

df = pd.DataFrame(authors)



# %%
def get_document_html(document):
    """A function used to fetch the 
    html of a document from the Swedish Parliamentary
    Database.

    Args:
        document (dict): A dictionary describing a document from the data.riksdagen.se/dokumentlista.
        Requires a key 'dokument_url_text' with a URL to the document text.

    Returns:
        str: An HTML document as a string
    """

    # Compose the URL
    url = "https:" + document['dokument_url_html']

    # Fetch the data
    response = requests.get(url)

    # Retrieve the data (format is text)
    text = response.text

    return text

# %%
from bs4 import BeautifulSoup as bs

def parse_html_document(html):
    """A function used to parse and extract the text from
    an HTML document.

    Args:
        html (str): An HTML document as a string

    Returns:
        str: The text content of the input HTML document
    """

    root = bs(html, "html")

    text = root.getText()

    return text


# %%
for document in documents:

    html = get_document_html(document)
    text = parse_html_document(html)

    print(text)

    break
# %%
