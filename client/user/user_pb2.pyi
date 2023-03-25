from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetDetailsRequest(_message.Message):
    __slots__ = ["email"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class GetDetailsResponse(_message.Message):
    __slots__ = ["email", "firstname", "lastname"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    firstname: str
    lastname: str
    def __init__(self, email: _Optional[str] = ..., firstname: _Optional[str] = ..., lastname: _Optional[str] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ["email", "password"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ["authenticate_token"]
    AUTHENTICATE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authenticate_token: str
    def __init__(self, authenticate_token: _Optional[str] = ...) -> None: ...

class RegisterRequest(_message.Message):
    __slots__ = ["email", "firstname", "lastname", "password"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    firstname: str
    lastname: str
    password: str
    def __init__(self, email: _Optional[str] = ..., firstname: _Optional[str] = ..., lastname: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ["email"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...
