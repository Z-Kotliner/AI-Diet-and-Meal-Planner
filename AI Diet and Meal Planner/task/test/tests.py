import json
import requests
from hstest import StageTest, CheckResult, dynamic_test

class FastAPIStageTest(StageTest):
    @dynamic_test(time_limit=120_000)
    def test_search_endpoint(self):
        url = 'http://localhost:8000'

        try:
            response = requests.get(f"{url}/")
        except requests.exceptions.ConnectionError:
            return CheckResult.wrong("Cannot connect to the server at 'http://localhost:8000'. Ensure the FastAPI app is running.")

        if response.status_code != 200:
            return CheckResult.wrong(f"Expected status code 200, but got {response.status_code}.")

        try:
            response_data = response.json()
        except json.JSONDecodeError:
            return CheckResult.wrong("Response is not valid JSON.")
        if response.json().get("message", "") != 'Success!':
            return CheckResult.wrong(f"Expected 'Success!' as the 'message' value, but got {response.json().get('message', '')}.")


        return CheckResult.correct()


if __name__ == '__main__':
    FastAPIStageTest().run_tests()