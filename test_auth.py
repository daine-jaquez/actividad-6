import pytest
import random

# Simulamos una base de datos de usuarios
users_db = {
    "user1": {"phone": "1234567890", "otp": None},
    "user2": {"phone": "0987654321", "otp": None}
}

# Función para generar OTP
def generate_otp(user_id):
    if user_id in users_db:
        otp = str(random.randint(100000, 999999))  # OTP de 6 dígitos
        users_db[user_id]["otp"] = otp
        return otp
    return None

# Función para validar OTP
def validate_otp(user_id, otp):
    if user_id in users_db and users_db[user_id]["otp"] == otp:
        return True
    return False

# Pruebas con pytest

def test_generate_otp():
    user_id = "user1"
    otp = generate_otp(user_id)
    assert otp is not None, "El OTP no debe ser None"
    assert len(otp) == 6, "El OTP debe tener 6 dígitos"
    assert otp.isdigit(), "El OTP debe ser numérico"

def test_validate_correct_otp():
    user_id = "user1"
    otp = generate_otp(user_id)
    assert validate_otp(user_id, otp) is True, "El OTP debería ser válido"

def test_validate_incorrect_otp():
    user_id = "user1"
    generate_otp(user_id)
    assert validate_otp(user_id, "000000") is False, "El OTP incorrecto no debería ser válido"

def test_validate_expired_otp():
    user_id = "user1"
    otp = generate_otp(user_id)
    users_db[user_id]["otp"] = None  # Simula que el OTP ha expirado
    assert validate_otp(user_id, otp) is False, "El OTP expirado no debería ser válido"
