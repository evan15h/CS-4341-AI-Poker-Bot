from pypokerengine.players import BasePokerPlayer
import random

class EmotionalPlayer(BasePokerPlayer):  # Do not forget to make parent class as "BasePokerPlayer"

    def __init__(self, name):
        #Score between 1 and 200
        self.emotion_score = 100
        self.name = name

    #  we define the logic to make an action through this method. (so this method would be the core of your AI)
    def declare_action(self, valid_actions, hole_card, round_state):
        # valid_actions format => [fold_action_info, call_action_info, raise_action_info]
        call_action_info = valid_actions[1]
        pot_size = round_state['pot']['main']['amount']  #Get the current pot size
        raise_amount = 0
        percent = 0

        # Calculate pot odds
        if call_action_info['amount'] > 0:
            pot_odds = self.calculate_pot_odds(pot_size, call_action_info['amount'])
        else:
            pot_odds = 0

        #between 0 and 100
        score = 0
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
            else:
                score = 95

        for com in round_state['community_card']:
            for hol in hole_card:
                if hol[1] in com[1]:
                    score +=100
        
        score = score
        random_influence = random.uniform(0.4, 1.0)
        score = score * random_influence

        score = score * self.emotion_score / 100

        if score < 40:
            # Check
            if call_action_info['amount'] == 0:
                self.adjust_emotion(0)
                return "call", 0
            else:
                self.adjust_emotion(-5)
                return "fold", 0
        elif score < 70:
            self.adjust_emotion(2)
            return "call", call_action_info['amount']
        else:
            self.adjust_emotion(10)
            if pot_odds >= 2:
                percent = 0.75
                raise_amount = self.calculate_raise_amount(pot_size, percent, round_state)   
                return "raise", raise_amount
            
            elif pot_odds >= 0.75:
                percent = 0.5
                raise_amount = self.calculate_raise_amount(pot_size, percent, round_state)   
                return "raise", raise_amount
            
            else:
                percent = 0.25
                raise_amount = self.calculate_raise_amount(pot_size, percent, round_state)   
                return "raise", raise_amount

    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        result = "win" if self.uuid in [winner["uuid"] for winner in winners] else "loss"
        if result == "win":
            self.adjust_emotion(10)
        else:
            self.adjust_emotion(-5)
    
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

    def calculate_pot_odds(self, pot_size, call_amount):
        """
        Calculate the pot odds for making a call.
        Pot odds = (Current Pot Size / Cost to Call)
        """
        return pot_size / call_amount if call_amount > 0 else 0
    
    def calculate_raise_amount(self, pot_size, percent, round_state):
        raise_amount = int(percent*pot_size)
        for player in round_state['seats']:
            if player['name'] == self.name:
                stack = player['stack']
                if raise_amount <= stack and raise_amount > 0:
                    return raise_amount
                else:
                    return max(1, min(raise_amount, stack))