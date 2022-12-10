from booking.bookings import Booking
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# inst = Booking()
# inst.land_first_page()

# with Booking(teardown=True) as bot:
#     bot.land_first_page()
#     print("Exiting....")
    # once python gets out of the indentation of the with method
    # ;it automatically executed the __exti__ method
try:
    with Booking() as bot:
        # a = 2/0 gives Zero division error before even the bot starts
        bot.land_first_page()
        # print("Exiting....")
        bot.change_currency(currency='INR')
        # bot.select_place_to_go("New York")
        # bot.select_dates(check_in_date='2022-12-19',
        #                 check_out_date='2022-12-25')
        # bot.select_adults(10)
        bot.select_place_to_go(input("Where you want to go ?"))
        bot.select_dates(check_in_date=input("What is the check in date ?"),
                         check_out_date=input("What is the check out date ?"))
        bot.select_adults(int(input("How many people ?")))
        bot.click_search()
        # bot.apply_filtrations()
        # print(len(bot.report_results()))
        bot.refresh() # A workaround to let our bot to grab the data properly
        bot.report_results()

        # path in this pc is G:\python datascience ml\Selenium Course\SeleniumDrivers
        # then python run.py in cmd
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise