# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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

    def run(self, dispatcher, tracker, domain):
        product = tracker.get_slot('product')
        
        product_info = {
            "Cuenta de Ahorros": "Abre tu Cuenta de Ahorros en 5 minutos y obtén 90 días sin comisión en pagos de Servicios Online.",
            "Cuenta Corriente": "Administra tus recursos con una Cuenta Corriente con chequera y tarjeta de débito. Accede a sobregiros.",
            "Tarjeta de Crédito": "Tarjeta de crédito con beneficios exclusivos y acumulación de millas por cada consumo.",
            "Inversiones": "Inversión rentable desde el primer día. Obtén asesoría exclusiva y maximiza tu dinero."
        }

        info = product_info.get(product, "Lo siento, no tengo información sobre ese producto.")
        dispatcher.utter_message(text=f"Aquí tienes información sobre {product}: {info}")
        
        return [SlotSet("product", product)]
