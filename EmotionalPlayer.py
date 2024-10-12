from pypokerengine.players import BasePokerPlayer
import random

# Parent class BasePokerPlayer
class EmotionalPlayer(BasePokerPlayer):

    def __init__(self, name):
        # Emotion score between 1 and 200
        self.emotion_score = 100
        self.name = name

    # Contains the logic for determining an action 
    def declare_action(self, valid_actions, hole_card, round_state):

        # valid_actions format => [fold_action_info, call_action_info, raise_action_info]
        raise_amount = 0
        percent = 0
        call_action_info = valid_actions[1]
        raise_action_info = valid_actions[2]

        # Get the current pot size and display
        pot_size = round_state['pot']['main']['amount']
        print(f'Pot size: {pot_size}')

        # Calculate pot odds based on current bet
        if call_action_info['amount'] > 0:
            pot_odds = self.calculate_pot_odds(pot_size, call_action_info['amount'])
        else:
            pot_odds = 0

        # Generate base hand strength score
        score = 0

        # Base on high card in hole cards
        for card in hole_card:
            if "A" in card:
                score = 90
            elif "K" in card:
                score = 85
            elif "Q" in card:
                score = 80
            elif "J" in card:
                score = 75
            elif "10" in card:
                score = 70
            elif "9" in card:
                score = 65
            elif "8" in card:
                score = 60
            elif "7" in card:
                score = 50
            elif "6" in card:
                score = 40
            elif "5" in card:
                score = 30
            elif "4" in card:
                score = 20
            elif "3" in card:
                score = 10

            # Pocket 2s
            else:
                score = 95

        # Check if there is atleast a pair and increase the score
        for com in round_state['community_card']:
            for hol in hole_card:
                if hol[1] in com[1]:
                    score +=100
        
        # Add some variance to incorporate bluffing and missing chances
        random_influence = random.uniform(0.4, 1.0)
        score = score * random_influence

        # Incorporate the emotional influence
        score = score * self.emotion_score / 100

        # Based on the generated score make an action and adjust the emotion based on the action
        if score < 30:
            if call_action_info['amount'] == 0:
                # Check
                self.adjust_emotion(0)
                return "call", 0
            else:
                # Fold
                self.adjust_emotion(-5)
                return "fold", 0
        elif score < 60:
            # Call
            self.adjust_emotion(1)
            return "call", call_action_info['amount']
        else:
            # Raise
            self.adjust_emotion(8)
            if pot_odds >= 2:
                percent = 0.75
                raise_amount = self.calculate_raise_amount(pot_size, percent, raise_action_info, round_state)   
                return "raise", raise_amount
            
            elif pot_odds >= 0.75:
                percent = 0.5
                raise_amount = self.calculate_raise_amount(pot_size, percent, raise_action_info, round_state)   
                return "raise", raise_amount
            
            else:
                percent = 0.25
                raise_amount = self.calculate_raise_amount(pot_size, percent, raise_action_info, round_state)   
                return "raise", raise_amount

    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass

    # Update emotion score based on winning or losing the hand
    def receive_round_result_message(self, winners, hand_info, round_state):
        result = "win" if self.uuid in [winner["uuid"] for winner in winners] else "loss"
        if result == "win":
            self.adjust_emotion(12)
        else:
            self.adjust_emotion(-5)
    
    # Helper function used to adjust emotion within a valid range
    def adjust_emotion(self, amount):
        if amount > 0:
            if self.emotion_score + amount > 200:
                self.emotion_score = 200
            else:
                self.emotion_score += amount
        else:
            if self.emotion_score + amount < 1:
                self.emotion_score = 1
            else:
                self.emotion_score += amount

    #Calculate the pot odds for making a call based on the pot size and current bet
    def calculate_pot_odds(self, pot_size, call_amount):
        return pot_size / call_amount if call_amount > 0 else 0
    
    # Determine the amount to raise by
    def calculate_raise_amount(self, pot_size, percent, raise_action_info, round_state):
        min_raise = raise_action_info["amount"]["min"]
        max_raise = raise_action_info["amount"]["max"]
        
        raise_amount = int(percent*pot_size)
        for player in round_state['seats']:
            if player['name'] == self.name:
                stack = player['stack']
                if raise_amount <= max_raise and raise_amount >= min_raise:
                    return raise_amount
                else:
                    return max(min_raise, min(raise_amount, max_raise))
