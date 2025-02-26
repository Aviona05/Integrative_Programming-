"""
QUESTION AND ANSWER:

1. How does the format() function help in combining variables with text in Python? Can you provide a simple example?
Ans. The format() function inserts variables into a string by replacing {} placeholders. Example:
name = "Aviona" 
print("Hello, {}!".format(name)) 
# Output: Hello, Aviona!

2. Explain the basic difference between opening a file in 'read' mode ('r') and 'write' mode ('w') in Python. When would you use each
Ans. 'r' mode reads a file without changing it, while 'w' mode creates or overwrites a file. Use 'r' to view data and 'w' to save new data.

3. Describe what string slicing is in Python. Provide a basic example of extracting a substring from a larger string.
Ans. String slicing in Python allows extracting a portion of a string using indexing. The syntax is string[start:end], where start is inclusive and end is exclusive. For example:
text = "Hello, World!" print(text[0:5])
 # Output: Hello

4. When saving information to a file in Python, what is the purpose of using the 'a' mode instead of the 'w' mode? Provide a straightforward example.
Ans. 'a' mode adds new content to a file without erasing existing data, while 'w' mode replaces it. Example:
with open("file.txt", "a") as f:
f.write("New data\n")

5. Write a simple Python code snippet to open and read a file named "data.txt." How would you handle the case where the file might not exist?
Ans. To open and read a file named "data.txt" while handling the case where it might not exist, you can use a try-except block. This ensures that if "data.txt" does not exist, the program does not crash but instead displays an error message.

"""