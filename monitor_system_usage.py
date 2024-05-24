import psutil # type: ignore
import GPUtil
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def monitor_disk_usage():
    """Monitor and log the disk usage."""
    disk_usage = psutil.disk_usage('/')
    logging.info(f"Disk Usage: {disk_usage.percent}%")

def monitor_gpu_usage():
    """Monitor and log the GPU usage."""
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]
        gpu_usage = gpu.load * 100  # GPU load is a fraction, so multiply by 100 to get percentage
        logging.info(f"GPU Usage: {gpu_usage:.2f}%")
    else:
        logging.warning("No GPU found")

def main():
    """Main function to continuously monitor system usage."""
    while True:
        monitor_disk_usage()
        monitor_gpu_usage()
        time.sleep(1)

if __name__ == "__main__":
    main()
