from pages.base_page import BasePage


class AddMatch(BasePage):
    main_page_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    name_player_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    matches_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    reports_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[3]/div[2]/span"
    language_change_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[3]/div[1]/div[2]/span"
    sing_out_block_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[3]/div[2]"
    my_team_field_xpath = "//*[@name="myTeam"]"
    enemy_team_field_xpath = "//*[@name="enemyTeam"]"
    my_team_score_field_xpath = "//*[@name="myTeamScore"]"
    enemy_team_score_field_xpath = "//*[@name="enemyTeamScore"]"
    date_placeholder_xpath = "//*[@name="date"]"
    match_at_home_radiobutton = "//*[@name="matchAtHome"] [@value="true"]"
    match_out_home_radiobutton = "//*[@name="matchAtHome"] [@value="false"]"
    tshirt-colour_field_xpath = "//*[ @ name = "tshirt"]"
    league_field_xpath = "//*[ @ name = "league"]"
    time_played_placeholder_xpath = "//*[@name="timePlayed"]"
    number_placeholder_xpath = "//*[@name="number"]"
    web_match_field_xpath = "//*[ @ name = "webMatch"]"
    general_field_xpath = "//*[ @ name = "general"]"
    rating_placeholder_xpath = "//*[@name="rating"]"
    submit_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]"
    clear_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]"
pass