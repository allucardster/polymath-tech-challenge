Polymath Tech Challenge
=======================

Requirements
============
- Python 3.7.0
- Pip 18.0
- Virtualenv 16.0.0

Installation
============
- Clone this repository
- From the command line:
```
:~$ virtualenv --python=/path/to/bin/python3.7 env-polymath-tech-challenge
:~$ source env-polymath-tech-challenge/bin/activate
:~$ pip install -r requirements.txt
```

How to run it
=============

### --rebuild

Rebuild the SQLite database and loads eBay categories.

```
:~$ ./categories --rebuild
```

### --render <category_id>

Renders category tree into HTML file

```
:~$ ./categories --render 220
```

Contributors
============

- Richard Melo [Twitter](https://twitter.com/allucardster), [Linkedin](https://www.linkedin.com/in/richardmelo)