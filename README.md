# Temperature Observability Microservice

The Temperature Observability Microservice is a Python-based REST API designed to monitor and manage temperature data for experiments. It is part of a larger system that helps researchers ensure their experiments maintain specific temperature ranges and receive notifications when temperature values deviate from the configured thresholds.

## Overview

The Temperature Observability Microservice offers the following core functionality:

- **Experiment Configuration**: Researchers can configure experiments, specifying sensors, temperature ranges, and notification email addresses.

- **Temperature Monitoring**: The microservice continuously monitors and stores temperature data throughout the experiment.

- **Notification System**: Researchers are notified when temperature values fall outside the specified range.

- **Integration with Kafka**: It integrates with Kafka for experiment data ingestion.

- **Interaction with a Notifications REST API**: It interacts with a Notifications REST API for event notifications.

## Usage

To use the Temperature Observability Microservice, interact with the provided API endpoints using HTTP requests. These endpoints allow you to configure experiments, start and monitor temperature data during experiments, and retrieve historic temperature measurements.



## API Endpoints

The Temperature Observability Microservice offers the following API endpoints:

- `POST /configure_experiment`: Configure an experiment with sensors, temperature range, and researcher's email.

- `POST /start_stabilization`: Signal the start of the temperature stabilization phase.

- `POST /start_experiment`: Mark the start of the experiment.

- `POST /measure_temperature`: Record temperature measurements and notify researchers when out of range.

- `POST /terminate_experiment`: Mark the end of an experiment.

- `GET /out_of_range_measurements/<experiment_id>`: Retrieve measurements when an experiment was out of the temperature range.


