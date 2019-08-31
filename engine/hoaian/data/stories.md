## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
* goodbye
  - utter_goodbye

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
  
## say intro
* ask_who_am_i
  - utter_intro

## say gender
* ask_gender
  - utter_gender
