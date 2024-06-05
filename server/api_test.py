import requests

url = 'http://127.0.0.1:5000/imgUploadTest'
file_path = r'E:\myrepository\GarbageSorting\imgs\111.png'

with open(file_path, 'rb') as f:
    files = {'imgs': f}
    response = requests.post(url, files=files)

print(response.text)