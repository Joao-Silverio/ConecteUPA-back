# ConecteUPA-back
Para o funcionamento do banco de dados deve-se criar um banco de dados sem senha com o nome de 'conecteupa' no MySql WorkBench
Após isso fazer as instalações dos programas necessários com os comandos

- pip install fastapi
- pip install uvicorn
- pip install sqlalchemy
- pip install mysqlclient
- pip install bcrypt
- pip install PyJWT python-decouple

Após as instalações feitas rode o programa com o seguinte comando:
- python -m uvicorn main:app --port 3333 --reload
