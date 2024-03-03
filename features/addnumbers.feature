Feature: My adder service should add two numbers together and return the result. 
    Scenario: Simple addition
        Given two numbers
        When I call the adder API providing the two numbers
        Then the response will contain the addition of those two numbers

    