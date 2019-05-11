from pip._vendor.distlib.compat import raw_input
import requests, json


def Traduccion(source, target, text):
    parametros = {'sl': source, 'tl': target, 'q': text}
    cabeceras = {"Charset": "UTF-8",
                 "User-Agent": "AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"}
    url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
    response = requests.post(url, data=parametros, headers=cabeceras)
    if response.status_code == 200:
        for x in response.json()['sentences']:
            return x['trans'], response.json()['ld_result']['srclangs'][0]
    else:
        return


def traductor(texto):
    try:
        if len(texto) <= 125 and texto != "":
            resultText, language_id = Traduccion('es', 'ru', texto)
            if language_id == 'es':
                return resultText
            else:
                return "El texto debe ser en español"
        else:
            return "El texto debe tener minimo una palabra y maximo 125 caracteres en total"
    except:
        return "Comprueba tu conexion a internet"


def getDataStorage():
    with open('datastorage.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


def casosTesting():
    """Obtenemos los casos de pruebas desde el datastorage"""
    data = getDataStorage()
    for caso in data['casos']:
        print('------------------' + caso['name'] + '---------------------')
        result = traductor(caso['input'])
        if result == caso['output']:
            print("Paso la prueba\n")
        else:
            print("No paso la prueba\n")


def menuPrincipal():
    print('------------------MENU PRINCIPAL---------------------')
    print("1. Ejecutar pruebas")
    print("2. Probar aplicacion")
    print("3. Salir")
    option = raw_input("Ingresa la opcion que deseas : ")
    if option == "1":
        casosTesting()
        menuPrincipal()
    elif option == "2":
        text = raw_input("Ingresa el texto que deseas ingresar : ")
        print(traductor(text))
        print()
        menuPrincipal()
    elif option == "3":
        print("salir")
    else:
        print("esa opcion no existe\n")
        menuPrincipal()


menuPrincipal()
