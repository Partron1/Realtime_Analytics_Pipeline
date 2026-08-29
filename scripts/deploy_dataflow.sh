#!/bin/bash
# Deploy to Google Cloud Dataflow

PROJECT_ID="tekstain-25"
TOPIC_ID="air-quality"
OUTPUT_TABLE="tekstain-25:pollution.air_quality"
TEMP_LOCATION="gs://teckflow_bucket/temp/"
STAGING_LOCATION="gs://teckflow_bucket/staging/"

echo "Deploying Dataflow job..."

python -m pipelines.streaming \
    --runner=DataflowRunner \
    --project=$PROJECT_ID \
    --input_topic=projects/$PROJECT_ID/topics/$TOPIC_ID \
    --output_table=$OUTPUT_TABLE \
    --temp_location=$TEMP_LOCATION \
    --staging_location=$STAGING_LOCATION \
    --num_workers=2 \
    --max_num_workers=10 \
    --machine_type=n1-standard-2 \
    --region=us-central1

echo "Dataflow job deployed successfully!"