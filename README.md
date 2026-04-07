# 🚀 ETL Pipeline: S3 + PySpark + Airflow

## 📌 Project Impact
- Built an automated ETL pipeline to process cloud-based data efficiently  
- Reduced manual data processing by introducing workflow automation using Airflow  
- Simulates a real-world data engineering pipeline used in production systems  
- Demonstrates handling of batch data processing using distributed computing (PySpark)

---

## ⚙️ Tech Stack
- Python  
- PySpark  
- Apache Airflow  
- AWS S3  
- AWS EC2  

---

## 🔄 Pipeline Workflow
1. Extract data from AWS S3 (CSV file - 1000 rows)  
2. Transform data using PySpark (filtering, aggregation, cleaning)  
3. Load processed data back into S3  
4. Schedule and automate workflow using Airflow DAG  

---

## 🏗️ Architecture
The pipeline follows a batch processing architecture:

- Data is stored in AWS S3 (input layer)  
- PySpark processes and transforms the data  
- Transformed data is written back to S3  
- Apache Airflow orchestrates and schedules the workflow  

Flow:
CSV → S3 → Airflow DAG → Spark → S3 (output)
---

## 📂 Project Structure
- `dags/` → Airflow DAG definition  
- `scripts/` → Spark ETL logic  
- `sample_data/` → Input dataset  
- `screenshots/` → Output proof  

---

## 📸 Output Screenshots
<img width="1920" height="1080" alt="airflow_success" src="https://github.com/user-attachments/assets/3376d907-f6d6-4ee9-a404-b2d8754a81b2" />
<img width="1920" height="1080" alt="airflow_success2" src="https://github.com/user-attachments/assets/2a3e404d-3770-46c8-ab6c-492f846f50e7" />
<img width="1920" height="1080" alt="AWS-S3-input-1000-rowsfile" src="https://github.com/user-attachments/assets/ce1c52a5-0fd3-4910-a99a-ee0b108d3c03" />
<img width="1920" height="1080" alt="AWS-S3-input-output" src="https://github.com/user-attachments/assets/6ed206b2-7524-4c0c-aa4a-cf985b4a134a" />
<img width="1920" height="1080" alt="AWS-S3-output-high-low" src="https://github.com/user-attachments/assets/974b2f38-0102-4122-86b6-244a6c9ea0d2" />
<img width="1920" height="1080" alt="AWS-S3-op-high_value" src="https://github.com/user-attachments/assets/7a426062-8208-4a41-baeb-d68d3c8a3083" />
<img width="1920" height="1080" alt="AWS-S3-op-low_value" src="https://github.com/user-attachments/assets/865584e3-d7f9-46e6-b40f-52738374606f" />



---

## ✅ Key Features
- Automated ETL pipeline using Airflow  
- Scalable data processing with PySpark  
- Cloud-based storage integration (AWS S3)  
- Modular and production-like project structure  

---

## 🚀 How to Run
1. Start Airflow services  
2. Upload input CSV file to S3  
3. Trigger the DAG from Airflow UI  
4. Verify processed output in S3  

---

## 💡 Learning Outcome
- Built a real-world ETL pipeline using cloud + big data tools  
- Gained hands-on experience with Airflow orchestration  
- Learned distributed data processing using PySpark  
