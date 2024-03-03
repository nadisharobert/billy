Feature: My service should divide the first number by the second and return the result. 
    Scenario: Simple division
        Given two numbers
        When I call the divide API providing the two numbers
        Then the response will contain the division of the first number by the second

    Scenario: Divid by zero check
        Given a non zero number
        When I call the divide API providing that number with zero as the second number
        Then the response will give an http error code and a message warning that divide by zero is not allowed
    