# link-in-arc

A Competitive Coding event.

Problem Solving using standard input and output like done in Google Code Jam

This eliminates the use of online Judge and provides flexible problem-solving

Input is taken from a given input file and output is redirected to an output file


```
your_program < input_file.txt > output_file.txt
```

Check out Google Code Jam site for details https://code.google.com/codejam/resources/quickstart-guide


# Build
1. setup virtual environment

```
virtualenv myenv
```

2. clone repo

```
cd myenv

git clone https://github.com/lugnitdgp/link-in-arc
```

3. Activate Virtual Environment

```
source bin/activate
```

4. Install Django and other dependencies

```
pip install django==1.8
```

5. Migrate database and start Django Dev server

```
cd link-in-arc
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

7. access lia on your web browser `http://127.0.0.1:8000`

# Contribute

Technologies used
* HTML, CSS, JavaScript
* Django(Python)

