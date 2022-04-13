import requests


def example():
    response = requests.get('http://example.com')
    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    example()
