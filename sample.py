print('this is a sample python file to see if jenkins is able to correctly run a python file!')
print('---Processing---')
print('20%-----50%------100%')
## saving a sample file to see if archives properly or not

text = "This is the content to save in the file."

with open("output.txt", "w") as file:
    file.write(text)
