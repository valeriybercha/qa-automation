# Locators file


class Locators():

    # Base url
    BaseURL = 'https://www.saucedemo.com'

    # Accepted usernames
    user = 'standard_user'
    user_locked_out = 'locked_out_user'
    user_problem = 'problem_user'
    user_performance_glitch = 'performance_glitch_user'

    # User password
    password = 'secret_sauce'

    # Index login page locators
    input_login_username_id = 'user-name'
    input_login_password_id = 'password'
    input_login_submit_xpath = "//input[@class='btn_action']"
    button_error_xpath = "//button[@class='error-button']"

    # Inventory page locators
    button_hamburger_menu_xpath = "//button[contains(text(),'Open Menu')]"
    a_logout_button_id = 'logout_sidebar_link'
    div_product_label_xpath = "//div[contains(text(), 'Products')]"
