#!/usr/bin/env python3

import os
import logging
from logging import handlers


# BOILERPLATE
# TODO: usar função
# TODO: usr lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instancia
log = logging.Logger("flauberth", log_level)
# level
# ch = logging.StreamHandler() # Console/terminal/stderr
# ch.setLevel(logging.DEBUG)
fh = handlers.RotatingFileHandler(
    "meulog.log",
    maxBytes=300, # 10**6 -> 1 MEGA
    backupCount=10,
) 
fh.setLevel(log_level)
# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
fh.setFormatter(fmt)
# destino
log.addHandler(fh)

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: banco de dados sumiu")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
