import os
import sys

import pytest
from fastapi.testclient import TestClient

import database.services as db_services
from api.main import app

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
client = TestClient(app)


class TestIntegrationStaff:
    @pytest.fixture(autouse=True)
    def setup(self):
        """
        Health check first.
        """
        # Asserting that backend and database is working
        healthcheck = client.get("/healthcheck")
        assert healthcheck.status_code == 200
        assert (
            healthcheck.json().get("database")
            == "Database connection successful!"
        )

    def test_get_clerk_staff_id(self):
        """
        Endpoint Tested:
          - GET staff/clerk/{clerk_id}
        Scenario:
          - Tests a successful GET request to get the relevant staff details information based on given clerk_id
        """
        # Provided clerk_id
        clerk_id = "user_2VyiaGNu4nOSAj7ZleHdwpoVORt"

        # Get staff details based on clerk_id by invoking endpoint
        staff_details = client.get(
            f"/staff/clerk/{clerk_id}",
        )

        # Assert that there is a successful response
        assert staff_details.status_code == 200

        # Assert that there is the matching staff details
        assert staff_details.json() == {
            "staff_id": 123456787,
            "fname": "FAUD",
            "lname": "NIZAM",
            "dept": "SALES",
            "email": "faud_nizam@all-in-one.com.sg",
            "phone": "60-03-21345678",
            "biz_address": "Unit 3A-07, Tower A, The Vertical Business Suite, 8, Jalan Kerinchi, Bangsar South, 59200 Kuala Lumpur, Malaysia",
            "sys_role": "manager",
        }

    def test_get_managers(self):
        """
        Endpoint Tested:
          - GET /staff/manager
        Scenario:
          - Tests a successful GET request to get all manager details
        """
        #  Get all manager details by invoking endpoint
        managers_details = client.get("/staff/manager")

        # Assert that there is a successful response
        assert managers_details.status_code == 200

        # Assert that there are the matching managers details
        assert managers_details.json() == [
            {
                "staff_id": 123456787,
                "fname": "FAUD",
                "lname": "NIZAM",
                "dept": "SALES",
                "email": "faud_nizam@all-in-one.com.sg",
                "phone": "60-03-21345678",
                "biz_address": "Unit 3A-07, Tower A, The Vertical Business Suite, 8, Jalan Kerinchi, Bangsar South, 59200 Kuala Lumpur, Malaysia",
                "sys_role": "manager",
            }
        ], "Response body matches the expected response"
