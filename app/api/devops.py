from fastapi import APIRouter

from app.services.devops_service import DevOpsService


router = APIRouter()

service = DevOpsService()


@router.post("/deploy/{application}")
def deploy(application: str):

    result = service.deploy_application(application)

    return {
        "application": application,
        "workflow": result
    }
