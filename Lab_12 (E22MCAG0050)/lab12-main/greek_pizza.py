import pizza

class Greek_Pizza(pizza.Pizza):
    
    def __init__(self, cost, dough, cheese, sauce,p_choice,c_choice,s_choice) -> None:
        super().__init__(cost, dough, cheese, sauce,p_choice,c_choice,s_choice)