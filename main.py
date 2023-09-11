# write your code here
def padel_court_cost(court_type):
    if court_type.lower() == "indoor":
        return 30
    if court_type.lower() == "outdoor":
        return 20

def rackets_cost(racket_brand):
    if racket_brand.lower() == "bullpadel":
        return 100
    if racket_brand.lower() == "nox":
        return 140
    if racket_brand.lower() == "siux":
        return 200

def padel_ball_cost(ball_boxes):
    if ball_boxes == 1:
        return 2
    if ball_boxes == 2:
        return 3.5
    if ball_boxes == 3:
        return 5

def padel_game_cost():
    court_type = input("Enter the court type (indoor/outdoor): ").lower()
    racket_brand = input("Enter the racket brand (bullpadel/nox/siux): ").lower()
    ball_boxes = int(input("Enter the number of ball boxes: "))
    
    court_cost = padel_court_cost(court_type)
    racket_cost = rackets_cost(racket_brand)
    ball_cost = padel_ball_cost(ball_boxes)
    
    total_cost = court_cost + racket_cost + ball_cost
    print("Total cost:", total_cost)
    return total_cost

padel_game_cost()