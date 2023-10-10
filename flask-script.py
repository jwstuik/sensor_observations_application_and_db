from flask import Flask, request, jsonify

app = Flask(__name__)

# here we should use the database for storage of experiments, but for testing I used this
experiments = {}

############### TOPIC EVENTS ##################

# Endpoint to handle Experiment Configuration Event
@app.route('/experiment_configured', methods=['POST'])
def configure_experiment():
    data = request.get_json()
    experiment = Experiment(
        researcher=data['researcher'],
        upper_threshold=data['temperature_range']['upper_threshold'],
        lower_threshold=data['temperature_range']['lower_threshold']
    )

    for sensor_id in data['sensors']:
        sensor = Sensor(sensor_id=sensor_id, experiment=experiment)
        db.session.add(sensor)

    db.session.add(experiment)
    db.session.commit()
    
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
    sensor_id = data.get('sensor')
    temperature = data.get('temperature')

    experiment = Experiment.query.filter_by(id=experiment_id).first()
    if experiment:
        measurement = Measurement(
            experiment=experiment,
            timestamp=data['timestamp'],
            temperature=temperature
        )
        db.session.add(measurement)

        # Check if temperature is out of range and notify researcher if needed
        if temperature > experiment.upper_threshold or temperature < experiment.lower_threshold:
            notify_researcher(experiment_id, data)

        db.session.commit()

    return jsonify({'message': 'Temperature measurement saved'}), 200


# Endpoint to handle Experiment Terminated Event
@app.route('/experiment_terminated', methods=['POST'])
def terminate_experiment():
    data = request.get_json()
    experiment_id = data.get('experiment')

    return jsonify({'message': 'Experiment terminated'}), 200


# Endpoint to get measurements during which an experiment was out of range
@app.route('/out_of_range_measurements/<experiment_id>', methods=['GET'])
def out_of_range_measurements(experiment_id):

    return jsonify([]), 200


# Helper function to notify the researcher 
def notify_researcher(experiment_id, measurement_data):
    # Still have to define
    pass


if __name__ == '__main__':
    app.run(debug=True)

