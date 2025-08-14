import spacy
nlp=spacy.load("en_core_web_sm")

with open("information.txt", "r") as file:
    text = file.read()

doc=nlp(text)

names=[]
emails=[]
github_urls=[]

for ent in doc.ents:
    if ent.label_ == "PERSON":
        names.append(ent.text)
for token in doc:
    if token.like_email:
        emails.append(token.text)
    if token.like_url and "github.com" in token.text:
        github_urls.append(token.text)  

print("Names:", names)
print("Emails:", emails)
print("GitHub URLs:", github_urls)

with open("output.txt", "w") as output_file:
    output_file.write("Names:\n")
    for name in names:
        output_file.write(name + "\n")
    
    output_file.write("\nEmails:\n")
    for email in emails:
        output_file.write(email + "\n")
    
    output_file.write("\nGitHub URLs:\n")
    for url in github_urls:
        output_file.write(url + "\n")