# Logistics Data Processing with Confluent, Kafka, MongoDB, Python and Docker

## Overview

This project aims to develop a Python-based application for processing logistics data using Confluent, Kafka, MongoDB and Docker. The application consists of a Kafka producer and consumer, leveraging Avro for data serialization/deserialization. Data is ingested into MongoDB, and an API is created for interaction with the stored data.

## Table of Contents

- [Objective](#objective)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [1. Kafka Producer in Python](#1-kafka-producer-in-python)
  - [2. Schema Registry Integration](#2-schema-registry-integration)
  - [3. Logistics Data Information](#3-logistics-data-information)
  - [4. Kafka Consumer in Python](#4-kafka-consumer-in-python)
  - [5. Scaling Kafka Consumers](#5-scaling-kafka-consumers)
  - [6. Data Validation in Kafka Consumer](#6-data-validation-in-kafka-consumer)
  - [7. API Development using MongoDB Atlas](#7-api-development-using-mongodb-atlas)
  - [8. Deliverables](#8-deliverables)
- [Submission Guidelines](#submission-guidelines)

## Objective

Develop a Python-based application that integrates Kafka and MongoDB to process logistics data. The application involves a Kafka producer and consumer, data serialization/deserialization with Avro, and data ingestion into MongoDB. Additionally, an API is developed to interact with the data stored in MongoDB.

## Requirements

- Basic understanding of Python, Kafka, MongoDB, and Docker.
- Access to Confluent Kafka and MongoDB Atlas.
- Familiarity with Docker and containerization.

## Tasks

### 1. Kafka Producer in Python

- Developed a Python script to act as a Kafka producer.
- Utilized Pandas to read logistics data from a CSV file.
- Serialized the data into Avro format and published it to a Confluent Kafka topic.

### 2. Schema Registry Integration

- Established a Schema Registry for managing Avro schemas.
- Ensured that the Kafka producer and consumer fetch the schema from the Schema Registry during serialization and deserialization.

### 3. Logistics Data Information

- Logistics data contains fields like shipment details and tracking information.

### 4. Kafka Consumer in Python

- Wrote a Python script for the Kafka consumer.
- Deserialized the Avro data and ingested it into a MongoDB collection.

### 5. Scaling Kafka Consumers

- Utilized Docker to scale Kafka consumers.
- Provided instructions for deploying multiple instances of the Kafka consumer using Docker.

### 6. Data Validation in Kafka Consumer

- Implemented data validation checks in the consumer script before ingesting data into MongoDB.
- Validations included checking for null values, data type validation, and format checks.
- Documented assumptions made for data validation in the submission document.

### 7. API Development using MongoDB Atlas

- Created an API to interact with the MongoDB collection.
- Implemented endpoints for filtering specific JSON documents and for aggregating data.
- Documented assumptions and use-cases for API creation in the submission document.

### 8. Deliverables

- Python scripts for Kafka producer and consumer.
- Sample logistics data CSV file.
- Dockerfile for scaling Kafka consumers.
- API code for MongoDB interactions.
- Documentation explaining the setup and execution of the application.

## Submission Guidelines

Include the following in your submission:

- Assumptions made during development.
- Use-cases considered for API creation.
- Detailed documentation explaining the setup and execution of the application.

Feel free to customize this template according to your specific project details and additional requirements. Congratulations on completing the project!
