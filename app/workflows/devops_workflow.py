from app.agents.deployment_agent import DeploymentAgent
from app.agents.monitoring_agent import MonitoringAgent
from app.agents.incident_agent import IncidentAgent
from app.agents.security_agent import SecurityAgent


class DevOpsWorkflow:
    """
    Coordinates DevOps agents.
    """

    def __init__(self):
        self.deployment = DeploymentAgent()
        self.monitoring = MonitoringAgent()
        self.incident = IncidentAgent()
        self.security = SecurityAgent()

    def execute(self, application):

        security_result = self.security.scan(application)

        deployment_result = self.deployment.deploy(application)

        monitoring_result = self.monitoring.check_health(application)

        return {
            "security": security_result,
            "deployment": deployment_result,
            "monitoring": monitoring_result
        }
