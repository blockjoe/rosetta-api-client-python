from typing import Optional
from urllib.parse import urljoin

import requests

from ..models import (
    ConstructionCombineRequest,
    ConstructionCombineResponse,
    ConstructionDeriveRequest,
    ConstructionDeriveResponse,
    ConstructionHashRequest,
    ConstructionMetadataRequest,
    ConstructionMetadataResponse,
    ConstructionParseRequest,
    ConstructionParseResponse,
    ConstructionPayloadsRequest,
    ConstructionPayloadsResponse,
    ConstructionPreprocessRequest,
    ConstructionPreprocessResponse,
    ConstructionSubmitRequest,
    TransactionIdentifierResponse
)

from ..utils.communication import post_request


def create_network_transaction_from_signatures(api_url : str, req : ConstructionCombineRequest, session : Optional[requests.Session] = None) -> ConstructionCombineResponse:
    """
    req: ConstructionCombineRequest
    resp: ConstructionCombineResponse
    ref: /construction/combine
    """
    url = urljoin(api_url, 'construction/combine')
    resp = post_request(url, req.json(), session)
    return ConstructionCombineResponse(**resp.json())

def derive_account_id_from_pubkey(api_url : str, req : ConstructionDeriveRequest, session : Optional[requests.Session] = None) -> ConstructionDeriveResponse:
    """
    req: ConstructionDeriveRequest
    resp: ConstructionDeriveResponse
    ref: /construction/derive
    """
    url = urljoin(api_url, 'construction/derive')
    resp = post_request(url, req.json(), session)
    return ConstructionDeriveResponse(**resp.json())

def get_hash_of_signed_transaction(api_url : str, req : ConstructionHashRequest, session : Optional[requests.Session] = None) -> TransactionIdentifierResponse:
    """
    req: ConstructionHashRequest
    resp: TransactionIdentifierResponse
    ref: /construction/hash
    """
    url = urljoin(api_url, 'construction/hash')
    resp = post_request(url, req.json(), session)
    return TransactionIdentifierResponse(**resp.json())

def get_metadata_for_transaction_construction(api_url : str, req : ConstructionMetadataRequest, session : Optional[requests.Session] = None) -> ConstructionMetadataResponse:
    """
    req: ConstructionMetadataRequest
    resp: ConstructionMetadataResponse
    ref: /construction/metadata
    """
    url = urljoin(api_url, 'construction/metadata')
    resp = post_request(url, req.json(), session)
    return ConstructionMetadataResponse(**resp.json())

def parse_transaction(api_url : str, req : ConstructionParseRequest, session : Optional[requests.Session] = None) -> ConstructionParseResponse:
    """
    req: ConstructionParseRequest
    resp: ConstructionParseResponse
    ref: /construction/parse
    """
    url = urljoin(api_url, 'construction/parse')
    resp = post_request(url, req.json(), session)
    return ConstructionParseResponse(**resp.json())

def generate_unsigned_transaction_and_signing_payloads(api_url : str, req : ConstructionPayloadsRequest, session : Optional[requests.Session] = None) -> ConstructionPayloadsResponse:
    """
    req: ConstructionPayloadsRequest
    resp: ConstructionPayloadsResponse
    ref: /construction/payloads
    """
    url = urljoin(api_url, 'construction/payloads')
    resp = post_request(url, req.json(), session)
    return ConstructionPayloadsResponse(**resp.json())

def create_request_to_fetch_metadata(api_url : str, req : ConstructionPreprocessRequest, session : Optional[requests.Session] = None) -> ConstructionPreprocessResponse:
    """
    req: ConstructionPreprocessRequest
    resp: ConstructionPreprocessResponse
    ref: /construction/preprocess
    """
    url = urljoin(api_url, 'construction/preprocess')
    resp = post_request(url, req.json(), session)
    return ConstructionPreprocessResponse(**resp.json())

def submit_signed_transaction(api_url : str, req : ConstructionSubmitRequest, session : Optional[requests.Session] = None) -> TransactionIdentifierResponse:
    """
    req: ConstructionSubmitRequest
    resp: TransactionIdentifierResponse
    ref: /construction/submit
    """
    url = urljoin(api_url, 'construction/submit')
    resp = post_request(url, req.json(), session)
    return TransactionIdentifierResponse(**resp.json())
