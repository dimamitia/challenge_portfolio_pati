from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    language_change_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sing_out_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    dev_team_contact_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a"
    add_player_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button"
    last_createred_player_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[1]/button"
    last_updated_player_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[2]/button"
    last_created_match_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[3]/button"
    last_updated_match_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[4]/button"
    last_updated_report_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[5]/button"


pass