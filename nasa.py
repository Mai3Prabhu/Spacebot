# nasa.py - Handles NASA Images API integration

import requests
import os

NASA_API_BASE_URL = "https://images-api.nasa.gov"

def search_nasa_images(query: str, media_type: str = "image") -> list[dict]:
    """Searches NASA Images API for a given query and media type.

    Args:
        query: The search term.
        media_type: The type of media to search for (e.g., 'image', 'audio').

    Returns:
        A list of dictionaries, each containing 'title', 'description', and 'image_url'.
        Returns an empty list if no results are found or an error occurs.
    """
    search_url = f"{NASA_API_BASE_URL}/search"
    params = {
        "q": query,
        "media_type": media_type
    }

    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        data = response.json()

        results = []
        if data.get("collection") and data["collection"].get("items"):
            for item in data["collection"]["items"]:
                if item.get("data") and item.get("links"):
                    item_data = item["data"][0] # Assuming the first data entry is relevant
                    image_url = None
                    for link in item["links"]:
                        if link.get("render") == "image":
                            image_url = link.get("href")
                            break
                    
                    if image_url:
                        results.append({
                            "title": item_data.get("title", "N/A"),
                            "description": item_data.get("description_508") or item_data.get("description", "N/A"),
                            "image_url": image_url
                        })
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from NASA API: {e}")
        return []
    except KeyError as e:
        print(f"Error parsing NASA API response: {e}")
        return []

if __name__ == '__main__':
    # Example Usage:
    # Note: NASA API does not require an API key for basic search, 
    # but rate limits might apply for heavy usage.
    images = search_nasa_images("apollo 11")
    if images:
        print(f"Found {len(images)} images for 'apollo 11':")
        for img in images[:3]: # Print details of the first 3 images
            print(f"  Title: {img['title']}")
            print(f"  Description: {img['description'][:100]}...") # Truncate description
            print(f"  URL: {img['image_url']}")
            print("---")
    else:
        print("No images found for 'apollo 11'.")

    images_hubble = search_nasa_images("hubble space telescope")
    if images_hubble:
        print(f"\nFound {len(images_hubble)} images for 'hubble space telescope':")
        for img in images_hubble[:1]: # Print details of the first image
            print(f"  Title: {img['title']}")
            print(f"  Description: {img['description'][:100]}...")
            print(f"  URL: {img['image_url']}")
            print("---")
    else:
        print("No images found for 'hubble space telescope'.")