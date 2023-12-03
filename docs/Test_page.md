## Python. 

```python exec="on"
print("Hello Markdown!")
#assert 1 + 1 == 11
```

---

## Bash  
```bash exec="1" source="tabbed-left" returncode="2"
grep extra_css README.md && exit 2
```

---

## Pyodide  
 ```pyodide
import micropip

print("Installing cowsay...")
await micropip.install("cowsay")
print("done!")
```

---

---

## html pyodide


## Bash  
```bash exec="1" source="material-block"
echo $BASH_VERSION
```

---

## Console  
```console exec="1" source="console"
$ mkdocs --help
```

---

##Tree

```tree
root1
    file1
    dir1
        file
    dir2
        file1
        file2
    file2
    file3
root2
    file1
```

---

## Diagramme cloud
```python exec="true" html="true" source="tabbed-right" title="Diagrams"
--8<-- "diagrams.py"
```

---

```bash exec="1" result="mermaid"
pipdeptree -p mkdocstrings-python --mermaid 2>/dev/null
```