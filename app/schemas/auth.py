from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class UserResponse(BaseModel):
    id: int
    email: EmailStr

class LoginRequest(BaseModel):
    email : EmailStr
    password : str    

class RefreshTokenRequest(BaseModel):
    refresh_token : str    

class TokenResponse(BaseModel):
    access_token: str
    refresh_token : str
    token_type: str    

class AccessTokenResponse(BaseModel):
    access_token : str
    token_type : str

class ForgotPasswordRequest(BaseModel):
    email : EmailStr


    
