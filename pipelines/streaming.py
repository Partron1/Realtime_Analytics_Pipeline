# Batch-to-stream simulator with Pub/Sub
import time # adds a delay between sending messages (so it feels like real-time data).
import json
from google.cloud import pubsub_v1 # is the official Google Cloud library for interacting with Pub/Sub.

# Pub/Sub configuration
project_id = "tekstain-25"
topic_id = "air-quality"

publisher = pubsub_v1.PublisherClient() # Connects your script to Pub/Sub.
topic_path = publisher.topic_path(tekstain-25, air-quality) 

# Input file (each line is one "event")
input_file = "air_quality_data.jsonl"  # This is your local data file (static data)

# Publish line by line with delay
with open(input_file, "r") as f: 
    for line in f:  # Reads one record at a time (like a sensor message), Skips empty lines.
        line = line.strip()
        if not line:
            continue

        # Convert to bytes (Pub/Sub requires bytes)
        data = line.encode("utf-8") # Converts your JSON line to bytes (Pub/Sub requires that)
        future = publisher.publish(topic_path, data) # Publishes the message to the Pub/Sub topic.
        print(f"Published message ID: {future.result()}") # Prints the message ID so you know it was sent successfully.

        # Delay between messages to mimic streaming
        time.sleep(1)  # 1 second per event, Mimics how real IoT sensors send data every few seconds.
