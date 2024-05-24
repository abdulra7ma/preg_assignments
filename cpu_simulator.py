
"""
Example usage:
2024-05-24 19:24:36,056 - INFO - CPU intensive task completed
2024-05-24 19:24:36,077 - INFO - CPU intensive task completed
2024-05-24 19:24:36,078 - INFO - CPU intensive task completed
2024-05-24 19:24:36,078 - INFO - CPU intensive task completed
"""

import threading
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def cpu_intensive_task(duration):
    """Function to simulate CPU intensive work."""
    end_time = time.time() + duration
    while time.time() < end_time:
        result = sum(i * i for i in range(10000))
    logging.info("CPU intensive task completed")


def simulate_cpu_work(duration, num_threads):
    """Simulate CPU work using multiple threads."""
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=cpu_intensive_task, args=(duration,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    # Simulate CPU work for 10 seconds using 4 threads
    simulate_cpu_work(duration=10, num_threads=4)


   