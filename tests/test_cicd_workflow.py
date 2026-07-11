from app.workflows.cicd_workflow import CICDWorkflow


def test_cicd_workflow():

    workflow = CICDWorkflow()

    result = workflow.execute("payment-service")

    assert result["status"] == "completed"
    assert "build" in result["pipeline"]
