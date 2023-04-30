import barbecue_sauce, marinara_sauce, plum_tomato_sauce, pumpkin_sauce
import reggiano_cheese, provolone_cheese, mozzarella_cheese, parmesan_cheese
import thin_crust_dough, thick_crust_dough
import chicago_pizza, sicilian_pizza, newyork_style_pizza, greek_pizza

def main():
    print('Hariharan S')
    print('E22MCAG0050')
    print('welcome to XYZ pizza creation software..........')

    Greek = int(input("Please enter prize of Greek pizza "))
    Chicago = int(input("Please enter prize of Chicago pizza "))
    NewYork = int(input("Please enter prize of NewYork pizza "))
    Sicilian = int(input("Please enter prize of Sicilian pizza "))
    PlumTomato = int(input("Please enter prize of PlumTomato Sauce "))
    Marinara = int(input("Please enter prize of Marinara Sauce "))
    Barbecue = int(input("Please enter prize of Barbecue Sauce "))
    Pumpkin = int(input("Please enter prize of Pumpkin Sauce "))
    ThinCrust = int(input("Please enter prize of ThinCrust "))
    ThickCrust = int(input("Please enter prize of ThickCrust "))
    Mozzarella = int(input("Please enter prize of Mozzarella Cheese "))
    Reggiano = int(input("Please enter prize of Reggiano Cheese "))
    Provolone = int(input("Please enter prize of Provolone Cheese "))
    Parmesan = int(input("Please enter prize of Parmesan Cheese "))





    sauce_dict = {'1': plum_tomato_sauce.Plum_Tomato_Sauce(PlumTomato), '2': marinara_sauce.Marinara_Sauce(Marinara), '3': barbecue_sauce.Barbecue_Sauce(Barbecue), '4': pumpkin_sauce.Pumpkin_Sauce(Pumpkin)}

    cheese_dict = {'1':mozzarella_cheese.Mozzarella_Cheese(Mozzarella), '2':reggiano_cheese.Reggiano_Cheese(Reggiano), '3': provolone_cheese.Provolone_Cheese(Provolone), '4':parmesan_cheese.Parmesan_Cheese(Parmesan)}

    dough_dict = {'1': thin_crust_dough.Thin_Crust_Dough(ThinCrust), '2':thick_crust_dough.Thick_Crust_Dough(ThickCrust)}
    while(True):
        p_choice = input(
            f'choose pizza type \n 01. Greek({Greek}) \n 02. Chicago({Chicago}) \n 03. NewYork({NewYork}) \n 04. Sicilian({Sicilian})')
        s_choice = input(f'choose Sauce \n 01. PlumTomato({PlumTomato}) \n 02. Marinara({Marinara}) \n 03. Barbecue({Barbecue}) \n 04. Pumpkin({Pumpkin})')
        d_choice = input(f'choose Dough \n 01. ThinCrust({ThinCrust}) \n 02. ThickCrust({ThickCrust})')
        c_choice = input(f'choose Cheese type \n 01. Mozzarella({Mozzarella}) \n 02. Reggiano({Reggiano}) \n 03. Provolone({Provolone}) \n 04. Parmesan({Parmesan})')

  
        pizza = None
        if p_choice == '1':
            pizza = greek_pizza.Greek_Pizza(Greek, dough_dict[d_choice], cheese_dict[c_choice], sauce_dict[s_choice],p_choice,c_choice,s_choice)
        elif p_choice == '2':
            pizza = chicago_pizza.Chicago_Pizza(Chicago, dough_dict[d_choice], cheese_dict[c_choice], sauce_dict[s_choice],p_choice,c_choice,s_choice)
        elif p_choice == '3':
            pizza = newyork_style_pizza.Newyork_Style_Pizza(NewYork, dough_dict[d_choice], cheese_dict[c_choice], sauce_dict[s_choice],p_choice,c_choice,s_choice)
        elif p_choice == '4':
            pizza = sicilian_pizza.Sicilian_Pizza(Sicilian, dough_dict[d_choice], cheese_dict[c_choice], sauce_dict[s_choice],p_choice,c_choice,s_choice)
        elif(p_choice==5):
            exit()
        else:
            print('wrong choice')




        print('Price of the requested Pizza: ',pizza.calculate_cost())
        pizza.print_details()
        
main()