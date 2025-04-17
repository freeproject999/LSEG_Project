import logging
import os

# Configure logging
log_format = '%(asctime)s,%(message)s'
logging.basicConfig(level=logging.INFO, format=log_format, datefmt='%H:%M:%S')

def process_log_file(log_file_path):
    # Check if the log file exists
    if not os.path.exists(log_file_path):
        logging.error(f"Log file not found: {log_file_path}")
        return

    try:
        with open(log_file_path, mode='r') as file:
            for line in file:
                # Strip whitespace and split the line into components
                parts = line.strip().split(',')
                if len(parts) != 4:
                    logging.warning(f"Invalid log entry: {line.strip()}")
                    continue
                
                time_str, job_name, status, pid = parts
                # Log the job start or end
                if status.strip() == 'START':
                    logging.info(f'scheduled task {job_name.strip()}, START, {pid.strip()}')
                elif status.strip() == 'END':
                    logging.info(f'scheduled task {job_name.strip()}, END, {pid.strip()}')
                else:
                    logging.warning(f"Unknown status '{status.strip()}' for job '{job_name.strip()}'")

    except Exception as e:
        logging.error(f"An error occurred while processing the log file: {e}")

if __name__ == "__main__":
    log_file_path = '../logs/logs.log'  # Adjust the path if necessary
    process_log_file(log_file_path)