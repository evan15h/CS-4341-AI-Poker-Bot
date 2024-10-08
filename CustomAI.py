from pypokerengine.players import BasePokerPlayer
from Emotion import Emotion
import random

class CustomAI(BasePokerPlayer):

    def __init__(self):
        self.emotion = Emotion()

    def declare_action(self, valid_actions, hole_card, game_state):
        call_action = next((action for action in valid_actions if action['action'] == 'call'), None)
        raise_action = next((action for action in valid_actions if action['action'] == 'raise'), None)

        pot_size = game_state['pot']['main']['amount']  # Get the current pot size
        call_amount = call_action['amount'] if call_action else 0

        # Calculate pot odds
        if call_amount > 0:
            pot_odds = self.calculate_pot_odds(pot_size, call_amount)
        else:
            pot_odds = 0

        hand_strength = self.evaluate_hand(hole_card, game_state['community_card'])

        if hand_strength == "strong":
            if raise_action:
                # Bet sizing: raise a percentage of the pot for strong hands
                raise_amount = int(0.75 * pot_size)  # 75% of the pot size
                return "raise", min(raise_amount, raise_action['amount']['max'])
            return "call", call_amount if call_action else 0
        elif hand_strength == "medium":
            if pot_odds >= 0.5:
                if raise_action:
                    # Raise with a smaller amount for medium hands
                    raise_amount = int(0.5 * pot_size)  # 50% of the pot size
                    return "raise", min(raise_amount, raise_action['amount']['min'])
                return "call", call_amount if call_action else 0
            else:
                return "fold", 0
        elif hand_strength == "weak":
            if pot_odds >= 1.0:
                return "call", call_amount if call_action else 0
            else:
                return "fold", 0

        return "call", call_amount if call_action else 0


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
