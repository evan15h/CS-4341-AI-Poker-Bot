from pypokerengine.players import BasePokerPlayer
from pypokerengine.engine.hand_evaluator import HandEvaluator
from pypokerengine.utils.card_utils import Card
from Emotion import Emotion
import random


class CustomAI(BasePokerPlayer):
   # Hear me out, we test with 1 emotion driven AI bot vs 3 regular and see how its win percentage compares. Human component is necessary for the app deliverable but isn't the focus. We need test results


    def __init__(self, name):
        super().__init__()  # Initialize BasePokerPlayer attributes
        self.emotion = Emotion()
        self.name = name  


    def declare_action(self, valid_actions, hole_card, game_state):

        # valid_actions => [raise_action_info, call_action_info, fold_action_info]
        raise_action_info = valid_actions[0]
        call_action_info = valid_actions[1]
        fold_action_info = valid_actions[2]

        call_action = next((action for action in valid_actions if action['action'] == 'call'), None)
        raise_action = next((action for action in valid_actions if action['action'] == 'raise'), None)


        pot_size = game_state['pot']['main']['amount']  # Get the current pot size


        # Calculate pot odds
        if call_action_info['amount'] > 0:
            pot_odds = self.calculate_pot_odds(pot_size, call_action_info['amount'])
        else:
            pot_odds = 0

        # Convert hole_card and community_card into Card objects
        # hole_cards = [Card.from_str(card) for card in hole_card]
        # community_cards = [Card.from_str(card) for card in game_state['community_card']]

        hand_strength = self.evaluate_hand(hole_card, game_state['community_card'])


        if hand_strength == "strong":
            if raise_action:
                # Bet sizing: raise a percentage of the pot for strong hands
                raise_amount = int(0.75 * pot_size)  # 75% of the pot size
                # Example line below for how to incorporate the emotion
                return self.emotion.adjust_decision("raise", min(raise_amount, raise_action['amount']['max']))
            if call_action:
                return self.emotion.adjust_decision("call", call_action_info['amount'])
        elif hand_strength == "medium":
            if pot_odds >= 0.5:
                if raise_action:
                    # Raise with a smaller amount for medium hands
                    raise_amount = int(0.5 * pot_size)  # 50% of the pot size
                    return self.emotion.adjust_decision("raise", min(raise_amount, raise_action['amount']['min']))
                if call_action:
                    return self.emotion.adjust_decision("call", call_action_info['amount'])
            else:
                return self.emotion.adjust_decision("fold", 0)
        elif hand_strength == "weak":
            if pot_odds >= 1.0:
                if call_action:
                    return self.emotion.adjust_decision("call", call_action_info['amount'])
            else:
                return self.emotion.adjust_decision("fold", 0)
            
        # Ensure a default action (safe fallback)
        return self.emotion.adjust_decision("fold", 0)


    def evaluate_hand(self, hole_card, community_cards):
        """
        Basic hand evaluation logic.
        Strong: high pairs, flush draws, straight draws, or made hands.
        Medium: lower pairs or some drawing hands.
        Weak: no pair, disconnected low cards.
        """
        values = [card[1] for card in hole_card + community_cards]


        # Basic pair evaluation logic (strong for now)
        if len(set(values)) < len(values):  # A simple pair logic
            return "strong"
        # You can improve this by adding flush or straight checks


        if random.random() > 0.5:  # Placeholder: make it medium sometimes
            return "medium"
        
        return "weak"

    def calculate_pot_odds(self, pot_size, call_amount):
        """
        Calculate the pot odds for making a call.
        Pot odds = (Current Pot Size / Cost to Call)
        """
        return pot_size / call_amount if call_amount > 0 else 0


    def receive_game_start_message(self, game_info):
        pass


    def receive_round_start_message(self, round_count, hole_card, seats):
        pass


    def receive_street_start_message(self, street, game_state):
        pass


    def receive_game_update_message(self, action, game_state):
        pass


    def receive_round_result_message(self, winners, hand_info, game_state):
        result = "win" if self.uuid in [winner["uuid"] for winner in winners] else "loss"
        self.emotion.update_emotion(result)