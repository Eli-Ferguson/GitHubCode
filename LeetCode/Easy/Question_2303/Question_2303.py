class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:

        payed = 0
        prevBracket = 0

        for upper, percent in brackets :

            if prevBracket > income : break

            amount = upper - prevBracket if income - upper >= 0 else income - prevBracket
            
            payed += amount * percent

            prevBracket = upper
        
        return payed / 100

brackets = [[3,50],[7,10],[12,25]]
income = 10

print( f'Taxes as per question are: ${Solution.calculateTax( super, brackets, income )}' )

# Beats 93.10% Runtime, 69ms
# Beats 65.76% Memory, 13.9mb