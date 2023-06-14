import requests
import pytest
from connection_db import collection_db

collection = collection_db()
headers = collection.find_one()["headers"]
invalid = collection.find_one()["invalid"]
userID = "21aee635-9231-4bf2-8b1b-1667ef932938"
invalidUserID = "21aee635-9231-4bf2-8b1b-1667ef93293"
##TEST_01
 
def test_usuario_valido():
    url = f"https://api.appcenter.ms/v0.1/user"

    response = requests.get(url, headers=headers)
    data = response.json()

    expected = collection.find_one()["prueba_1"]["expected"]
    assert data["email"] == expected

##TEST_02

def test_info_usuario_valido():
    url = f"https://api.appcenter.ms/v0.1/user"

    response = requests.get(url, headers=invalid)
    data = response.json()

    expected = collection.find_one()["prueba_2"]["expected"]
    assert data["code"] == expected

##TEST_03


def test_usuario_sin_token():
    url = f"https://api.appcenter.ms/v0.1/user"

    response = requests.get(url)
    data = response.json()

    expected = collection.find_one()["prueba_3"]["expected"]
    assert data["code"] == expected

##TEST_04


def test_create_registro_exitoso():
    url = f"https://api.appcenter.ms/v0.1/users/{userID}/devices/register"

    payload = collection.find_one()["prueba_4"]["payload"]
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    expected = collection.find_one()["prueba_4"]["expected"]
    assert data["model"] == expected

##TEST_05

def test_registro_sin_datos():
    url = f"https://api.appcenter.ms/v0.1/users/{userID}/devices/register"

    payload = collection.find_one()["prueba_5"]["payload"]
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    expected = collection.find_one()["prueba_5"]["expected"]
    assert data["message"] == expected

##TEST_06

def test_registro_sin_wrong_if_user():
    url = f"https://api.appcenter.ms/v0.1/users/{invalidUserID}/devices/register"

    payload = collection.find_one()["prueba_6"]["payload"]
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    expected = collection.find_one()["prueba_6"]["expected"]
    assert data["message"] == expected

##TEST_07

def test_lista_usuario_token_valido():
    url = f"https://api.appcenter.ms/v0.1/user/devices"

    response = requests.get(url,headers=headers)
    data = response.json()

    expected = collection.find_one()["prueba_7"]["expected"]
    assert data[0]["udid"] == expected

##TEST_08

def test_lista_token_invalido():
    url = f"https://api.appcenter.ms/v0.1/user/devices"

    response = requests.get(url,headers=invalid)
    data = response.json()

    expected = collection.find_one()["prueba_8"]["expected"]
    assert data["code"] == expected

#TEST_09
def test_lista_usuario_sin_token():
    url = f"https://api.appcenter.ms/v0.1/user/devices"

    response = requests.get(url)
    data = response.json()

    expected = collection.find_one()["prueba_9"]["expected"]
    assert data["statusCode"] == expected

##TEST_10
def test_info_especifica_usuario():
    url = f"https://api.appcenter.ms/v0.1/user/devices/2"

    response = requests.get(url,headers=headers)
    data = response.json()

    expected = collection.find_one()["prueba_10"]["expected"]
    assert data["model"] == expected

##TEST_11

def test_info_especifica_usuario_token_invalido():
    url = f"https://api.appcenter.ms/v0.1/user/devices/1"

    response = requests.get(url,headers=invalid)
    data = response.json()

    expected = collection.find_one()["prueba_11"]["expected"]
    assert data["code"] == expected

##TEST_12
def test_usuario_no_existente():
    url = f"https://api.appcenter.ms/v0.1/user/devices/1"

    response = requests.get(url,headers=headers)
    data = response.json()

    expected = collection.find_one()["prueba_12"]["expected"]
    assert data["code"] == expected
##TEST_13
def test_eliminar_dispositivo():
    url = f"https://api.appcenter.ms/v0.1/user/devices/1"
    response = requests.delete(url, headers=headers)
    data = response.json()
    expected = collection.find_one()["prueba_13"]["expected"]

    assert data == expected

##TEST_14
def test_eliminar_disp_token_invalido():
    url = f"https://api.appcenter.ms/v0.1/user/devices/1"
    response = requests.delete(url, headers=invalid)
    data = response.json()
    expected = collection.find_one()["prueba_14"]["expected"]
    assert data["code"] == expected

##TEST_15    
def test_elimina_disp_existente_usuario():
    url = f"https://api.appcenter.ms/v0.1/user/devices/1"

    response = requests.get(url,headers=headers)
    data = response.json()

    expected = collection.find_one()["prueba_12"]["expected"]
    assert data["code"] == expected