class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def step(full_bottles, empty_bottles, num_exchange, bottle_drunk):
            action = False
            if full_bottles:
                action = True
                bottle_drunk += full_bottles
                empty_bottles += full_bottles
                full_bottles = 0
            if num_exchange <= empty_bottles:
                action = True
                empty_bottles -= num_exchange
                num_exchange += 1
                full_bottles += 1
            return action, full_bottles, empty_bottles, num_exchange, bottle_drunk
        
        full_bottles = numBottles
        empty_bottles = 0
        num_exchange = numExchange
        bottle_drunk = 0

        action = True
        while action:
            action, full_bottles, empty_bottles, num_exchange, bottle_drunk = step(full_bottles, empty_bottles, num_exchange, bottle_drunk)
        return bottle_drunk