#!/usr/bin/python3

import base64
import ceasar

# Go to https://www.telenor.no/om/jobbitelenor/visomvaager/
# Open developer tools
# See the code below into the console

# 1. Base64 decode the text
base64_decoded_text = base64.b64decode("SXZOYWZyZ2dyZQ==").decode("utf-8")

# 2. Decipher the text with the ceasar cipher (ROT 13)
print(ceasar.decipher(base64_decoded_text, 13))
