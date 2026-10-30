
import requests
from functools import lru_cache

BASE_URL = "https://india-lgd-index-api.vercel.app/v1"


def fetch_data(endpoint, params=None):
    """Fetch administrative location data."""
    response = requests.get(
        f"{BASE_URL}/{endpoint}",
        params=params,
        timeout=20
    )
    response.raise_for_status()

    result = response.json()

    if not result.get("success"):
        raise ValueError("Unable to load location information.")

    return result


@lru_cache(maxsize=1)
def get_states():
    result = fetch_data("states")

    return result["data"], result["meta"]


@lru_cache(maxsize=36)
def get_district_records(state_code):
    result = fetch_data(
        "districts",
        {"state": state_code}
    )
    return result["data"]


@lru_cache(maxsize=1000)
def get_subdistrict_records(district_code):
    result = fetch_data(
        "subdistricts",
        {"district": district_code}
    )
    return result["data"]


def get_state_names():
    states, meta = get_states()
    return sorted(states, key=lambda item: item["name"].lower())


def get_district_names(state_code):
    districts = get_district_records(str(state_code))
    return sorted(districts, key=lambda item: item["name"].lower())


def get_subdistrict_names(district_code):
    subdistricts = get_subdistrict_records(str(district_code))
    return sorted(subdistricts, key=lambda item: item["name"].lower())


def get_source_date():
    states, meta = get_states()
    return meta.get("source_date", "Unknown")


def get_attribution():
    states, meta = get_states()
    return meta.get("attribution", {})
