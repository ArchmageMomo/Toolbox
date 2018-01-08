import re
def autoregex(path):
    with open(path, 'r') as content_file:
        file1 = content_file.read()

        file1=str(file1)
        temp= re.compile(r"\n",re.DOTALL).sub(r"\\\\\n", file1)
        temp = re.sub(r"\*(.*?)\*", r"\\textit{\1}", temp, re.DOTALL)
        temp = re.sub(r"\\\\\n\\\\\n\\\\\n(.*?)\\\\\n\\\\\n\\\\\n", r"\n\n\n\\newpage\\section{\1}\n\n\n", temp, re.MULTILINE|re.DOTALL)

        with open ("%re.txt"%(path),'w') as file2:
            file2.write(temp)

autoregex(input("Path to file: "))