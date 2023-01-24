from pages.base_page import BasePage


class AddPlayer(BasePage):
    main_page_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    language_change_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sing_out_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    email_field_xpath = "//*[@name="email"]"
    name_field_xpath = "//*[@name="name"]"
    surname_field_xpath = "//*[@name="surname"]"
    phone_field_xpath = "//*[@name="phone"]"
    weight_field_xpath = "//*[@name="weight"]"
    height_field_xpath = "//*[ @ name = "height"]"
    age_placeholder_xpath = "//*[ @ name = "age"]"
    leg_listbox_xpath = "//*[ @ name = "leg"]"
    right_leg_button_xpath = "//*[@id="menu-leg"]/div[3]/ul/li[1]"
    left_leg_button_xpath = "//*[@id="menu-leg"]/div[3]/ul/li[2]"
    club_field_xpath = "//*[ @ name = "club"]"
    level_field_xpath = "//*[ @ name = "level"]"
    main_position_field_xpath = "//*[@name="mainPosition"]"
    second_position_field_xpath = "//*[@name="secondPosition"]"
    district_listbox_xpath = "//*[ @ name = "district"]"
    lower_silesia_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[1]"
    kuyavia_pomerania_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[2]"
    lublin_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[3]"
    lubusz_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[4]"
    lodz_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[5]"
    lesser_poland_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[6]"
    masovia_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[7]"
    opole_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[8]"
    subcarpathia_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[9]"
    podlaskie_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[10]"
    pomerania_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[11]"
    silesia_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[12]"
    holly_cross_province_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[13]"
    warmia_masuria_xpath = "//*[@id="menu-district"]/div[3]/ul/li[14]"
    greater_poland_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[15]"
    west_pomerania_button_xpath = "//*[@id="menu-district"]/div[3]/ul/li[16]"
    achievements_field_xpath = "//*[ @ name = "achievements"]"
    add_language_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[15]/button"
    laczy_nas_pilka_field_xpath = "//*[ @ name = "webLaczy"]"
    ninety_minut_field_xpath = "//*[ @ name = "web90"]"
    facebook_field_xpath = "//*[ @ name = "webFB"]"
    add_link_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[19]/button"
    submit_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]"
    clear_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]"

pass