import requests
from bs4 import BeautifulSoup
from collections import Counter

# Step 1: Fetch the webpage
url = 'http://quotes.toscrape.com/tableful/'
response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Failed to load page with status code {response.status_code}")

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract all tags and their counts from the table
tag_counter = Counter()

# Locate the table and loop through all <a> tags inside it
for a_tag in soup.select('table a'):
    tag_name = a_tag.get_text(strip=True)
    
    # Extract the count of the tag from the text between <a> and <br> (inside parentheses)
    sibling = a_tag.next_sibling
    if sibling and "(" in sibling:
        count_str = sibling.strip().strip('()')
        try:
            count = int(count_str)
            tag_counter[tag_name] += count
        except ValueError:
            continue  # Skip if the count is not an integer

# Step 4: Find the most repeated tag
if tag_counter:
    most_common_tag, most_common_count = tag_counter.most_common(1)[0]
    print(f"Le tag le plus répétitif '{most_common_tag}' with {most_common_count} occurrences.")
else:
    print("Pas de tag trouvé.")