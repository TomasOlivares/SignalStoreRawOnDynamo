from __future__ import print_function
import json
import decimal
from decimal import *
from metodos.error import class_Error

class class_Validacion():
    def __init__(self):
        print('mi constructor vacio')


    def valida_data(self, element):
        objError = class_Error()
        #Valida señal
        try:
            id_ = element['id']
            if type(id_) != str:
                return objError.formatea_error('Se esperaba id como una cadena ' + str(id_), element)
        except:
            return formatea_error('Se esperaba id como id', element)
        
        try:
            reading = Decimal(str(element['reading']))#Revisar si quitar el str
            if type(reading) != Decimal:
                return formatea_error('Se esperaba reading como Decimal ' + str(reading), element)
        except:
            return formatea_error('Se esperaba reading como reading', element)
        
        try:
            property_ = element['property']
            if type(property_) != str:
                return formatea_error('Se esperaba property como una cadena ' + str(property_), element)
        except:
            return formatea_error('Se esperaba property como property', element)
        
        try:
            place = element['place']
            if type(place) != str:
                return formatea_error('Se esperaba place como una cadena ' + str(place), element)
        except:
            return formatea_error('Se esperaba place como place', element)
        
        try:
            date = element['date']
            if type(date) != str:
                return formatea_error('Se esperaba date como una cadena ' + str(date), element)
        except:
            return formatea_error('Se esperaba date como date', element)
        
        try:
            hourMinute = int(element['hourMinute'])
            if type(hourMinute) != int:
                return formatea_error('Se esperaba hourMinute como una entero ' + str(hourMinute), element)
        except:
            return formatea_error('Se esperaba hourMinute como hourMinute', element)
        
        return {
            'Exelente': [{
                'id': id_,
                'reading': reading,
                'property': property_,
                'place': place,
                'date': date,
                'hourMinute': hourMinute
            }]
        }