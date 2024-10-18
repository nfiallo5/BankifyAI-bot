# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionShowProductInfo(Action):
    def name(self) -> str:
        return "action_show_product_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product = tracker.get_slot('product')
        product_number = tracker.get_slot('product_number')

        product_index = {"2": "Cuenta de Ahorros", "3": "Cuenta Corriente", "4": "Tarjeta de Crédito", "5": "Inversiones"}

        if product_number:
            product =product_index.get(product_number, product)
        
        product_info = {
            "Cuenta de Ahorros": "Abre tu Cuenta de Ahorros en 5 minutos y obtén 90 días sin comisión en pagos de Servicios Online.",
            "Cuenta Corriente": "Administra tus recursos con una Cuenta Corriente con chequera y tarjeta de débito. Accede a sobregiros.",
            "Tarjeta de Crédito": "Tarjeta de crédito con beneficios exclusivos y acumulación de millas por cada consumo.",
            "Inversiones": "Inversión rentable desde el primer día. Obtén asesoría exclusiva y maximiza tu dinero."
        }

        info = product_info.get(product, "Lo siento, no tengo información sobre ese producto.")
        dispatcher.utter_message(text=f"Aquí tienes información sobre {product}: {info}")
        
        return [SlotSet("product", product), SlotSet("product_number", product_number)]
    

class ActionInvestCalculator(Action):
    def name(self) -> str:
        return "action_invest_calculator"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #Obtener la entrada del usuario
        amount = tracker.get_slot('invest_amount')
        time_days = tracker.get_slot('invest_time')

        #Validar
        if amount < 1000:
            dispatcher.utter_message(text="El monto minimo a invertir es de $1000")
            return []

        if time_days < 60:
            dispatcher.utter_message(text="Dias minimo son 60 ")
            return []

        tasa = 0.74 #%7.4

        total_return = int(amount * (1 + tasa) ** (time_days/365))

        dispatcher.utter_message(text=f"Invirtiendo ${amount} en un plazo de {time_days} dias, obtendrias un aproximado de ${total_return} \n*Valores Referenciales")

        return [SlotSet("invest_amount", amount), SlotSet("invest_time", time_days)]

