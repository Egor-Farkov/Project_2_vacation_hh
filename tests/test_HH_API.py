from unittest.mock import patch

from src.HH_API import HeadHunterAPI


def test_hh_api(hh_api_data: dict) -> None:
    """Тест"""
    hh_api = HeadHunterAPI()
    assert isinstance(hh_api, HeadHunterAPI)

    with patch("requests.get") as mock:
        mock.return_value.status_code = 200
        mock.return_value.json.return_value = hh_api_data
        l_vac = hh_api.load_vacancies("Водитель")
        assert isinstance(l_vac, list)
