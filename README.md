# etl-s3-spark-airflow
etl-s3-spark-airflow
# 🚀 ETL Pipeline: S3 + PySpark + Airflow

## 📌 Project Overview
This project demonstrates an end-to-end ETL pipeline built using modern data engineering tools.

## ⚙️ Tech Stack
- Python
- PySpark
- Apache Airflow
- AWS S3
- EC2

## 🔄 Pipeline Workflow
1. Extract data from AWS S3 (CSV file -1000 rows)
2. Transform data using PySpark
3. Load processed data back into S3
4. Orchestrate using Airflow DAG

## 📂 Project Structure
- dags/ → Airflow DAG
- scripts/ → Spark ETL logic
- sample_data/ → Input data


## ✅ Key Features
- Automated ETL pipeline
- Scalable data processing using Spark
- Cloud storage integration (S3)
- Workflow scheduling using Airflow

## 🚀 How to Run
1. Start Airflow
2. Upload data to S3
3. Trigger DAG
4. Check output in S3

## 💡 Learning Outcome
Built a real-world ETL pipeline simulating production-level data workflows.

