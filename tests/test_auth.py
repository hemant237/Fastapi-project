from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)

def test_register_user():
    response=client.post("/auth/register",
                         json={"email":"testuser@gmail.com",
                               "password":"password123"} )
    
    assert response.status_code==201

    data=response.json()
    assert data ["email"] == "testuser@gmail.com"


def test_register_duplicate_user():
    response=client.post(
        "/auth/register",
        json = {
            "email" : "duplicate@gmail.com",
            "password": "password123"
        }
    )

    assert response.status_code==201    


    response=client.post(
            "/auth/register",
            json = {
                "email" : "duplicate@gmail.com",
                "password": "password123"
            }
    )
    
    assert response.status_code==409


def test_login(test_user):
    response =client.post(
        "/auth/login",
        json = {
            "email" : "loginuser@gmail.com",
            "password" : "password123"
        }
    )

    assert response.status_code == 200

    data =response.json()

    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"]=="bearer"


def test_login_wrong_password(test_user):
    response = client.post("/auth/login",
                           json = {
                               "email": "loginuser@gmail.com",
                               "password":"wrongpassword"
                           })    
    assert response.status_code==401

    data = response.json()

    assert data["detail"]=='Invalid Email or Password'


def test_login_non_existent_user():
    response =client.post(
        "/auth/login",
        json = {
            "email" : "doesnotexist@gmail.com",
            "password" : "password123"
        }
    )    
    assert response.status_code==401

    data = response.json()
    assert data["detail"]=="Invalid Email or Password"

def test_get_me(test_user):
    login_response=client.post(
        "/auth/login",
         json ={
            "email" : "loginuser@gmail.com",
            "password" : "password123"
}    
    )

    assert login_response.status_code==200

    tokens = login_response.json()

    access_token = tokens["access_token"]

    response = client.get(
        "/auth/me",
        headers = {
            "Authorization" : f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"]    == test_user.id
    assert data["email"] == test_user.email


def test_get_me_without_token():
    response =client.get("/auth/me")

    assert response.status_code == 401    

def test_get_me_with_invalid_token():
    response = client.get("/auth/me",
                          headers= {
                              "Authorization" : "Bearer my-invalid-access-token-uwbkcnugwygobmkkgb8yubhmicmbhyc5hyuucbhubm5uhymbv5hymuonivunhvkevbn6hvukb6hube"
                          })    

    assert response.status_code==401

    data = response.json()

    assert data["detail"] == "Invalid token"


def test_refresh_token(test_user):
    login_response=client.post(
        "/auth/login",
        json = {
            "email" : "loginuser@gmail.com",
            "password" : "password123"
        }
    )

    assert login_response.status_code == 200

    tokens=login_response.json()

    old_refresh_token=tokens["refresh_token"]

    response = client.post(
        "/auth/refresh",
        json = {"refresh_token":old_refresh_token}
    )

    assert response.status_code==200

    new_tokens=response.json()

    assert "access_token" in new_tokens
    assert "refresh_token" in new_tokens

    assert new_tokens["token_type"]=="bearer"

    assert new_tokens["refresh_token"] != old_refresh_token


def test_old_refresh_token_cannot_be_reused(test_user):
    login_response = client.post(
        "/auth/login",
        json = {"email" : "loginuser@gmail.com",
                "password" : "password123"}
    )    

    assert login_response.status_code == 200

    tokens=login_response.json()

    old_refresh_token = tokens["refresh_token"]

    response= client.post(
        "/auth/refresh",
        json = {
            "refresh_token" : old_refresh_token
        }
    )

    assert response.status_code == 200

    second_response = client.post(
        "/auth/refresh",
        json = {"refresh_token" : old_refresh_token}
    )

    assert second_response.status_code == 401


def test_logout(test_user):
    login_response=client.post(
        "/auth/login",
        json ={
            "email" : "loginuser@gmail.com",
            "password" : "password123"
                            }
    )
    assert login_response.status_code==200

    tokens = login_response.json()

    refresh_token=tokens["refresh_token"]

    response = client.post(
        "/auth/logout",
        json = {"refresh_token" : refresh_token}
    )
    assert response.status_code==200

    data = response.json()

    assert data["message"] == "Logged out Successfully"

    new_response=client.post(
        "/auth/refresh",
        json = {"refresh_token" : refresh_token}
    )

    assert new_response.status_code == 401


def test_admin_endpoint_forbiddesn():
    login_response = client.post(
        "/auth/login",
        json = {"email" : "loginuser@gmail.com",
                "password" : "password123"}
    )    

    assert login_response.status_code==200

    access_token = login_response.json()["access_token"]

    response = client.get(
        "/auth/admin_test",
        headers = {
            "Authorization" : f"Bearer {access_token}"
        }
    )

    assert response.status_code==403

    data = response.json()

    assert data["detail"] == "Admin Access Required"







