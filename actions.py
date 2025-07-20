from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionCheckRepeatIntent(Action):
    def name(self) -> Text:
        return "action_check_repeat_intent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        last_intent = tracker.latest_message['intent'].get('name')
        asked_intents = tracker.get_slot("asked_intents") or []

        if last_intent in asked_intents:
            dispatcher.utter_message(response="utter_already_answered")
        else:
            asked_intents.append(last_intent)
            return [SlotSet("asked_intents", asked_intents)]

        return [SlotSet("asked_intents", asked_intents)]