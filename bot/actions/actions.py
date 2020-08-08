from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class CheckNumberAction(Action):
    def name(self):
        return "action_check"


    def run(self, dispatcher, tracker, domain):
        num = tracker.get_slot("num_menu")
        num = int(num)
        if num == 1:
            dispatcher.utter_message(template="utter_who_we_are")
        elif num == 2:
            dispatcher.utter_message(template="utter_local")
        elif num == 3:
            dispatcher.utter_message(template="utter_services")
        elif num == 4:
            dispatcher.utter_message(template="utter_contact")
        elif num > 4 or num < 1:
            dispatcher.utter_message("Digite uma opção válida")