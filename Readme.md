## EXEMPLO DE API FLASK COM CHAMADA MULTITHREAD

### 1- Crie um virtual enviroment para a aplicação
#### $ virtualenv venv
#### $ source venv/bin/activate 
### 2 - Instale as libs necessárias
#### $ pip install -r requirements.txt 
### 3 - Execute usando o Gunicorn
#### $ gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:ap