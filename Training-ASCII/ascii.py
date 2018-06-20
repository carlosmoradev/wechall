#!/usr/bin/python3

# Challenge

# In a computer, you can only work with numbers.
# In this challenge you have to decode the following message, which is in ASCII

# Solution:

cypher_message = "84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 114, 98, 102, 98, 108, 97, 101, 108, 110, 103, 102, 108"

cypher_message = cypher_message.split(", ")

message = ""

for i in cypher_message:
    message += (chr(int(i)))

print message