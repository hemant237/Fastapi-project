from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_student(db):
    response = client.post(
        "/students",
        json={
            "name": "Rahul",
            "age": 21
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Rahul"
    assert data["age"] == 21


def test_get_students(db):
    # Create students through the API
    client.post(
        "/students",
        json={
            "name": "Rahul",
            "age": 21
        }
    )

    client.post(
        "/students",
        json={
            "name": "Amit",
            "age": 25
        }
    )

    # Get all students
    response = client.get("/students")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2

    assert data[0]["name"] == "Rahul"
    assert data[0]["age"] == 21

    assert data[1]["name"] == "Amit"
    assert data[1]["age"] == 25    


def test_get_student(db):
    create_response = client.post(
        "/students",
        json={
            "name": "Rahul",
            "age": 21
        }
    )

    assert create_response.status_code == 201

    student_id = create_response.json()["id"]

    response = client.get(f"/students/{student_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == student_id
    assert data["name"] == "Rahul"
    assert data["age"] == 21    


def test_get_student_not_found(db):
    response = client.get("/students/999999")

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "Student Not Found"    


def test_update_student(db):
    create_response = client.post(
        "/students",
        json={
            "name": "Rahul",
            "age": 21
        }
    )

    assert create_response.status_code == 201

    student_id = create_response.json()["id"]

    update_response = client.put(
        f"/students/{student_id}",
        json={
            "name": "Rahul Sharma",
            "age": 22
        }
    )

    assert update_response.status_code == 200

    data = update_response.json()

    assert data["id"] == student_id
    assert data["name"] == "Rahul Sharma"
    assert data["age"] == 22    


def test_update_student_partial(db):
    create_response = client.post(
        "/students",
        json={
            "name": "Rahul",
            "age": 21
        }
    )

    assert create_response.status_code == 201

    student_id = create_response.json()["id"]

    response = client.patch(
        f"/students/{student_id}",
        json={
            "age": 22
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == student_id
    assert data["name"] == "Rahul"
    assert data["age"] == 22    


def test_update_student_partial_not_found(db):
    response = client.patch(
        "/students/999999",
        json={
            "age": 22
        }
    )

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "Student Not Found"   


def test_delete_student(db):
    create_response = client.post(
        "/students",
        json={
            "name": "Rahul",
            "age": 21
        }
    )

    assert create_response.status_code == 201

    student_id = create_response.json()["id"]

    delete_response = client.delete(
        f"/students/{student_id}"
    )

    assert delete_response.status_code == 200

    data = delete_response.json()

    assert data["message"] == "Student Deleted Successfully"

    # Verify the student is actually deleted
    get_response = client.get(
        f"/students/{student_id}"
    )

    assert get_response.status_code == 404

    data = get_response.json()

    assert data["detail"] == "Student Not Found"     


def test_delete_student_not_found(db):
    response = client.delete("/students/999999")

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "Student Not Found"    

def test_create_student_missing_age(db):
    response = client.post(
        "/students",
        json={
            "name": "Rahul"
        }
    )

    assert response.status_code == 422

    data = response.json()

    assert "detail" in data    

def test_create_student_missing_name(db):
    response = client.post(
        "/students",
        json={
            "age": 21
        }
    )

    assert response.status_code == 422

    data = response.json()

    assert "detail" in data    


def test_create_student_invalid_age_type(db):
    response = client.post(
        "/students",
        json={
            "name": "Rahul",
            "age": "twenty"
        }
    )

    assert response.status_code == 422

    data = response.json()

    assert "detail" in data    


def test_create_student_invalid_name_type(db):
    response = client.post(
        "/students",
        json={
            "name": 12345,
            "age": 21
        }
    )

    assert response.status_code == 422

    data = response.json()

    assert "detail" in data

def test_update_student_partial_invalid_age_type(db):
    create_response = client.post(
        "/students",
        json={
            "name": "Rahul",
            "age": 21
        }
    )

    assert create_response.status_code == 201

    student_id = create_response.json()["id"]

    response = client.patch(
        f"/students/{student_id}",
        json={
            "age": "twenty"
        }
    )

    assert response.status_code == 422

    data = response.json()

    assert "detail" in data    


def test_update_student_partial_invalid_name_type(db):
    create_response = client.post(
        "/students",
        json={
            "name": "Rahul",
            "age": 21
        }
    )

    assert create_response.status_code == 201

    student_id = create_response.json()["id"]

    response = client.patch(
        f"/students/{student_id}",
        json={
            "name": 12345
        }
    )

    assert response.status_code == 422

    data = response.json()

    assert "detail" in data    

def test_update_student_partial_empty_body(db):
    create_response = client.post(
        "/students",
        json={
            "name": "Rahul",
            "age": 21
        }
    )

    assert create_response.status_code == 201

    student_id = create_response.json()["id"]

    response = client.patch(
        f"/students/{student_id}",
        json={}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == student_id
    assert data["name"] == "Rahul"
    assert data["age"] == 21    