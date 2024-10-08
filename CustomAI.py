from pypokerengine.players import BasePokerPlayer
from Emotion import Emotion
import random
from poker.hand import Hand
import logging

logging.basicConfig(level=logging.INFO)

class CustomAI(BasePokerPlayer):

    def __init__(self, name):
        super().__init__()  # Initialize BasePokerPlayer attributes
        self.emotion = Emotion()
        self.name = name  

    def receive_game_start_message(self, game_info):
        # Set the AI's name based on the game_info
        for player in game_info['seats']:
            if player['uuid'] == self.uuid:
                self.name = player['name']
                break

    def declare_action(self, valid_actions, hole_card, game_state):
        call_action = next((action for action in valid_actions if action['action'] == 'call'), None)
        raise_action = next((action for action in valid_actions if action['action'] == 'raise'), None)

        # Get the current pot size and call amount
        pot_size = game_state['pot']['main']['amount']
        call_amount = call_action['amount'] if call_action else 0

        # Define current_bet based on call_amount
        current_bet = call_amount

        # Example of fixed raise (2x the call amount)
        fixed_raise = 2 * current_bet if current_bet > 0 else 10  # Default to a small raise if there's no call amount

        # Calculate pot odds
        if call_amount > 0:
            pot_odds = self.calculate_pot_odds(pot_size, call_amount)
        else:
            pot_odds = 0

        # Evaluate hand strength (this can be refined based on actual poker hand evaluation logic)
        hand_strength = self.evaluate_hand(hole_card, game_state['community_card'])
        logging.info(f"Hand Strength: {hand_strength}, Pot Odds: {pot_odds}")

        # If fear is too high, AI may fold even on strong hands
        if self.emotion.fear > 0.7:
            return "fold", 0

        # If confidence is high and hand strength is strong, AI may become more aggressive
        if self.emotion.confidence > 1.5 and hand_strength == "strong":
            if raise_action:
                # Be aggressive, raise 100% of the pot size
                raise_amount = int(1.0 * pot_size)
                raise_amount = min(raise_amount, raise_action['amount']['max'])
                raise_amount = max(raise_amount, raise_action['amount']['min'])
                return "raise", raise_amount

        if hand_strength == "strong":
            if raise_action:
                # Bet sizing: raise 75% of the pot for strong hands
                raise_amount = int(0.75 * pot_size)
                raise_amount = min(raise_amount, raise_action['amount']['max'])
                raise_amount = max(raise_amount, raise_action['amount']['min'])
                return "raise", raise_amount
            return "call", call_amount if call_action else 0

        elif hand_strength == "medium":
            if pot_odds >= 0.5:
                if raise_action:
                    # Raise with 50% of the pot size for medium hands
                    raise_amount = int(0.5 * pot_size)
                    raise_amount = min(raise_amount, raise_action['amount']['max'])
                    raise_amount = max(raise_amount, raise_action['amount']['min'])
                    return "raise", raise_amount
                return "call", call_amount if call_action else 0
            else:
                # Default to a fixed raise
                if raise_action:
                    raise_amount = fixed_raise
                    raise_amount = min(raise_amount, raise_action['amount']['max'])
                    raise_amount = max(raise_amount, raise_action['amount']['min'])
                    return "raise", raise_amount
                return "call", call_amount if call_action else 0

        elif hand_strength == "weak":
            if pot_odds >= 1.0:
                return "call", call_amount if call_action else 0
            else:
                return "fold", 0

        return "call", call_amount if call_action else 0

    def evaluate_hand(self, hole_card, community_cards):
        """
        Basic hand evaluation logic using all cards (hole + community).
        Strong: high pairs, flush draws, straight draws, or made hands.
        Medium: lower pairs or some drawing hands.
        Weak: no pair, disconnected low cards.
        """
        # Combine hole cards and community cards
        full_hand = hole_card + community_cards

        # Only evaluate if there are at least 5 cards
        if len(full_hand) < 5:
            return "weak"  # Default to "weak" if there are fewer than 5 cards
        
        # Create a string representation for hand evaluation
        hand_str = " ".join([f"{card[1]}{card[0].upper()}" for card in full_hand])  # e.g., "S6 DJ" -> "6S JD"
        
        try:
            hand = Hand(hand_str)  # Evaluate the hand
            strength = hand.evaluate()
            # Adjust this logic based on your hand evaluation strategy
            if strength in ['PAIR', 'TWOPAIR', 'TRIPS', 'STRAIGHT', 'FLUSH', 'FULLHOUSE', 'QUADS', 'STRAIGHTFLUSH']:
                return "strong"
            elif strength in ['HIGHCARD']:
                return "medium"
            else:
                return "weak"
        except ValueError:
            return "weak"  # Default to weak if hand evaluation fails
    
    def calculate_pot_odds(self, pot_size, call_amount):
        """
        Calculate the pot odds for making a call.
        Pot odds = (Current Pot Size) / Cost to Call
        """
        return pot_size / call_amount if call_amount > 0 else 0

    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        print(f"Round {round_count} started. Hole cards: {hole_card}")
        print(f"Available seat names: {[seat['name'] for seat in seats]}")  # Print seat names for debugging

        # Try to find the AI's seat by matching against its name
        for index, seat in enumerate(seats):
            if seat['name'] == self.name:
                self.player_id = index
                break
        else:
            raise ValueError(f"AI player name '{self.name}' not found in seats. Available names: {[seat['name'] for seat in seats]}")

    def receive_street_start_message(self, street, game_state):
        pass

    def receive_game_update_message(self, action, game_state):
        pass

    def receive_round_result_message(self, winners, hand_info, game_state):
        print("\nRound Result:")
        for winner in winners:
            print(f"Winner: {winner['name']} with stack: {winner['stack']}")
        print(f"Hand Info: {hand_info}")
        print(f"Pot Size: {game_state['pot']['main']['amount']}")
        for player in game_state['seats']:
            print(f"Player {player['name']} has stack: {player['stack']}")