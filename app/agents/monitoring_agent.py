from app.tools.monitoring_executor import MonitoringExecutor


class MonitoringAgent:
    """
    Handles application health monitoring.
    """

    def __init__(self):

        self.name = "Monitoring Agent"
        self.monitor = MonitoringExecutor()


    def check_health(self, service):

        metrics = self.monitor.collect_metrics(service)

        logs = self.monitor.collect_logs(service)

        return {
            "agent": self.name,
            "metrics": metrics,
            "logs": logs,
            "status": "healthy"
        }
