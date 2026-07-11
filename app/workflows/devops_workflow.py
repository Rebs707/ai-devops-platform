from app.agents.deployment_agent import DeploymentAgent
from app.agents.monitoring_agent import MonitoringAgent
from app.agents.incident_agent import IncidentAgent
from app.agents.security_agent import SecurityAgent
from app.agents.cicd_agent import CICDAgent


class DevOpsWorkflow:
    """
    End-to-end AI DevOps workflow.
    """

    def __init__(self):

        self.cicd = CICDAgent()
        self.security = SecurityAgent()
        self.deployment = DeploymentAgent()
        self.monitoring = MonitoringAgent()
        self.incident = IncidentAgent()


    def execute(self, application):

        pipeline = self.cicd.build_pipeline(application)

        security = self.security.scan(application)

        deployment = self.deployment.deploy(application)

        monitoring = self.monitoring.check_health(application)

        return {
            "pipeline": pipeline,
            "security": security,
            "deployment": deployment,
            "monitoring": monitoring
        }
