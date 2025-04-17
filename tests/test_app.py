import unittest
from src.app import process_log_file  # Assuming this is the function you want to test

class TestLogMonitoring(unittest.TestCase):

    def test_process_log_file(self):
        # Sample log data
        log_data = [
            "2023-01-01 12:00:00, Job1, START",
            "2023-01-01 12:05:00, Job1, END",
            "2023-01-01 12:10:00, Job2, START",
            "2023-01-01 12:20:00, Job2, END",
        ]
        
        # Expected output
        expected_output = {
            "Job1": 5,  # Job1 duration in minutes
            "Job2": 10,  # Job2 duration in minutes
        }
        
        # Call the function to test
        result = process_log_file(log_data)
        
        # Assert the result matches the expected output
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()