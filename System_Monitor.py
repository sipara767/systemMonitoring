import psutil
import logging


class SystemMonitor:
    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_memory_utilization(self):
        return psutil.virtual_memory().percent

    def log_event(self, message):
        current_cpu_usage = self.get_cpu_usage()
        current_memory_usage = self.get_memory_utilization()
        message = f"{message} (CPU: {current_cpu_usage}%, Memory: {current_memory_usage}%)"
        logging.info(message)
