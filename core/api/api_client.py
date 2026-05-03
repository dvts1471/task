from typing import Any, Optional, Callable

import allure
from requests import Response, Session

from config import BASE_HOST, API_TOKEN, API_MODULE
from core.api.api_expected_response import ApiExpectedResponse
from core.utils.logger import Logger


class ApiClient:
    SERVICE: str = ""
    HOST: str = (BASE_HOST or "") + API_MODULE

    def __init__(self) -> None:
        self.logger = Logger(self.__class__.__name__)
        self.session = Session()
        self.__auth()

    def __repr__(self) -> str:
        return self.__class__.__name__

    def __auth(self) -> None:
        self.session.headers.update({"x-user-id": API_TOKEN or ""})

    @property
    def service_url(self) -> str:
        return f"{self.HOST}{self.SERVICE}"

    @property
    def request_headers(self) -> dict[str, str]:
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        return headers

    def get(self, url: str, params: Optional[dict[Any, Any]] = None) -> Response:
        if params is None:
            params = {}
        return self.session.get(url, headers=params.get("headers", {}), verify=False)

    def post(self, url: str, params: Optional[dict[Any, Any]] = None) -> Response:
        if params is None:
            params = {}
        return self.session.post(url, verify=False, **params)

    def put(self, url: str, params: Optional[dict[Any, Any]] = None) -> Response:
        if params is None:
            params = {}
        return self.session.put(url, verify=False, **params)

    def delete(self, url: str, params: Optional[dict[Any, Any]] = None) -> Response:
        if params is None:
            params = {}
        return self.session.delete(url, verify=False, **params)

    def patch(self, url: str, params: Optional[dict[Any, Any]] = None) -> Response:
        if params is None:
            params = {}
        return self.session.patch(url, verify=False, **params)

    def get_request_method(
        self, method: str
    ) -> Callable[[str, Optional[dict[Any, Any]]], Response]:
        if method == "GET":
            return self.get
        elif method == "POST":
            return self.post
        elif method == "DELETE":
            return self.delete
        elif method == "PUT":
            return self.put
        elif method == "PATCH":
            return self.patch
        else:
            raise Exception(f"Provide correct HTTP method! Provided: {method}")

    @allure.step(
        "Send {method} request to {url} with body: {body} and headers: {headers}"
    )
    def send_request(
        self,
        method: str,
        url: str,
        body: Optional[dict[Any, Any]] = None,
        headers: Optional[dict[str, str]] = None,
        verify_schema: bool = True,
    ) -> Response:
        if headers:
            request_headers = {
                **self.request_headers,
                **headers,
            }
        else:
            request_headers = self.request_headers

        request_method = self.get_request_method(method)
        params = {"headers": request_headers, "json": body}
        response = request_method(url, params)
        self.logger.info(
            f"{method} request to {url} with headers: {request_headers} and body: {body}"
        )
        return response

    def verify_response(
        self,
        actual_response: Response,
        expected_response: ApiExpectedResponse,
    ) -> None:
        if expected_response.status_code == actual_response.status_code:
            model = expected_response.model
            res_body = actual_response.json()
            if model is None:
                return
            try:
                model.model_validate(res_body)
            except Exception as e:
                err_text = f"Test failed: response is invalid:\n{e}"
                self.logger.error(err_text)
                raise AssertionError(err_text)
        else:
            err_text = (
                f"Response status code is invalid!\n"
                f"Actual: {actual_response.status_code}\tExpected: {expected_response.status_code}\n"
                f"Actual text: {actual_response.text}"
            )
            self.logger.error(err_text)
            raise AssertionError(err_text)
