import sender_stand_request
import data


def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body ["name"]

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def test_crear_1_kit_con_nombre_de_1_letras():
    new_kit_body = get_kit_body("A")
    positive_assert(new_kit_body)

def test_crear_1_kit_con_nombre_de_511_letras():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(new_kit_body)

def test_crear_1_kit_con_nombre_de_0_letras():
    new_kit_body = get_kit_body("")
    negative_assert_code_400(new_kit_body)

def test_crear_1_kit_con_nombre_de_512_letras():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(new_kit_body)

def test_crear_1_kit_con_nombre_con_caracteres_especiales():
    new_kit_body = get_kit_body("№%@")
    positive_assert(new_kit_body)

def test_crear_1_kit_con_nombre_con_espacios():
    new_kit_body = get_kit_body("A Aaa ")
    positive_assert(new_kit_body)

def test_crear_1_kit_con_nombre_de_numero():
    new_kit_body = get_kit_body("123")
    positive_assert(new_kit_body)

def test_crear_1_kit_sin_nombre():
    new_kit_body = get_kit_body()
    negative_assert_code_400(new_kit_body)

def test_crear_1_kit_con_nombre_tipo_numero():
    new_kit_body = get_kit_body(123)
    negative_assert_code_400(new_kit_body)


