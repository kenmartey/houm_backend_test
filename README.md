# Pokemon Api Testing

## Setup

### Setup your environment

```bash
virtualenv -p python3.8 venv
```

### Activate your environment

```bash
source venv/bin/activate
```

### Clone the project

```bash
git clone https://github.com/kenmartey/houm_backend_test.git
```

#### cd into project and install requirements.txt

```bash
pip install -r requirements.txt
```

#### Create .env file in project root
Create .env file and set this url as environment variable. Sample is illustrated in .env_sample in the project
NOTE: I put the url because it's a test project
```bash
POKEMON_BASE_URL="https://pokeapi.co/api/v2"
```

### Run project

```bash
python main.py
```

### Run test cases

```bash
pytest test.py  
```
