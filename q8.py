prompt_a = """
I am a marketing manager at a retail company and we have just finished 
a three-month campaign. My team has collected customer feedback through 
an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the 
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment. I need to present the findings to our CEO next 
Friday in a way that is easy to understand. Can you analyse this data 
for me, highlight which age groups and products have the lowest 
satisfaction scores, identify the most common complaints from the 
written comments, and summarise everything in a short paragraph I can 
use as an executive summary?
"""

prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""


# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer:Prompt_b

# Q8b: Give TWO reasons to support your choice.
# Your answer (Reason 1): One of the key prompt: Constraints (The Guardrails), which is to "Keep the summary concise and free of technical jargon" is present 
# Your answer (Reason 2): One of the key prompt : Format (The Output Structure), which is "Step 1 to 3" tells AI how to present the information.

# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer: One strength is that of telling the AI to "specifically extract the most common compliant from all the written comments" rather to regurgitating all
               other sensitive or non-relevant information from surfacing out in the final executive summary report.


# Task 2
# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.
# Your answer:

I have used prompt_b = """ and re-written it with
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common theme from the written comments.
3. Summarise findings into a "short" executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.

What I borrowed: The key word "short" to replace the word "concise" instead.
Reasons: "Concise" is to be as detailed as possible and this might tells the AI to go into regurgitating out a very lengthy and confusing report with a lot of extra
          and unnecessary informations which will takes up a lot of CEO precious time to dwell over all other irrelevant matters and topics for disscussion.

