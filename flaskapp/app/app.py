from flask import Flask, request, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)


########## Opt for this one ##########

#client = MongoClient('mongodb://mongodb:27017/')
client = MongoClient('localhost', 27017, username='root', password='experiment')
db = client['temperature-observability']  
collection = db['experiments']


# Function to save experiment data
def save_experiment(experiment_data):
    collection.insert_one(experiment_data)

# Function to save temperature measurements
def save_temperature_measurement(measurement_data):
    collection.insert_one(measurement_data)

# Function to retrieve out-of-range measurements for a specific experiment
def get_out_of_range_measurements(experiment_id):
    out_of_range_measurements = collection.find({
        "experiment": experiment_id,
    })
    return list(out_of_range_measurements)



@app.route('/')
def contact_db():
    return "This is the main page of the experiment"

############### TOPIC EVENTS ##################

# Endpoint to handle Experiment Configuration Event
@app.route('/experiment_configured', methods=['POST'])
def configure_experiment():
    data = request.get_json()
    save_experiment(data)
    return jsonify({'message': 'Experiment configuration saved'}), 201


# Endpoint to handle Stabilization Started Event
@app.route('/stabilization_started', methods=['POST'])
def start_stabilization():
    data = request.get_json()
    experiment_id = data.get('experiment')

    return jsonify({'message': 'Stabilization started'}), 200


# Endpoint to handle Experiment Started Event
@app.route('/experiment_started', methods=['POST'])
def start_experiment():
    data = request.get_json()
    experiment_id = data.get('experiment')

    return jsonify({'message': 'Experiment started'}), 200


# Endpoint to handle Sensor Temperature Measured Event
@app.route('/measure_temperature', methods=['POST'])
def measure_temperature():
    data = request.get_json()
    experiment_id = data.get('experiment')
    temperature = data.get('temperature')
    save_temperature_measurement(data)
    # Check if temperature is out of range and notify researcher if needed
    if experiment_id in collection:
        experiment = collection[experiment_id]
        upper_threshold = experiment['temperature_range']['upper_threshold']
        lower_threshold = experiment['temperature_range']['lower_threshold']
        if temperature > upper_threshold or temperature < lower_threshold:
            notify_researcher(experiment_id, data)

    return jsonify({'message': 'Temperature measurement saved'}), 200


# Endpoint to handle Experiment Terminated Event
@app.route('/experiment_terminated', methods=['POST'])
def terminate_experiment():
    data = request.get_json()
    experiment_id = data.get('experiment')

    return jsonify({'message': 'Experiment terminated'}), 200


@app.route('/out_of_range_measurements/<experiment_id>', methods=['GET'])
def out_of_range_measurements(experiment_id):
    out_of_range_data = get_out_of_range_measurements(experiment_id)
    return jsonify(out_of_range_data), 200


# Helper function to notify the researcher 
def notify_researcher(experiment_id, measurement_data):
    pass


if __name__ == '__main__':
    app.run(debug=True)

