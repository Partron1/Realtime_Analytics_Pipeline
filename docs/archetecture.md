# Architecture Overview

## Data Flow Diagram

```
IoT Sensors (Simulated) → Pub/Sub → Dataflow (UDF Transform) → BigQuery → Tableau Dashboard
```

## Components

### 1. **Pub/Sub Topic**
- Topic ID: `air-quality`
- Input format: JSON messages with air quality metrics
- Schema: timestamp, location, PM2.5, PM10, NO2, CO, O3, temperature, humidity

### 2. **Dataflow Pipeline**
- Runner: DataflowRunner (production) / DirectRunner (local testing)
- Input: Pub/Sub messages
- Transform: Data validation, schema enforcement
- Output: BigQuery table

### 3. **BigQuery Dataset**
- Dataset: `pollution`
- Table: `air_quality`
- Partitioned by: `timestamp` field
- Retention: 90 days (configurable)

### 4. **Tableau Dashboard**
- Connection type: Live (real-time)
- Charts: Time series, heatmaps, KPI cards
- Alerts: Email-based when thresholds exceeded

## Deployment Steps

1. Create Pub/Sub topic
2. Run publisher simulator
3. Deploy Dataflow job using `scripts/deploy_dataflow.sh`
4. Connect Tableau to BigQuery
5. Monitor in BigQuery console

## Security Considerations

- Use service account instead of default Compute Engine account
- Enable "Public Access Prevention" on Cloud Storage bucket
- Grant minimal IAM roles (Dataflow Admin, Storage Admin, Pub/Sub Editor, BigQuery Data Editor)
