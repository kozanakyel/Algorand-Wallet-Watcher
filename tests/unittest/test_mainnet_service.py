import pytest
from unittest.mock import patch, MagicMock
from algo_wallet_watcher.Infrastructure.services.mainnet_wallet_service import (
    MainnetWalletService,
)


@pytest.fixture
def mock_requests_get():
    with patch(
        "algo_wallet_watcher.Infrastructure.services.mainnet_wallet_service.requests.get"
    ) as mock:
        yield mock


def test_get_account_info_success(mock_requests_get):
    # Why response.json()["status"] not found i dont know???
    algorand_address = "SLGYSO6ZRYW5FOJCYPLXSBMKFAGOV3QUZ3AZZ3LRAJMSJDDH63RIJDYJUU"
    expected_response = {
        "address": "SLGYSO6ZRYW5FOJCYPLXSBMKFAGOV3QUZ3AZZ3LRAJMSJDDH63RIJDYJUU",
        "amount": 100,
        "state": "Offline",
    }
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = expected_response
    mock_requests_get.return_value = mock_response

    service = MainnetWalletService()
    result = service.get_account_info(algorand_address)
    print(result)

    assert result == expected_response


def test_get_account_info_failure(mock_requests_get):
    algorand_address = "test_address"
    expected_error = {"error": '400 - {"message":"failed to parse the address"}\n'}
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.text = '{"message":"failed to parse the address"}\n'
    mock_requests_get.return_value = mock_response

    service = MainnetWalletService()
    result = service.get_account_info(algorand_address)

    assert result == expected_error
