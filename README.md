# Real-Time Air Quality Monitoring Pipeline (Accra)

### Overview
A real-time data streaming pipeline to monitor air quality across the city of Accra, using simulated IoT sensor data. The system ingests, transforms, stores, and visualizes environmental data (PM2.5, PM10, CO, NO₂, O₃, temperature, humidity) in real time.

**Source:** IoT sensors in cities stream air quality data (timestamp, location, PM2.5, PM10, CO, NO2, O3, temperature and humidity levels every few seconds)

- In this project I used Pub/sub to BigQuery 
  
The Pub/sub template is a streaming pipeline that can read JSON-formatted messages from a Pub/Sub topic and write them to a BigQuery table 

**Workflow:**  
IoT Sensors (Simulated) →  Pub/Sub →  Dataflow (UDF Transform) →  BigQuery →  Tableau Dashboard

**Impact:** To demonstrate how smart cities can monitor environmental conditions and trigger alerts when pollution thresholds are exceeded.

IoT sensors (or the software that manages it, like Raspberry Pi, Arduino, or edge gateway) sends HTTP or gRPC request to Pub/Sub APIs.

Note: *For this project I did not have a real-time streaming data from any IoT sensor so I used a local file as a streaming source **(batch-to-stream trick)***

Python script to read the file line by line and publish each row into Pub/Sub (with a delay e.g., 1 sec per row). These mimics streaming, even though the source is a static file.
