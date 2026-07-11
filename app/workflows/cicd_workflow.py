from app.agents.cicd_agent import CICDAgent


class CICDWorkflow:

    def __init__(self):
        self.agent = CICDAgent()

    def execute(self, application):

        return self.agent.build_pipeline(application)
