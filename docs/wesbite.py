with open('docs/index.html', 'r') as f:
    content = f.read()
    with open('docs/tempfile.txt', 'w') as f2:
        f2.write(content)
    with open('docs/cssfile.txt', 'w') as f3:
        content = content.split("\n")
        id1 = -1
        id2 = -1
        for line in content:
            line = line.replace(" ", "")
            print(line)
            if(line=="<style>" and id1 < 0):
                id1 = content.index(line)
            if(line=="</style>"):
                id2 = content.index(line)
            # print(id1, id2)
        f3.write("\n".join(content[id1:id2+1]))