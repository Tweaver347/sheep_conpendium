
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")

    assert response.status_code == 200

    assert response.json() == {
        "id":1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

#Define a test function for adding a new sheep
def test_add_sheep():
    #TODO: Prepare the new sheep data in a dictionary format
    new_sheep = {
        "id": 7,
        "name": "Luna",
        "breed": "Merino",
        "sex": "ewe"
    }
    #TODO: Send a POST request to the endpoint "/sheep" with the new sheep data.
    # Arguments should be your endpoint and new sheep data
    response = client.post("/sheep", json=new_sheep)
    #TODO: Assert that the response status code is 201 (Created)
    assert response.status_code == 201
    #TODO: Assert that the response JSON matches the new sheep data
    assert response.json() == new_sheep
    #TODO: Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
    # include an assert statement to see if the new sheep data can be retrieved
    response = client.get(f"/sheep/{new_sheep['id']}")
    assert response.status_code == 200
    assert response.json() == new_sheep