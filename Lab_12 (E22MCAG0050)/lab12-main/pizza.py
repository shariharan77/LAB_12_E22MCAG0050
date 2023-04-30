import dough
class Pizza:

    def __init__(self, cost, dough, cheese, sauce,p_choice,c_choice,s_choice) -> None:
        self.__cost = cost
        self.__dough = dough
        self.__cheese = cheese
        self.__sauce = sauce
        self.__p_choice =p_choice
        self.__c_choice = c_choice
        self.__s_choice = s_choice

    def calculate_cost(self):
        Finalprice = self.__cost + self.__dough.get_cost() + self.__cheese.get_cost() + self.__sauce.get_cost()
        discount=0

        if(self.__p_choice == '3'):
            discount = discount+6
        if self.__p_choice == '4':
            discount = discount + 3
        if self.__c_choice == '3':
            discount = discount+4
        if self.__s_choice =='2':
            discount= discount+3


        coustmor_price = (Finalprice-(Finalprice*(discount/100)))
        return coustmor_price

    def print_details(self):
        print('--- details---\n')
        print('-----------------------------------')
        print('|', self.__class__.__name__, '|', self.__cost, '|')
        print('|', self.__dough.__class__.__name__, '|', self.__dough.get_cost(), '|')
        print('|', self.__cheese.__class__.__name__, '|', self.__cheese.get_cost(), '|')
        print('|', self.__sauce.__class__.__name__, '|', self.__sauce.get_cost(), '|')
        print('------------------------------------')
        print('|', 'Total: \t', '|', self.calculate_cost(), '|')
        

    
