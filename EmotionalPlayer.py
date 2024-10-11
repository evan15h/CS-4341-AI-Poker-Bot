from pypokerengine.players import BasePokerPlayer
import random

class EmotionalPlayer(BasePokerPlayer):  # Do not forget to make parent class as "BasePokerPlayer"

    def __init__(self):
        #Score between 1 and 200
        self.emotion_score = 100

    #  we define the logic to make an action through this method. (so this method would be the core of your AI)
    def declare_action(self, valid_actions, hole_card, round_state):
        # valid_actions format => [raise_action_info, call_action_info, fold_action_info]
        raise_action_info = valid_actions[0]
        call_action_info = valid_actions[1]
        fold_action_info = valid_actions[2]
        action, amount = call_action_info["action"], call_action_info["amount"]

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

        #print(f"Hole cards {hole_card}")
        #print(random_influence)
        #print(f"Hand score {score}")

        if score < 40:
            # Check
            if call_action_info['amount'] == 0:
                self.adjust_emotion(-5)
                print(f"Emotion score {self.emotion_score}")
                return "call", 0
            else:
                self.adjust_emotion(-10)
                print(f"Emotion score {self.emotion_score}")
                return "fold", 0
        elif score < 70:
            self.adjust_emotion(-5)
            print(f"Emotion score {self.emotion_score}")
            return "call", call_action_info['amount']
        else:
            self.adjust_emotion(1)
            print(f"Emotion score {self.emotion_score}")
            return "raise", 20

        #return action, amount   # action returned here is sent to the poker engine

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
            self.adjust_emotion(15)
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