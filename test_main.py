from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]
    def test_cities_in_spain():
        response = client.get("/countries/Spain/cities")
        assert response.status_code == 200
        assert "Madrid" in response.json()  # Assuming Madrid is one of the cities in Spain

    def test_monthly_average_in_madrid():
        response = client.get("/countries/Spain/Madrid/January")
        assert response.status_code == 200
        assert "average_temperature" in response.json()  # Assuming the response contains average temperature data