import sender_stand_request
import data

# esta función cambia los valores en el parámetro "name"
def get_kit_body (name_kit):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name_kit
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body

# Función para generar el "authToken"
def get_new_user_token():
    new_user = sender_stand_request.post_new_user(data.user_body.copy())
    auth_token = new_user.json()["authToken"]
    create_token_user = data.headers.copy()
    create_token_user["Authorization"] = f"Bearer {auth_token}"
    return create_token_user


#función para pruebas positivas
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


# función para pruebas negativas
def negative_assert (name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


# Prueba 1. Test para comprobar que el campo name permite 1 caracter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


# Prueba 2. Test para comprobar que el campo name  permitaa 511 caracteres
def test_create_kit_511_letter_in_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Prueba 3. Test para comprobar que el campo name no permite 0 caracteres
def test_create_kit_0_letter_in_get_negative_response():
    negative_assert("")


# Prueba 4. Test para  comprobar que el campo name no permite 512 caracteres
def test_create_kit_512_in_get_negative_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Prueba 5. Test para comprobar que el campo name permita caracteres especiales
def test_create_kit_special_letter_success_response():
    positive_assert("\"№%@\",")


# Prueba 6. Test para comprobar que el campo name permita espacios
def test_create_kit_space_success_response():
    positive_assert(" A Aaa ")


# Prueba 7. Test para comprobar que el campo name permita números
def test_create_kit_number_success_response():
    positive_assert("123")


# Prueba 8. Test para comprobar que la solicitud marca error si se envia sin el campo name
def test_create_kit_negative_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert(kit_body)
    


# Prueba 9. Test para comprobar que el campo name no permite un número en lugar de un string
def test_create_kit_not_string_negative_response():
    negative_assert(123)





