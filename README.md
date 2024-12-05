# Chatbot Deployment with Flask and JavaScript


This gives 2 deployment options:
- Deploy within Flask app with jinja2 template
- Serve only the Flask prediction API. The used html and javascript files can be included in any Frontend application (with only a slight modification) and can run completely separate from the Flask App then.

## Initial Setup:
This repo currently contains the starter files.

Clone repo and create a virtual environment
```
$ git clone 
$ cd chatbot-deployment
$ python3 -m venv venv
$ .\\venv\\Scripts\\Activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
$ (venv) pip install flask_cors
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modify `intents.json` with different intents and responses for your Chatbot

Run in Browser for Frontend
```
Run python app.py
```
Run in terminal
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```

## Credits:
This repo was used for the frontend code:
https://github.com/hitchcliff/front-end-chatjs
