import re
import requests
import json
import hashlib



headers = {
    'Host': 'task.zostansecurity.ninja',
}

response = requests.get('https://task.zostansecurity.ninja/', headers=headers)

# Sample response text
response_text = response.text

# Regular expression pattern to match the desired part
pattern = r'/\?step=\d+&challenge=[a-f0-9]+&timestamp=\d+'

# Search for the pattern in the response text
match = re.search(pattern, response_text)

if match:
    desired_part = match.group(0)
    print("Extracted URL part:", desired_part)

    url = f"https://task.zostansecurity.ninja{desired_part}"
    print("Generated URL:", url)

    # Send a GET request to the generated URL
    response_new = requests.get(url, headers=headers)

    print("\nResponse from the new URL:")
    print(response_new.text)
    
    

else:
    print("Pattern not found in the response text") 
    
pattern_challenge = r'X-challenge: ([a-f0-9]+)'
pattern_timestamp = r'X-timestamp: (\d+)'

# Search for X-challenge and X-timestamp in the response text
match_challenge = re.search(pattern_challenge, response_new.text)
match_timestamp = re.search(pattern_timestamp, response_new.text)

if match_challenge and match_timestamp:
    x_challenge = match_challenge.group(1)
    x_timestamp = match_timestamp.group(1)

    print("\nExtracted X-challenge:", x_challenge)
    print("Extracted X-timestamp:", x_timestamp)

    # Proceed to the next step if needed
    # You can generate the URL and send another GET request similar to the first part if required

else:
    print("X-challenge or X-timestamp not found in the response text")
  

# URL for the second step
url = "https://task.zostansecurity.ninja/?step=2"


# Headers to be added to the request
headers = {
    'Host': 'task.zostansecurity.ninja',
    'X-challenge': f'{x_challenge}',
    'X-timestamp': f'{x_timestamp}',
}

# Sending the GET request
response = requests.get(url, headers=headers)

# Print the response content
print(response.text)




pattern_challenge = r'challenge: ([a-f0-9]+)'
pattern_timestamp = r'timestamp: (\d+)'

# Search for X-challenge and X-timestamp in the response text
match_challenge = re.search(pattern_challenge, response.text)
#match_timestamp = re.search(pattern_timestamp, response.text)

if match_challenge and match_timestamp:
    challenge = match_challenge.group(1)
    timestamp = match_timestamp.group(1)

    #print("\nExtracted challenge:", challenge)
    #print("Extracted timestamp:", timestamp)

    # Proceed to the next step if needed
    # You can generate the URL and send another GET request similar to the first part if required

else:
    print("challenge or timestamp not found in the response text")

json_data_match = re.search(r'\{([^{}]*)\}', response.text)
if json_data_match:
    json_data_text = json_data_match.group(0)
    # Parse the extracted JSON data
    extracted_data = json.loads(json_data_text)
   # print(extracted_data)
else:
    print("No JSON data found")







# Define your extracted_data dictionary


def flatten_dict(d):
    return '&'.join([f"{key}={value}" for key, value in sorted(d.items())])

def generate_sha256_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()

# Flatten the dictionary
flattened_str = flatten_dict(extracted_data)
#print("Flattened string:", flattened_str)

# Calculate the SHA256 hash
sha256_hash = generate_sha256_hash(flattened_str)
#print("SHA256 hash:", sha256_hash)


import requests
import time
import hashlib

url = 'https://task.zostansecurity.ninja/?step=3'
headers = {
    'Host': 'task.zostansecurity.ninja',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'challenge': challenge,
    'timestamp': timestamp,  # Update timestamp with current Unix timestamp
    'hash': sha256_hash
}

response = requests.post(url, headers=headers, data=data)
print(response.text)