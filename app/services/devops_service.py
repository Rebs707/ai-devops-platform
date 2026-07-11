from app.workflows.devops_workflow import DevOpsWorkflow


class DevOpsService:

    def __init__(self):
        self.workflow = DevOpsWorkflow()

    def deploy_application(self, application):
        return self.workflow.execute(application)
