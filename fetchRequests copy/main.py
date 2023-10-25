import requests


def fetch_requests():
    urls = []
    while True:
        url = input("Enter an URL (or write quit to exit):")

        if url.lower() == 'quit':
            break

        urls.append(url)

    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            print(f"Successfully retrieved: {url}")
            # print(response.text)  # Can uncomment to get the content of the url.
        else:
            print(f"Couldn't retrieve anything from {url}. Status Code: {response.status_code}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fetch_requests()
