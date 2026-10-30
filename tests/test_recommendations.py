
import pytest

from recommendations import (
    get_crop_recommendations,
    get_season
)


def test_rabi_season():
    assert get_season(10) == "Rabi"


def test_kharif_season():
    assert get_season(7) == "Kharif"


def test_zaid_season():
    assert get_season(4) == "Zaid"


def test_recommendations_return_structure():
    result = get_crop_recommendations(
        soil="Black",
        irrigation="Limited",
        temperature=25,
        rainfall_mm=15,
        rainfall_probability=40,
        month=10
    )

    assert "recommended" in result
    assert "less_suitable" in result
    assert "season" in result


def test_recommendations_have_scores():
    result = get_crop_recommendations(
        soil="Black",
        irrigation="Limited",
        temperature=25,
        rainfall_mm=15,
        rainfall_probability=40,
        month=10
    )

    for crop in result["recommended"]:
        assert 0 <= crop["score"] <= 100


def test_invalid_soil():
    with pytest.raises(ValueError):
        get_crop_recommendations(
            soil="Invalid",
            irrigation="Limited",
            temperature=25,
            rainfall_mm=15,
            rainfall_probability=40,
            month=10
        )


def test_invalid_rainfall_probability():
    with pytest.raises(ValueError):
        get_crop_recommendations(
            soil="Black",
            irrigation="Limited",
            temperature=25,
            rainfall_mm=15,
            rainfall_probability=120,
            month=10
        )
