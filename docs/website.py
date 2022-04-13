id1 = -1
id2 = -1
import time
with open('docs/index.html', 'r') as f:
    content = f.read()
    content = content.split("\n")
    for index, line in enumerate(content):
        line2 = line.replace(" ", "")
        # print(line)
        if(line2=="<style>" and id1 < 0):
            id1 = index
        if(line2=="</style>"):
            id2 = content.index(line)

    with open('docs/tempfile.txt', 'w') as f2:
        f2.write("\n".join(content))
    with open('docs/cssfile.txt', 'w') as f3:
        if (id1 == -1 or id2 == -1):
            with open('docs/tempfile.txt', 'r') as f2:
                content = f2.read()
                content = content.split("\n")
        f3.write("\n".join(content[id1:id2+1]))

with open('README.md', 'r') as f:
    content = f.read()
    with open('docs/readmetemp.md', 'w') as f2:
        f2.write(content)
    head = '''<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Github - Sabyasachi Seal</title>
        <link rel="shortcut icon" href="https://sabyasachiseal.me/wp-content/img/github/GitHub-Mark-Light-64px.png" type="image/x-icon">'''
    tail = f'''</div></div></body></html><!--{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}-->'''
    with open('docs/index.html', 'w') as f3:
        with open('docs/cssfile.txt', 'r') as f4:
            css = f4.read()
            f3.write(head+"\n"+css+"\n"+content+"\n"+tail)