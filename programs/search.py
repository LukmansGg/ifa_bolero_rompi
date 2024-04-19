import time
import requests
from googlesearch import search
from tinydb import TinyDB
import uuid

# Initialize the database
db = TinyDB('search_results.json')

def search(query):
    try:
        search_id = str(uuid.uuid4())  # Generate a unique ID
        for i, result in enumerate(search(query, num_results=20, lang='id', advanced=True), 1):
            string_result = str(result)

            title_raw = string_result.split("title=")[1]
            title_result = title_raw.split(", description")[0]
            description_raw = string_result.split("description=")[1]
            description_result = description_raw.split(")")[0]

            link_raw = string_result.split("url=")[1]
            link_result = link_raw.split(", title")[0]

            # Save search data to the database along with the unique ID
            db.insert({'search_id': search_id, 'title': title_result, 'description': description_result, 'link': link_result})

            # Limit to sending only the first 5 search results
            if i >= 10:
                break

        return search_id
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 429:
            # Add a delay before retrying
            time.sleep(5)  # Example delay of 5 seconds, adjust as needed
            # Retry the request after the delay
            return "Maaf, saat ini sedang terdapat gangguan pada sistem jaringan Google kami 🙏"
    except Exception as e:
        # Handle any other unknown errors gracefully
        return "An unknown error occurred: {e}"

