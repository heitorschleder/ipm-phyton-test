# Requerimentos para rodar
Python 3.5+ - https://www.python.org/

# Após clonar e entrar na pasta do projeto rodar:
pip install virtualenv (caso não tenha instalado)
py -3 -m venv .venv

# Para ativar no windows:
.venv\Scripts\activate

# Para ativar no Linux/Mac:
source venv/bin/activate

# Após criar e ativar a virtualenv rodar:
pip install -r requirements.txt

# Após instalar os requirements
flask run --host=0.0.0.0
