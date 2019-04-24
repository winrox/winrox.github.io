import json

what_to_execute = {
    "instructions": [
        ("LOAD_VALUE", 0),
        ("LOAD_VALUE", 1),
        ("ADD_TWO_VALUES", None),
        ("LOAD_VALUE", 2),
        ("ADD_TWO_VALUES", None),
        ("PRINT_ANSWER", None)
    ],
    "numbers": [7, 5, 8] 
}

my_json = str(what_to_execute).replace("'", '"').replace('None', 'null').replace('(', '[').replace(')', ']')
f = open("instructions.js", "w")
f.write(f"const whatToExecute = '{my_json}';")
f.write("\nmodule.exports = { whatToExecute: whatToExecute };")
