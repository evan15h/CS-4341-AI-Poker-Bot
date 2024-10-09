class Emotion:
   def __init__(self):
       self.confidence = 50  # Neutral state, ranges from 0 (low) to 100 (high)
       self.fear = 0  # No fear by default, ranges from 0 to 100
  
   # Includes ranges of 0 to 100 for both fear and confidence
   def adjust_fear(self, amount):
       if amount < 0:
           if self.fear + amount < 0:
               self.fear = 0
       else:
           if self.fear + amount > 100:
               self.fear = 100


   def adjust_confidence(self, amount):
       if amount < 0:
           if self.confidence + amount < 0:
               self.confidence = 0
       else:
           if self.confidence + amount > 100:
               self.confidence = 100


   #Make sure to actually call this somewhere
   def update_emotion(self, result):
       # Adjust emotions based on the result of the previous round, adjust variables as needed
       if result == 'win':
           self.adjust_confidence(15)
           self.adjust_fear(-5)


       elif result == 'loss':
           self.adjust_confidence(-15)
           self.adjust_fear(+10)
  
   def adjust_decision(self, base_decision, amount=0):
       # Modify the base decision based on emotions
       # Raising increases fear
       # Folding reduces fear


       # Very high confidence
       if self.confidence > 85:  # High confidence leads to more aggressive play


           if base_decision == "raise":
               self.adjust_fear(10)
               return base_decision, amount
           elif base_decision == "call":
               self.adjust_fear(10)
               return 'raise', amount
           elif base_decision == "fold":
               return 'call', amount
          
       # High confidence
       elif self.confidence > 65:  # High confidence leads to more aggressive play


           if base_decision == "raise":
               self.adjust_fear(10)
               return base_decision, amount
           elif base_decision == "call":
               return 'raise', amount
           elif base_decision == "fold":
               self.adjust_fear(-5)
               return base_decision, amount
      
       # High fear
       elif self.fear > 60:  # High fear may lead to folding
           self.adjust_fear(-25)
           return 'fold', amount
      
       return base_decision, amount



# class Emotion:
#     def __init__(self):
#         self.confidence = 1.0  # Neutral state, ranges from 0 (low) to 2 (high)
#         self.fear = 0.0  # No fear by default, ranges from 0 to 1
#         self.excitement = 0.5  # Neutral excitement level, ranges from 0 to 1
    
#     def update_emotion(self, result):
#         # Adjust emotions based on the result of the previous round, adjust variables as needed
#         if result == 'win':
#             self.confidence += 0.1
#             self.excitement += 0.05

#         elif result == 'loss':
#             self.fear += 0.1
#             self.confidence -= 0.1
    
#     def adjust_decision(self, base_decision):
#         # Modify the base decision based on emotions
#         if self.confidence > 1.5:  # High confidence leads to more aggressive play
#             return 'raise' if base_decision == 'call' else base_decision
        
#         elif self.fear > 0.7:  # High fear may lead to folding
#             return 'fold'
        
#         return base_decision
