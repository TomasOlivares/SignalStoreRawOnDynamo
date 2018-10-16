from __future__ import print_function
import json
import decimal
import datetime
import uuid
from decimal import *

class class_Error():
    def __init__(self):
        print('mi constructor vacio')
    
    def formatea_error(self, error, senial):
        return {
            'Error': [{
                "date": str(datetime.datetime.now()),
                "error": error,
                "function": "bloviusSignalStoreRawOnDynamo",
                "id":  str(uuid.uuid4()),
                "service": "Lambda",
                "signal": str(senial)
            }]
        }