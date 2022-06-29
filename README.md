## Chess RestApi
We can use our API in two ways:
1. To find all available moves 
2. To check if this move is possible

***
## For the first option we use link:
    http://http://127.0.0.1:5000/api/v1/<figur>/<current_field>/
    local host
## Where "figur" is name of figur and "current_field" is your start position.
## For example:
    http://http://127.0.0.1:5000/api/v1/king/a1
## The result will be:
    {
    "availableMoves": [
        "A2",
        "B1",
        "B2"
    ],
    "error": null,
    "figure": "king",
    "currentField": "A1"
    }
***
## For the second option we use link
     http://http://127.0.0.1:5000/api/v1/api/v1/<figur>/<current_field>/<dest_field>'
## Where "figur" is name of figur, "current_field" is your start position and "dest_field" is your destination.
## For example:
    http://http://127.0.0.1:5000/api/v1/king/a1/a2
## The result will be:
    {
    "move": "Valid",
    "figure": "king",
    "error": null,
    "currentField": "A1",
    "destField": "A2"
    }
    
    #if this destination is valid

## OR:
    {
    "move": "Invalid",
    "figure": "king",
    "error": "Current move is not permitted.",
    "currentField": "A1",
    "destField": "A3"
    }

    #if this destination is invalid
----
    




