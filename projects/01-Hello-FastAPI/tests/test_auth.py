from fastapi.testclient import TestClient
from app.main import app

from app.core.security import create_password_reset_token , hash_password
from app.models.password_reset_token import PasswordResetToken
from datetime import datetime , timezone , timedelta
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



def test_admin_endpoint_success(admin_user):
    login_response=client.post(
        "/auth/login",
        json = {
            "email" : "admin@gmail.com",
            "password" : "password123"
        }
    )    

    assert login_response.status_code==200

    access_token = login_response.json()["access_token"]

    response= client.get(
        "/auth/admin_test",
        headers = {
            "Authorization" : f"Bearer {access_token}"
        }
    )

    assert response.status_code==200

    data = response.json()

    assert data["user"] == "admin@gmail.com"
    assert data["role"] == "admin"


def test_admin_endpoint_without_token():
    response=client.get("/auth/admin_test")

    assert response.status_code == 401


def test_forgot_password(test_user):
    response = client.post(
        "/auth/forgot-password",
        json = {"email" : "loginuser@gmail.com"
        }
    )    

    assert response.status_code == 200

    data = response.json()
    assert "message" in data

def test_forgot_password_nonexistent_user():
    response = client.post (
        "/auth/forgot-password",
        json = {"email" : "doesnotexist@gmail.com"}
    )    

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "User Not Found"


def test_reset_password(test_user,db):
    reset_token = create_password_reset_token()

    reset_token_record=PasswordResetToken(
        user_id = test_user.id,
        token_hash =hash_password(reset_token),
        expires_at = datetime.now(timezone.utc) + timedelta(minutes=15),
        used=False,
        created_at= datetime.now(timezone.utc)
    )

    db.add(reset_token_record)
    db.commit()

    response = client.post(
        "/auth/reset-password",
        json = {"token" : reset_token,
                   "new_password" : "password132"}
    )

    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "Password Reset Successfully"


def test_reset_password_changes_login_password(test_user,db):
    reset_token = create_password_reset_token()

    reset_token_record=PasswordResetToken(
        user_id = test_user.id,
        token_hash=hash_password(reset_token),
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=15),
        used=False,
        created_at=datetime.now(timezone.utc)
    )

    db.add(reset_token_record)
    db.commit()

    response= client.post(
        "/auth/reset-password",
        json = {"token" : reset_token,
                "new_password": "newpassword"}
    )

    assert response.status_code == 200

    old_password_login = client.post(
        "/auth/login",
        json ={"email" : "loginuser@gmail.com",
               "password" : "password123"}
    )

    assert old_password_login.status_code == 401

    new_pass_login = client.post(
        "/auth/login",
        json = {"email" : "loginuser@gmail.com",
                "password": "newpassword"}
    )

    assert new_pass_login.status_code == 200

    data = new_pass_login.json()

    assert "access_token" in data
    assert "refresh_token" in data


def test_reset_password_token_reuse(test_user,db):
    reset_token = create_password_reset_token()

    reset_token_record=PasswordResetToken(
        user_id=test_user.id,
        token_hash=hash_password(reset_token),
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=15),
        used = False,
        created_at= datetime.now(timezone.utc)
    )    

    db.add(reset_token_record)
    db.commit()

    first_response=client.post(
        "/auth/reset-password",
        json= {"token" : reset_token,
               "new_password": "passwordnew123"}
    )

    assert first_response.status_code==200

    sec_response= client.post(
        "/auth/reset-password",
        json = {"token" : reset_token,
                "new_password" : "passwordnew"}
    )

    assert sec_response.status_code==401

    data= sec_response.json()
    assert data["detail"] == "Reset token has already been used"


def test_reset_password_expired_token(test_user,db):
    reset_token=create_password_reset_token()

    reset_token_record=PasswordResetToken(
        user_id = test_user.id,
        token_hash=hash_password(reset_token),
        expires_at= datetime.now(timezone.utc) - timedelta(minutes=1),
        used=False,
        created_at=datetime.now(timezone.utc)
    )    

    db.add(reset_token_record)
    db.commit()

    response=client.post(
        "/auth/reset-password",
        json = {"token" : reset_token,
                "new_password": "password1234"}
    )

    assert response.status_code == 401

    data = response.json()
    assert data["detail"] == "Reset token has expired"


def test_reset_password_invalid_token():
    response= client.post(
        "/auth/reset-password",
        json ={"token" : "invalid-token_for_test",
               "new_password": "password12345"}
    )

    assert response.status_code == 401

    data = response.json()
    assert data["detail"] == "Invalid password reset token"


def test_reset_password_marks_token_as_used(test_user, db):
    reset_token = create_password_reset_token()

    reset_token_record = PasswordResetToken(
        user_id=test_user.id,
        token_hash=hash_password(reset_token),
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=15),
        used=False,
        created_at=datetime.now(timezone.utc)
    )

    db.add(reset_token_record)
    db.commit()

    response = client.post(
        "/auth/reset-password",
        json={
            "token": reset_token,
            "new_password": "newpassword123"
        }
    )

    assert response.status_code == 200

    # Refresh the database object
    db.refresh(reset_token_record)

    assert reset_token_record.used is True    










