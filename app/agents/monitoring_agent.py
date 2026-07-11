from app.tools.aws_tool import AWSTool


class MonitoringAgent:

    def __init__(self):
        self.name = "Monitoring Agent"
        self.aws = AWSTool()

    def check_health(self, service):

        environment = self.aws.check_environment(service)

        return {
            "agent": self.name,
            "environment": environment,
            "status": "healthy"
        }
