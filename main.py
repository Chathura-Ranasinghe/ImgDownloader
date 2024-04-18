import requests
import os

def download_images(image_type, num_images):
    # Create a directory to save images if not exists
    if not os.path.exists(f"Downloads/{image_type}"):
        os.makedirs(f"Downloads/{image_type}")

    # Search URL for images
    search_url = f"https://www.google.com/search?q={image_type}&tbm=isch"

    # Request headers to mimic a browser visit
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Send GET request
    response = requests.get(search_url, headers=headers)
    response.raise_for_status()

    # Extract image URLs from response
    image_urls = response.text.split('src="')[1:]

    # Download images
    successful_downloads = 0
    i = 0
    while successful_downloads < num_images and i < len(image_urls):
        url = image_urls[i].split('"')[0]
        try:
            image_data = requests.get(url, headers=headers).content
            with open(os.path.join(f"Downloads/{image_type}", f"{image_type}_{successful_downloads+1}.jpg"), "wb") as f:
                f.write(image_data)
            print(f"Downloaded image {successful_downloads+1}/{num_images}")
            successful_downloads += 1
        except Exception as e:
            print(f"Failed to download image {successful_downloads+1}: {e}")
        i += 1

if __name__ == "__main__":
    image_type = input("Enter the type of image you want to download: ")
    num_images = int(input("Enter the number of images you want to download: "))
    
    download_images(image_type, num_images)
