# Operational Runbook

## Quick Start

### Step 1: Setup (One-time)
- Create GCP project
- Enable required APIs (Dataflow, Pub/Sub, BigQuery, Cloud Storage)
- Create service account and grant roles

### Step 2: Create Pub/Sub Topic
```bash
gcloud pubsub topics create air-quality
```

### Step 3: Run Publisher
```bash
python publisher/simulator.py
```

### Step 4: Deploy Dataflow
```bash
bash scripts/deploy_dataflow.sh
```

### Step 5: Monitor Results
- Check BigQuery for incoming data
- View Dataflow job dashboard
- Connect Tableau for visualization

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Pub/Sub connection error | Verify service account has Pub/Sub Editor role |
| BigQuery write fails | Check IAM permissions and table schema |
| No data appearing | Ensure publisher is running and topic is created |
| Dataflow job stalled | Check worker logs in Cloud Logging |

## Monitoring

- **Dataflow Dashboard**: Monitor job status, throughput, errors
- **BigQuery Console**: Query results, check data freshness
- **Cloud Logging**: Review pipeline errors and warnings