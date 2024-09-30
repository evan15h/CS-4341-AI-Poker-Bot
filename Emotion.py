class Emotion:
    def __init__(self):
        self.confidence = 1.0  # Neutral state, ranges from 0 (low) to 2 (high)
        self.fear = 0.0  # No fear by default, ranges from 0 to 1
        self.excitement = 0.5  # Neutral excitement level, ranges from 0 to 1
    
    def update_emotion(self, result):
        # Adjust emotions based on the result of the previous round, adjust variables as needed
        if result == 'win':
            self.confidence += 0.1
            self.excitement += 0.05

        elif result == 'loss':
            self.fear += 0.1
            self.confidence -= 0.1
    
    def adjust_decision(self, base_decision):
        # Modify the base decision based on emotions
        if self.confidence > 1.5:  # High confidence leads to more aggressive play
            return 'raise' if base_decision == 'call' else base_decision
        
        elif self.fear > 0.7:  # High fear may lead to folding
            return 'fold'
        
        return base_decision
