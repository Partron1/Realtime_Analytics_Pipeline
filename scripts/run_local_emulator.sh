#!/bin/bash
# Local testing with DirectRunner

echo "Starting local pipeline test..."

# Set up Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Run with DirectRunner (no GCP, local machine)
python -m pipelines.streaming \
    --runner=DirectRunner \
    --input_topic=local-test-topic \
    --output_table=local-test-table \
    --temp_location=/tmp/beam-temp

echo "Local pipeline test complete!"