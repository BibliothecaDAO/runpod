import time
import requests
import json
import os
import dotenv # pip install python-dotenv

dotenv.load_dotenv()

# Set the API endpoint URL
endpoint = os.getenv("RUNPOD_ENDPOINT")

# Set the headers for the request
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {os.getenv('RUNPOD_API_TOKEN')}"
 }

# Define your inputs
input_data = {
  "input": {
    "prompt": "a woodblock illustration of a male human mage with blue glowing eyes a beard and white hair, wearing a white priest's robe with golden ornaments, closeup, frontal",
    "num_outputs": 5,
    "num_inference_steps": 35,
    "scheduler": "EULER-A",
  }
 }

# Make the request
response = requests.post(f"{endpoint}/run", json=input_data, headers=headers)

# Print the response 
response = json.loads(response.text)
id = response["id"]
print(id)

while True:
    response = requests.get(
        f"{endpoint}/status/{id}",
        headers=headers,
    )
    response = json.loads(response.text)
    if response["status"] == "COMPLETED":
        break
    print(response)
    time.sleep(1)

for idx, image in enumerate(response["output"]):
    imgurl = image["image"].split(".png")[0]
    # download image
    response = requests.get(f"{imgurl}.png")
    with open(f"{idx}.png", "wb") as f:
        f.write(response.content)
