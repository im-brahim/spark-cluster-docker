# Spark Standalone Cluster with MinIO & Jupyter in Docker
This repository contains a project to set up a standalone Spark cluster running in Docker containers. It integrates with Jupyter(pyspark-notebook) & with MinIO, a local S3-compatible storage, to process and store data. The setup is ideal for testing and learning Spark in a production-like environment.

## Project Features

- Standalone Spark cluster (Master + Worker nodes -v 3.5.0)

- Jupyter/pyspark-notebook for some analysis.

- MinIO as a local S3-compatible storage backend.

- Support for PySpark job execution (spark-submit).

- Tested with NYC Taxi data (or other sample datasets).

"The environment is configured using Docker Compose."

## Project Structure

Create the necessary folders in your local like this :
.
- docker-compose.yaml               # Docker Compose file for the entire setup
- config/                           # the default config for spark cluster
    - spark-defaults.conf           # Configuration file for Spark
- data/
    - input                         # in case reading data from local
    - output                        # To save data locally
- jobs/                             # Folder for PySpark job scripts
    - test.py                       # Example PySpark job
- nootebook/                        # Jupyter notebooks for interactive analysis
- jars/                             # Folder for additional Spark JAR dependencies
- logs/                             # Directory for Spark logs (if enabled)
- README.md                         # Project documentation
- .gitignore             

## Prerequisites

1. **Docker and Docker Compose**: Ensure both are installed and properly configured on your system.
2. **S3-Compatible JARs**: Required for MinIO integration. Ensure `hadoop-aws-3.3.4.jar` and `aws-java-sdk-bundle-1.12.262.jar` JARs are available.

---

## Setup Instructions

### 1. Clone the Repository
     ```bash
    git clone https://github.com/im-brahim/spark-cluster-docker.git
    cd spark-docker-cluster
     ```

### 2. Prepare the Environment
Add datasets to the data/input/ directory or upload them to the MinIO bucket.
Place additional JAR dependencies (e.g., S3 JARs) in the jars/ folder & mount them into the Spark container (/opt/spark/jars).

### 3. Update Configuration (if needed)
Edit config/spark-defaults.conf to configure Spark properties:
- Example for MinIO:
     ```bash
    spark.hadoop.fs.s3a.access.key  minio
    spark.hadoop.fs.s3a.secret.key  minio123
    spark.hadoop.fs.s3a.endpoint    http://minio:9000

    spark.eventLog.enabled           true
    spark.eventLog.dir              s3a://mybucket/logs
    ```

### 4. Start the Cluster
     ```bash
    docker-compose up -d
     ```
This starts the Spark master, workers, MinIO, and Jupyter notebook containers.

## Running Spark Jobs
## 1. From Local Machine
Submit a PySpark job using the spark-submit command (inside the container):
     ```bash
    docker exec -it master bash
     ```
    
     ```bash
    spark-submit --master spark://master:7077 \
             --jars /opt/spark/jars/hadoop-aws-3.3.4.jar,/opt/spark/jars/jars/aws-java-sdk-1.12.262.jar \
             /opt/spark/jobs/test.py
     ```
- /opt/spark/jobs/test.py : the path where py scripts mounted in container (configured in docker-compose file)
- /opt/spark/jars/*       : where the jars is mounted
#### Important Note:
- If JARs are not mounted, they must be added directly to /opt/bitnami/spark/jars in the container, so you will not need to specifies the path for s3 jars.

## 2. Add worker 
To scale worker just put the number of workers you need 
     ```bash
    docker-compose up -d --scale worker=3
     ```
- worker: the name of the service in docker-compose.
- 3 the number of workers you want to run

## 3. Using Jupyter Notebook
### Access the notebook:
Open your browser and navigate to http://localhost:8888.
Run Spark code interactively using PySpark after adding necessary config to access minIO and locate Jars..
     ```bash
    spark = SparkSession.builder \
    .appName("Jupyter with Spark") \
    .master("spark://master:7077") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "minio") \
    .config("spark.hadoop.fs.s3a.secret.key", "minio123") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.jars", "/opt/spark/jars/hadoop-aws-3.3.4.jar,/opt/spark/jars/aws-java-sdk-bundle-1.12.262.jar") \
    .getOrCreate()
     ```

# Let's Practis :)