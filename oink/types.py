# generated by datamodel-codegen:
#   filename:  dataplane.yaml
#   timestamp: 2020-06-05T15:19:32+00:00

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel


class MetadataServerResponse(BaseModel):
    name: str
    version: str
    extensions: List[str]


class MetadataServerErrorResponse(BaseModel):
    error: str


class MetadataTensor(BaseModel):
    name: str
    datatype: str
    shape: List[float]


class MetadataModelErrorResponse(BaseModel):
    error: str


class Parameters(BaseModel):
    pass


class TensorData(BaseModel):
    __root__: List[Union[TensorData, float, int, str, bool]]


class RequestOutput(BaseModel):
    name: Optional[str] = None
    parameters: Optional[Parameters] = None


class ResponseOutput(BaseModel):
    name: str
    shape: List[float]
    datatype: str
    parameters: Optional[Parameters] = None
    data: TensorData


class InferenceResponse(BaseModel):
    model_name: str
    model_version: Optional[str] = None
    id: str
    parameters: Optional[Parameters] = None
    outputs: List[ResponseOutput]


class InferenceErrorResponse(BaseModel):
    error: Optional[str] = None


class MetadataModelResponse(BaseModel):
    name: str
    versions: Optional[List[str]] = None
    platform: str
    inputs: List[MetadataTensor]


class RequestInput(BaseModel):
    name: str
    shape: List[float]
    datatype: str
    parameters: Optional[Parameters] = None
    data: TensorData


class InferenceRequest(BaseModel):
    id: Optional[str] = None
    parameters: Optional[Parameters] = None
    inputs: List[RequestInput]
    outputs: Optional[List[RequestOutput]] = None


TensorData.update_forward_refs()