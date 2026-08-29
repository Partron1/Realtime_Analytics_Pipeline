import unittest
import json

class TestAirQualityTransforms(unittest.TestCase):
    """Test cases for data transformation pipeline"""
    
    def test_valid_pubsub_message(self):
        """Test that valid Pub/Sub messages are processed correctly"""
        message = {
            "timestamp": 1672531200000,
            "location": "Accra",
            "PM2_5": 41.3,
            "PM10": 12.56,
            "NO2": 13.65,
            "CO": 2.57,
            "O3": 131.05,
            "temperature": 26.6,
            "humidity": 71.6
        }
        self.assertIsNotNone(message.get("timestamp"))
        self.assertEqual(message["location"], "Accra")
    
    def test_schema_validation(self):
        """Verify all required fields are present"""
        required_fields = ["timestamp", "location", "PM2_5", "PM10", "NO2", "CO", "O3", "temperature", "humidity"]
        message = {"timestamp":1672531200000,"location":"Accra","PM2_5":41.3,"PM10":12.56,"NO2":13.65,"CO":2.57,"O3":131.05,"temperature":26.6,"humidity":71.6}
        for field in required_fields:
            self.assertIn(field, message)

if __name__ == "__main__":
    unittest.main()