from app.workflows.devops_workflow import DevOpsWorkflow


def test_devops_workflow():

    workflow = DevOpsWorkflow()

    result = workflow.execute("payment-service")

    assert result["security"]["status"] == "secure"
    assert result["deployment"]["status"] == "completed"
    assert result["monitoring"]["status"] == "healthy"
