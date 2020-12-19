from .. import API_URL

from ..models import (
                      AccountBalanceRequest,
                      AccountCoinsRequest,
                      BlockRequest,
                      BlockTransactionRequest,
                      MempoolTransactionRequest,
                      MetadataRequest,
                      NetworkRequest,
                      NetworkListResponse
                     )

from ..utils.communication import post_request

def get_available_networks(req : MetadataRequest):
    """
    req: MetadataRequest
    resp: NetworkListResponse
    ref: /network/list
    """
    url = '{}/network/list'.format(API_URL)
    resp = post_request(url, req.json())
    return NetworkListResponse(**resp.json())

def get_network_options():
    """
    req: NetworkRequest
    resp: NetworkOptionsResponse
    ref: /network/options
    """
    pass

def get_network_status():
    """
    req: NetworkRequest
    resp: NetworkStatusResponse
    ref: /network/status
    """
    pass

def get_account_balance():
    """
    req: AccountBalanceRequest
    resp: AccountBalanceResponse
    ref: /account/balance
    """
    pass

def get_account_unspent_coins():
    """
    req: AccountCoinsRequest
    resp: AccountCoinsResponse
    ref: /account/coins
    """
    pass

def get_block():
    """
    req: BlockRequest
    resp: BlockResponse
    ref: /block
    """
    pass
    
def get_block_transaction():
    """
    req: BlockTransacitonRequest
    resp: BlockTransactionResponse
    ref: /block/transaction
    """
    pass


def get_mempool_transaction_ids():
    """
    req: NetworkRequest
    resp: MempoolResponse
    ref: /mempool
    """
    pass

def get_mempool_transaction():
    """
    req: MempoolTransactionRequest
    resp: MempoolTransactionResponse
    ref: /mempool/transaction
    """
    pass