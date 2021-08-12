
class Wafi:

    def __init__(self) -> None:
        self.bank = {"User X":39322, "User W": 493202} #using an Hashmap data structure for easy read and write in O(1) times
    
    def add_user(self, user):
        #check if user is already exiting in the bank
        if self.check_user_exist(user):
            return None

        self.bank[user] = 0
        print(user+" successfully added to the bank")
        return user

    def deposit_money(self, user, amount):

        #check if user is already exiting in the bank
        if not self.check_user_exist(user):
            return None
        
        self.bank[user] += amount
        print(user+" successfully depositied $"+str(amount))
        return user

    def transfer_money(self, sender, receiver, amount):

        #check if user is already exiting in the bank
        if not self.check_user_exist(sender):
            return None

        #check if receiver is already exiting in the bank
        if not self.check_user_exist(receiver):
            return None
        
        #check if amount to be transferred exists in users account then transfer
        if self.bank[sender] >= amount:
            self.bank[sender] -= amount
            self.bank[receiver] += amount
            print(sender+" successfully transferred $"+str(amount)+" to "+receiver)
            return self.bank[sender]
        else:
            print("You do not have up to that amount in your account")
            return None
    
    def check_balance(self, user):

        #check if user is already existing in the bank
        if not self.check_user_exist(user):
            return None
        print(user+" currently has $"+str(self.bank[user]))
        return self.bank[user] 

    def check_user_exist(self, user):
        #check if user is already exiting in the bank
        if user not in self.bank:
            print(user+" doesn't exist in the bank") 
            return False
        return True