## who am i
* whoami
  - utter_whoami

## what is version
* whatisversion
  - utter_whatisversion

## ask favorite food
* ask_favorite_food
    - utter_favorite_food

## ask favorite cuisine
* ask_favorite_cuisine
    - utter_favorite_cuisine

## ask favorite restaurant
* ask_favorite_place
    - utter_favorite_place

## ask to cook affirm
* ask_cook
    - utter_deny
    - utter_ask_cook
* affirm
    - utter_ask_to_cook
* affirm
    - utter_favorite_food
* affirm
    - utter_happy

## ask to cook deny
* ask_cook
    - utter_deny
    - utter_ask_cook
* deny
    - utter_sad

## happy path
* talk_about_food
    - food_form
    - form{"name": "food_form"}
    - form{"name": null}
    - utter_food_hobbies
* affirm
    - utter_happy

## chitchat
* talk_about_food
    - food_form
    - form{"name": "food_form"}
* chitchat
    - utter_chitchat
    - food_form
    - form{"name":null}

## greet
* greet
    - utter_greet

## ask favorite

* ask_favorite_restaurant
    - utter_favorite_place
* ask_favorite_food
    - utter_favorite_food
* ask_favorite_cuisine
    - utter_favorite_cuisine

## ask to cook deny 2

* ask_cook
    - utter_deny
    - utter_ask_cook
* affirm
    - utter_ask_to_cook
* deny
    - utter_sad

## ask to cook deny 3

* ask_cook
    - utter_deny
    - utter_ask_cook
* deny
    - utter_acknowledge

## ask cook deny

* greet
    - utter_greet
* ask_cook
    - utter_deny
    - utter_ask_cook
* deny
    - utter_acknowledge

## ask check restaurant
* ask_check_restaurant
    - utter_ask_favorite_cuisine
* inform_cuisine
    - action_check_restaurants

## ask favorite food 2

* greet
    - utter_greet
* ask_favorite_food
    - utter_favorite_food

## happy path 2

* greet
    - utter_greet
* ask_favorite_food
    - utter_affirm
    - food_form
    - form{"name":"food_form"}
    - slot{"requested_slot":"favorite_cuisine"}

## happy path 3

* ask_like_cuisine
    - utter_affirm
    - food_form
    - form{"name":"food_form"}
    - form{"name": null}

## goodbye

* goodbye
    - utter_goodbye

## ask favorite cuisine 1

* greet
    - utter_greet
* ask_favorite_cuisine
    - utter_favorite_cuisine

## ask favorite restaurant 1

* greet
    - utter_greet
* ask_favorite_restaurant
    - utter_favorite_place