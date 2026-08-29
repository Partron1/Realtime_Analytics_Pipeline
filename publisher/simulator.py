# Multi-device IoT stream simulator (Python)
import time
import json
import random
from datetime import datetime
from google.cloud import pubsub_v1

# Pub/Sub configuration
project_id = "tekstain-25"
topic_id = "air-quality"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# Simulated IoT devices
device_ids = [f"device-{i}" for i in range(1, 6)]  # device-1 ... device-5

# Input file (one row = one payload)
input_file = "air_quality_data.jsonl"  # or .csv

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        # Choose a random device
        device_id = random.choice(device_ids)

        # Build IoT-style message
        message = {
            "device_id": device_id,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "payload": json.loads(line) if line.startswith("{") else {"raw": line}
        }

        # Publish to Pub/Sub
        data = json.dumps(message).encode("utf-8")
        future = publisher.publish(topic_path, data)
        print(f"Published from {device_id}, message ID: {future.result()}")

        # Delay between events
        time.sleep(1)  # 1 second per simulated event