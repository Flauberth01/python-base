#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no 
ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Flauberth Brito"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": None,
}
for arg in sys.argv[1:]:
    # TODO: 
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
    print(key, value)

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde",
}
    
print(msg[current_language])
 