
import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_coordinates(state, district, mandal):
    """Find coordinates using the farmer's location details."""

    search_queries = [
        f"{mandal}, {district}, {state}, India",
        f"{district}, {state}, India"
    ]

    for query in search_queries:
        response = requests.get(
            GEOCODING_URL,
            params={
                "name": query,
                "count": 5,
                "language": "en",
                "format": "json"
            },
            timeout=15
        )
        response.raise_for_status()

        results = response.json().get("results", [])

        if results:
            # Prefer a result in the selected state.
            state_match = next(
                (
                    place for place in results
                    if state.lower() in place.get(
                        "admin1", ""
                    ).lower()
                ),
                None
            )

            place = state_match or results[0]

            return {
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "name": place.get("name", query),
                "matched_query": query
            }

    raise ValueError(
        "Location not found. Please check the mandal and district names."
    )


def get_weather(latitude, longitude):
    """Fetch current weather and a 7-day forecast."""

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "apparent_temperature",
            "precipitation",
            "rain"
        ],
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "precipitation_probability_max"
        ],
        "forecast_days": 7,
        "timezone": "auto"
    }

    response = requests.get(
        WEATHER_URL,
        params=params,
        timeout=20
    )
    response.raise_for_status()

    data = response.json()

    if "current" not in data or "daily" not in data:
        raise ValueError("Weather forecast data is incomplete.")

    return {
        "current": data["current"],
        "daily": data["daily"],
        "timezone": data.get("timezone", "Local time")
    }
