# CDC Solution using Debezium, Kafka, and PostgreSQL
This project demonstrates a Change Data Capture (CDC) solution using Debezium to capture changes in a source PostgreSQL database and propagate them to a target PostgreSQL database via Kafka. The setup includes Kafka, Zookeeper, Debezium, and Schema Registry, all running in Docker containers.

## Prerequisites
To run this solution, you need:
- Docker
- Docker Compose

## Overview
The architecture involves two PostgreSQL databases :

- Source DB: exampledb, which captures all data changes.
- Target DB: targetdb, which receives propagated changes.
We use Debezium to monitor changes in the source PostgreSQL database and Kafka to transport these changes. Schema Registry helps in managing the Avro schemas used for data serialization.

Docker Services uded in the project : 
1. Postgres (Source DB)
Runs a PostgreSQL instance with CDC enabled using Debezium.
Accessible on port 5432.
Database: exampledb
2. Postgres (Target DB)
Runs a separate PostgreSQL instance where changes from the source DB will be applied.
Accessible on port 5433.
Database: targetdb
3. Zookeeper
A service used by Kafka for distributed coordination.
Accessible on port 2181.
4. Kafka
Serves as the backbone for transmitting changes captured by Debezium from the source database to the target database.
Accessible on port 9092.
5. Debezium Connect
Monitors the source PostgreSQL database and publishes the changes to Kafka topics.
Accessible on port 8083.
Requires Kafka and Zookeeper to function.
6. Schema Registry
Manages Avro schemas to ensure proper data serialization/deserialization between services.
Accessible on port 8081.
## Instructions
Start the Docker containers:
```bash
docker-compose up
```
This will spin up all the necessary services (Postgres, Kafka, Zookeeper, Debezium, and Schema Registry).

## Notes
The custom connector image for Debezium is loaded via the PLUGIN_PATH. If you need to add more connectors or customize the path, ensure that the volume mount is correctly set.
The source PostgreSQL is running on port 5432, and the target PostgreSQL on port 5433. You can connect to these databases using any PostgreSQL client for testing and monitoring.
