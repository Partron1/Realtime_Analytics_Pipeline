# Batch-to-stream simulator with Pub/Sub
import time
import json
from google.cloud import pubsub_v1

# Pub/Sub configuration
project_id = "tekstain-25"
topic_id = "air-quality"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# Input file (each line is one "event")
input_file = "air_quality_data.jsonl"  # This is your local data file (static data)

# Publish line by line with delay
with open(input_file, "r") as f:
    for line in f:  # Reads one record at a time (like a sensor message)
        line = line.strip()
        if not line:
            continue

        # Convert to bytes (Pub/Sub requires bytes)
        data = line.encode("utf-8")
        future = publisher.publish(topic_path, data)
        print(f"Published message ID: {future.result()}")

        # Delay between messages to mimic streaming
        time.sleep(1)  # 1 second per event