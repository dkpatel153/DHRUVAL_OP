
"""
program which calculate the area of circle
Author = Dhruval patel
"""

cover_prize_book = 24.95
total_copies = 60
first_copy_shipping_cost = 3
other_copy_shipping_cost = 0.75
discount = cover_prize_book * 0.40
cost_of_firstbook = first_copy_shipping_cost + (cover_prize_book - discount)
cost_of_otherbooks = (other_copy_shipping_cost * 59) + (14.97 * 59)
wholesale = cost_of_firstbook + cost_of_otherbooks
print("discount:",discount)
print("cost of firstbook:",cost_of_firstbook,sep="")
print("cost of otherbooks:",cost_of_otherbooks)
print("grand total wholesale cost:",wholesale,sep="")
