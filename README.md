# random-user-streaming

## Project Overview

This project demonstrates a data streaming and processing pipeline using various technologies including Python, Kafka, Airflow, Spark Streaming, Cassandra, and Docker. The pipeline fetches data from a public API, streams it to Kafka, processes it using Spark Streaming, and stores the processed data in a Cassandra database. All components are containerized using Docker.

## Components

1. **Data Fetching (Python)**: Python code fetches data from the [Random User API](https://randomuser.me/api/) and converts it into a dictionary format.

2. **Kafka Producer**: The dictionary data is streamed to Kafka using a Kafka Producer in Python.

3. **Airflow**: Airflow is used to trigger and orchestrate the Python script that fetches and streams the data.

4. **Spark Streaming**: Spark Streaming processes the incoming data from Kafka and prepares it for storage.

5. **Cassandra**: Processed data is stored in a Cassandra table after creating the necessary keyspace and table.

6. **Docker**: All services (Python script, Kafka, Airflow, Spark, Cassandra) are containerized using Docker to ensure a consistent and reproducible environment.

## Prerequisites

- Docker and Docker Compose installed
- Basic knowledge of Python, Kafka, Spark, Cassandra, and Airflow

## Getting Started

### Clone the Repository

```sh
git clone https://github.com/NikhilLIv/kafka-spark-streaming.git
cd kafka-spark-streaming
```

### Build and Run Docker Containers

Ensure Docker and Docker Compose are installed on your machine. Then, run the following command to build and start the containers:

```sh
docker compose up -d
```

### Accessing Services

- **Airflow**: Access the Airflow web interface at `http://localhost:8080`
- **Kafka**: Kafka broker will be available at `localhost:9092`
- **Spark**: Access the Spark Master at `http://localhost:9090`
- **Cassandra**: Cassandra will be available at `localhost:9042`

## Usage

1. **Trigger Data Fetching**: Use the Airflow web interface to trigger the DAG that runs the Python script to fetch and stream data to Kafka.
2. **Monitor Spark Streaming**: Spark Streaming job will automatically pick up the data from Kafka, process it, and store it in Cassandra.
3. **Verify Data in Cassandra**: Connect to Cassandra and query the table to verify that the data has been correctly stored.

## Configuration

- **Airflow DAG**: Located in `dags/` directory.
- **Python Script**: Located in root directory.
- **Docker Compose**: Configuration in `docker-compose.yml`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Random User API](https://randomuser.me/api/)
- [Apache Kafka](https://kafka.apache.org/)
- [Apache Airflow](https://airflow.apache.org/)
- [Apache Spark](https://spark.apache.org/)
- [Apache Cassandra](https://cassandra.apache.org/)
- [Docker](https://www.docker.com/)

```

Feel free to customize any sections as needed!
