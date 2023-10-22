import requests

base_url = "http://localhost:5000"  

configure_experiment_url = f"{base_url}/experiment_configured"

experiment_data = {
    "experiment": "9ee55bd4-a531-409c-9a64-0398353cadc5",
    "researcher": "d.landau@uu.nl",
    "sensors": [
        "66cc5dc0-d75a-40ee-88d5-0308017191af",
        "ac5e0ea2-a04d-4eb3-a6e3-206d47ffe9e1"
    ],
    "temperature_range": {
        "upper_threshold": 26.0,
        "lower_threshold": 25.0,
    }
}

response = requests.post(configure_experiment_url, json=experiment_data)


if response.status_code == 201:
    print("Experiment configured successfully.")
else:
    print("Failed to configure the experiment.")
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.text}")
