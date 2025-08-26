# clase-1.py
from lm import LMSession
import utils

slm = LMSession()

prompt = """
Tengo la siguiente lista de números:

[1,1,1,1,1,1,1]

Quiero que lo ordenes de menor a mayor
"""

results = []
for i in range(10):
    response = slm.execute(prompt, format=None)   # <-- quita "plain"
    if not isinstance(response, str):             # <-- evita pasar None a extract_numbers
        print("LLM sin respuesta, se omite iteración")
        continue
    response = utils.extract_numbers(response)
    results.append(response)

print(results)
