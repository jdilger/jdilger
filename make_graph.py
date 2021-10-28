from contributions.render_html import create_graph
test = create_graph([r"repo_count.txt"], "GEE repositories")

with open('test_mod.html','w') as f:
    f.writelines(test)

with open('test_mod.html') as reader, open('test_mod.html', 'r+') as writer:
  for line in reader:
    if line.strip():
      writer.write(line)
  writer.truncate()

filenames = [ "README_base.md","test_mod.html"]

with open("README.md", "w") as outfile:
    for filename in filenames:
        with open(filename) as infile:
            contents = infile.read()
            outfile.write(contents)