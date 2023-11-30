from fastapi import status, APIRouter
from fastapi.responses import JSONResponse
from service.etl_service import etl_dataset_example
from fastapi.encoders import jsonable_encoder
from schemas.elt_schema import EtlBasic
from schemas.api_response_schema import ApiResponseSchema

etl_router = APIRouter()

@etl_router.post('/erp/test', tags=["TEST"], response_model=ApiResponseSchema)
def dwTEST(request_body: EtlBasic):
    object = ApiResponseSchema(status=1, message="OK")
    return JSONResponse(content=jsonable_encoder(object), status_code=status.HTTP_200_OK)

@etl_router.post('/erp/dataset/dw-dataset-example', tags=["EXAMPLE"], response_model=ApiResponseSchema)
def dwDatasetExample(request_body: EtlBasic):
    try:
        object =  etl_dataset_example(request_body.id_cia)
        return JSONResponse(content=jsonable_encoder(object), status_code=status.HTTP_200_OK)
    except Exception as e:
        object = ApiResponseSchema(status=1.2, message=str(e))
        return JSONResponse(content=jsonable_encoder(object), status_code=status.HTTP_400_BAD_REQUEST)