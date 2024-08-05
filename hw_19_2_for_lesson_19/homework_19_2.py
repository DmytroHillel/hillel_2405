import requests

# URL сервера для завантаження зображення
upload_url = "http://127.0.0.1:8080/upload"
image = 'man-1854195_150.jpg'
files = {'image': open(image, 'rb')}
response = requests.post(upload_url, files=files)

if response.status_code == 201:
    print("Зображення успішно завантажено!")
else:
    print("Помилка при завантаженні зображення.")

# Отримання URL завантаженого зображення
image = 'man-1854195_150.jpg'
get_url = f"http://127.0.0.1:8080/image/{image}"
headers = {'Content-Type': 'text'}
response_2 = requests.get(get_url, headers=headers)
print(response_2.text)
if response_2.status_code == 200:
    image_url = response_2.json().get('image_url')
    print(f"Посилання на зображення: {image_url}")
else:
    print("Помилка при отриманні посилання на зображення.")

# Видалення завантаженого зображення
delete_url = f"http://127.0.0.1:8080/delete/{image}"

response = requests.delete(delete_url)
if response.status_code == 200:
    print(f"Зображення {image} успішно видалено.")
else:
    print("Помилка при видаленні зображення.")
