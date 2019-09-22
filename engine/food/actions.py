# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


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
#         dispatcher.utter_message("Hello World!")
#
#         return []
from rasa_sdk.forms import FormAction
from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class FoodForm(FormAction):

    def name(self):  # type: () -> Text
        return "food_form"

    @staticmethod
    def required_slots(tracker):  # type: (Tracker) -> List[Text]
        return ["favorite_cuisine", "favorite_food", "favorite_restaurant"]

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_submit', tracker)
        return []


class ActionCheckRestaurants(Action):
    def name(self):  # type: () -> Text
        return "action_check_restaurants"

    def run(
            self,
            dispatcher,  # type: CollectingDispatcher
            tracker,  # type: Tracker
            domain,  # type:  Dict[Text, Any]
    ):  # type: (...) -> List[Dict[Text, Any]]
        cuisine = tracker.get_slot('favorite_cuisine')
        print(cuisine)
        results = ['KFC', 'Gogi', 'Góc Hà Nội']
        dispatcher.utter_message("Blah Blah Blah")
        return [SlotSet("found_restaurants", results)]
