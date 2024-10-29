
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
    new_sheep = {
        "id": 7,
        "name": "Luna",
        "breed": "Merino",
        "sex": "ewe"
    }
    response = client.post("/sheep", json=new_sheep)

    assert response.status_code == 201
    assert response.json() == new_sheep

    response = client.get(f"/sheep/{new_sheep['id']}")

    assert response.status_code == 200
    assert response.json() == new_sheep

def test_delete_sheep():
    # Step 1: Delete an existing sheep (using ID 1, which is "Spice")
    delete_response = client.delete("/sheep/1")
    assert delete_response.status_code == 204  # Confirm deletion status

    # Step 2: Try to retrieve the deleted sheep
    get_response = client.get("/sheep/1")
    assert get_response.status_code == 404  # Confirm sheep no longer exists


def test_update_sheep():
    # Step 1: Add a sheep to be updated
    original_sheep = {
        "id": 9,
        "name": "Shadow",
        "breed": "Black Welsh Mountain",
        "sex": "ram"
    }
    response = client.post("/sheep", json=original_sheep)
    assert response.status_code == 201  # Ensure it was added successfully

    # Step 2: Update the sheep's data
    updated_sheep = {
        "id": 9,  # Same ID to ensure we're updating, not creating a new one
        "name": "Shadowfax",
        "breed": "Black Welsh Mountain",
        "sex": "ram"
    }
    update_response = client.put(f"/sheep/{original_sheep['id']}", json=updated_sheep)
    assert update_response.status_code == 200  # Confirm update status
    assert update_response.json() == updated_sheep  # Confirm data matches updated sheep

    # Step 3: Verify the update in the database
    get_response = client.get(f"/sheep/{updated_sheep['id']}")
    assert get_response.status_code == 200  # Ensure the sheep still exists
    assert get_response.json() == updated_sheep  # Confirm the data is updated

def test_get_all_sheep():
    # Step 1: Retrieve all sheep
    response = client.get("/sheep")

    # Step 2: Verify the status code and response content
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the response is a list
    assert len(response.json()) >= 1  # Check that there is at least one sheep in the response
