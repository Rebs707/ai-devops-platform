class MonitoringExecutor:
    """
    Executes monitoring checks.
    """

    def __init__(self):
        self.name = "Monitoring Executor"

    def collect_metrics(self, service):

        return {
            "executor": self.name,
            "service": service,
            "metrics": {
                "cpu": "normal",
                "memory": "normal",
                "availability": "healthy"
            }
        }

    def collect_logs(self, service):

        return {
            "executor": self.name,
            "service": service,
            "logs": "No critical errors detected"
        }
