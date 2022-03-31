import ssl
import requests

from requests.adapters import HTTPAdapter
from urllib3 import PoolManager
from urllib3.util import ssl_

CIPHERS = (
    'TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-ECDSA-AES256-GCM-SHA384' 
    ':ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20' 
    '-POLY1305:DHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:DHE-RSA' 
    '-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES256-SHA256:ECDHE-ECDSA' 
    '-AES128-SHA256:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA' 
    ':DHE-RSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:DHE-RSA-AES128-SHA:RSA-PSK-AES256-GCM' 
    '-SHA384:DHE-PSK-AES256-GCM-SHA384:RSA-PSK-CHACHA20-POLY1305:DHE-PSK-CHACHA20-POLY1305:ECDHE-PSK-CHACHA20' 
    '-POLY1305:AES256-GCM-SHA384:PSK-AES256-GCM-SHA384:PSK-CHACHA20-POLY1305:RSA-PSK-AES128-GCM-SHA256:DHE-PSK' 
    '-AES128-GCM-SHA256:AES128-GCM-SHA256:PSK-AES128-GCM-SHA256:AES256-SHA256:AES128-SHA256:ECDHE-PSK-AES256' 
    '-CBC-SHA384:ECDHE-PSK-AES256-CBC-SHA:SRP-RSA-AES-256-CBC-SHA:SRP-AES-256-CBC-SHA:RSA-PSK-AES256-CBC-SHA384' 
    ':DHE-PSK-AES256-CBC-SHA384:RSA-PSK-AES256-CBC-SHA:DHE-PSK-AES256-CBC-SHA:AES256-SHA:PSK-AES256-CBC-SHA384' 
    ':PSK-AES256-CBC-SHA:ECDHE-PSK-AES128-CBC-SHA256:ECDHE-PSK-AES128-CBC-SHA:SRP-RSA-AES-128-CBC-SHA:SRP-AES' 
    '-128-CBC-SHA:RSA-PSK-AES128-CBC-SHA256:DHE-PSK-AES128-CBC-SHA256:RSA-PSK-AES128-CBC-SHA:DHE-PSK-AES128-CBC' 
    '-SHA:AES128-SHA:PSK-AES128-CBC-SHA256:PSK-AES128-CBC-SHA'
)


class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args,
                                       ssl_context=ctx,
                                       **pool_kwargs)


body = {
  "responseId": "0d1863ee-fcfd-4040-bf2d-ef8e2986cf63-94f60986",
  "queryResult": {
    "queryText": "ciao ramo 1",
    "parameters": {},
    "allRequiredParamsPresent": "true",
    "fulfillmentMessages": [
      {
        "text": {
          "text": [
            ""
          ]
        }
      },
      {
        "payload": {
          "welcome_data": {
            "gsw_gia_t_ivr": "20",
            "gia_call_id": "TestAutolettura_800_ramo1",
            "gsw_mode": "DAY",
            "gsw_exit_code": "701#2008600",
            "gsw_codice_conto_cliente": "505353490277",
            "gsw_codice_esito": "2008600",
            "gsw_ani": "3334761728",
            "gsw_nome": "PASQUALE",
            "gsw_descrizione_esito": "",
            "gsw_ivr_name": "IVRGNS1T",
            "gia_origin": "700",
            "gsw_ingresso": "RETAIL",
            "gsw_conn_id": "1234_1",
            "gsw_marginalita": "",
            "gsw_codice_cliente": "8111183301",
            "gsw_pa": "123",
            "gsw_perimetro_middle": "349856380",
            "gsw_esito": "OK",
            "gsw_sito_ivr": "1T",
            "gsw_segmento_middle": "",
            "gsw_time_key": "20200708094030",
            "gsw_cognome_ragione_soc": "DE CARIA",
            "gsw_macrosegmento": "macroseg",
            "gsw_flag_middle": "N",
            "gsw_sito_gns": "1T",
            "gsw_dettagli": "field1:value1|field2:value2|field3:value3"
          }
        }
      }
    ],
    "outputContexts": [
      {
        "name": "projects/prova-va-eni-dwpfjf/agent/sessions/6895891c-5ed8-2e5b-22d0-87fb04d71eb3/contexts/__system_counters__",
        "parameters": {
          "no-input": 0,
          "no-match": 0
        }
      }
    ],
    "intent": {
      "name": "projects/prova-va-eni-dwpfjf/agent/intents/238aae3b-62e2-4504-9b4f-ca550ee31aa1",
      "displayName": "tmp_welcome_ramo_1"
    },
    "intentDetectionConfidence": 1,
    "languageCode": "it",
    "sentimentAnalysisResult": {
      "queryTextSentiment": {
        "score": 0.2,
        "magnitude": 0.2
      }
    }
  },
  "originalDetectIntentRequest": {
    "source": "DIALOGFLOW_CONSOLE",
    "payload": {}
  },
  "session": "projects/prova-va-eni-dwpfjf/agent/sessions/6895891c-5ed8-2e5b-22d0-87fb04d71eb3"
}


session = requests.session()
# adapter = TlsAdapter(ssl.PROTOCOL_TLSv1)
adapter = TlsAdapter(ssl.OP_NO_TLSv1_2 | ssl.OP_NO_TLSv1_3 | ssl.OP_NO_TLSv1_1)
session.mount("https://", adapter)

try:
    url = 'https://lettere-numeri-dot-gpjegld01-1812-convintel-ivr.ew.r.appspot.com/fulfillment'
    headers = {'Authorization': 'Basic ZGV2OjVrSk4tc3RVSTctazRZRzBmXzJ5Qkg3ZC1oNU9LMXM='}
    r = session.request('POST', url=url,json=body, headers=headers)
    print(r)
except Exception as exception:
    print(exception)