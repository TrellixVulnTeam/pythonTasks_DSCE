import unittest
from unittest.mock import Mock

from my_service import MyService
from fake_single_sign_on_registry import *

class MyServiceTest(unittest.TestCase):
    def test_invalid_token(self):
        registry = FakeSingleSignOnRegistry()
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=None)
        self.assertIn("please, enter your login details", response)

    def test_valid_token(self):
        registry = FakeSingleSignOnRegistry()
        token = registry.register("valid credentials")
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token)
        self.assertIn("hello world", response)

    def test_invalid_token_with_mock(self):
        token = SSOToken()
        registry = MockSingleSignOnRegistry(expected_token=token, token_is_valid=False)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=token)
        self.assertTrue(registry.is_valid_was_called)

    def test_valid_token_with_mock(self):
        token = SSOToken()
        registry = MockSingleSignOnRegistry(expected_token=token, token_is_valid=True)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token)
        self.assertTrue(registry.is_valid_was_called)

    def test_invalid_token_with_spy(self):
        token = SSOToken()
        registry = SpySingleSignOnRegistry(accept_all_tokens=False)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=token)
        self.assertIn(token, registry.checked_tokens)

    def test_valid_token_with_spy(self):
        token = SSOToken()
        registry = SpySingleSignOnRegistry(accept_all_tokens=True)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=token)
        self.assertIn(token, registry.checked_tokens)

    def test_invalid_token_with_mocking_fw_as_spy(self):
        invalid_token = SSOToken()
        registry = Mock(SpySingleSignOnRegistry)
        def is_valid(token):
            if not token == invalid_token:
                raise Exception("Got the wrong token")
            return False
        registry.is_valid = Mock(side_effect=is_valid)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=invalid_token)
        registry.is_valid.assert_called_with(invalid_token)

    def test_valid_token_with_mocking_fw_as_spy(self):
        valid_token = SSOToken()
        registry = Mock(SpySingleSignOnRegistry)
        def is_valid(token):
            if not token == valid_token:
                raise Exception("Got the wrong token")
            return False
        registry.is_valid = Mock(side_effect=is_valid)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=valid_token)
        registry.is_valid.assert_called_with(valid_token)