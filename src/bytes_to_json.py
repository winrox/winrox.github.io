import json
from python_execute_me import what_to_execute

my_json = str(what_to_execute).replace("'", '"').replace('None', 'null').replace('(', '[').replace(')', ']')
f = open("instructions.js", "w")
f.write(f"const whatToExecute = '{my_json}';")
f.write("\nmodule.exports = { whatToExecute: whatToExecute };")
