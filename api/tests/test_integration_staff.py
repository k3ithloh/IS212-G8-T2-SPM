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

    def test_get_staff(self):
        """
        Endpoint Tested:
          - GET /staff/{staff_id}
        Scenario:
          - Tests a successful GET request to get a staff details based on given staff_id
        """
        # Provided staff_id
        staff_id = 123456789

        # Get staff details based on staff_id by invoking endpoint
        staff_details = client.get(f"/staff/{staff_id}")

        # Assert that there is a successful response
        assert staff_details.status_code == 200

        # Assert that there is the matching staff details
        assert staff_details.json() == {
            "staff_id": 123456789,
            "fname": "AH GAO",
            "lname": "TAN",
            "dept": "FINANCE",
            "email": "tan_ah_gao@all-in-one.com.sg",
            "phone": "65-1234-5678",
            "biz_address": "60 Paya Lebar Rd, #06-33 Paya Lebar Square, Singapore 409051",
            "sys_role": "staff",
        }

    def test_get_staff_skills(self):
        """
        Endpoint Tested:
          - GET /staff/skills/{staff_id}
        Scenario:
          - Tests a successful GET request to get staff skills based on given staff_id
        """
        # Provided staff_id
        staff_id = 123456789

        # Get staff skills based on staff_id by invoking endpoint
        staff_skills = client.get(f"/staff/skills/{staff_id}")

        # Assert that there is a successful response
        assert staff_skills.status_code == 200

        # Assert that there are the matching staff skills
        assert staff_skills.json() == [
            {
                "staff_id": 123456789,
                "skill_id": 345678790,
                "skill_name": "Typescript Developer",
                "skill_status": "active",
                "ss_status": "in-progress",
            },
            {
                "staff_id": 123456789,
                "skill_id": 345678866,
                "skill_name": "Java Developer",
                "skill_status": "active",
                "ss_status": "active",
            },
            {
                "staff_id": 123456789,
                "skill_id": 345678890,
                "skill_name": "VMWare Villian",
                "skill_status": "inactive",
                "ss_status": "unverified",
            },
            {
                "staff_id": 123456789,
                "skill_id": 345678912,
                "skill_name": "Pascal Programming",
                "skill_status": "inactive",
                "ss_status": "active",
            },
            {
                "staff_id": 123456789,
                "skill_id": 345678927,
                "skill_name": "LinkedIn Master",
                "skill_status": "active",
                "ss_status": "in-progress",
            },
            {
                "staff_id": 123456789,
                "skill_id": 345678935,
                "skill_name": "MongoDB Maniac",
                "skill_status": "active",
                "ss_status": "in-progress",
            },
        ]

    def test_get_staff_role_skills_match(self):
        """
        Endpoint Tested:
          - GET /staff/role-skills-match/{staff_id}/{role_listing_id}
        Scenario:
          - Tests a successful GET request to get the matches and mismatches between staff skills and given role_listing required skills
        """
        # Provided role_id
        staff_id = 123456789
        role_listing_id = 312

        # Get staff matched and mismatched skills with role_listing based on staff_id and role_listing_id by invoking endpoint
        skill_match_details = client.get(
            f"/staff/role-skills-match/{staff_id}/{role_listing_id}"
        )

        # Assert that there is a successful response
        assert skill_match_details.status_code == 200

        # Assert that there are the matching and mistmached staff skills with given role_listing
        assert skill_match_details.json() == {
            "match": {
                "active": [
                    {
                        "skill_id": 345678866,
                        "skill_name": "Java Developer",
                        "skill_status": "active",
                        "ss_status": "active",
                    }
                ],
                "in_progress": [
                    {
                        "skill_id": 345678790,
                        "skill_name": "Typescript Developer",
                        "skill_status": "active",
                        "ss_status": "in-progress",
                    }
                ],
                "unverified": [],
            },
            "missing": [
                {
                    "skill_id": 345678922,
                    "skill_name": "React Beast",
                    "skill_status": "active",
                }
            ],
        }

    def test_get_staff_role_listing_application_status(self):
        """
        Endpoint Tested:
          - GET /staff/role/{staff_id}/{role_listing_id}
        Scenario:
          - Tests a successful GET request to get the application status of a staff for a given role_listing
        """
        # Provided role_id
        staff_id = 123456789
        role_listing_id = 312

        # Get staff role_listing_application status based on staff_id and role_listing_id by invoking endpoint
        staff_role_listing_application = client.get(
            f"/staff/role/{staff_id}/{role_listing_id}"
        )

        # Assert that there is a successful response
        assert staff_role_listing_application.status_code == 200

        # Assert that there is the matching staff role_listing_application
        assert staff_role_listing_application.json() == {
            "role_app_status": "applied",
            "role_app_id": 10,
            "role_listing_id": 312,
            "staff_id": 123456789,
            "role_app_ts_create": "2023-10-30T04:52:25",
        }
