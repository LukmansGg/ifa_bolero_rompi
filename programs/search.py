import time
import requests
from googlesearch import search
from tinydb import TinyDB
import uuid

# Initialize the database
db = TinyDB('search_results.json')

def searching(query):
    try:
        search_id = str(uuid.uuid4())  # Generate a unique ID
        results = search(query, lang="id", num_results=20, advanced=True)
        my_results_list = []
        for i, result in enumerate(results, 1):
            string_result = str(result)

            title_raw = string_result.split("title=")[1]
            title_result = title_raw.split(", description")[0]
            description_raw = string_result.split("description=")[1]
            description_result = description_raw.split(")")[0]

            link_raw = string_result.split("url=")[1]
            link_result = link_raw.split(", title")[0]

            my_results_list.append({'title': title_result, 'description': description_result, 'link': link_result})

            # Limit to sending only the first 10 search results
            if i >= 10:
                break

        # Simpan data ke dalam database dengan struktur yang diinginkan
        db.insert({'search_id': search_id, 'links': my_results_list})
        return search_id
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 429:
            # Add a delay before retrying
            time.sleep(5)  # Example delay of 5 seconds, adjust as needed
            # Retry the request after the delay
            return "Maaf, saat ini sedang terdapat gangguan pada sistem jaringan Google kami 🙏"
    except Exception as e:
        # Handle any other unknown errors gracefully
        return f"An unknown error occurred: {e}"

