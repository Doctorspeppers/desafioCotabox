# Desafio Cotabox #

Desafio feito durante seleção para vaga de estagio.

## Instação

A execução do programa pede apenas que a maquinha tenha python3 instalado com conexão com a internet e pode ser feita pelos arquivos init encontrados na pasta ou executando os comandos abaixo


### Para windows
``` 

pip3 install -r requirements.txt
set FLASK_APP=server.py
python server.py

```

### Para linux


```

#!/bin/bash
pip3 install -r requirements.txt
$env:FLASK_APP = "server.py"
python server.py
```

# Funções adicionais

Alem das funções requisitadas foram adicionadas as seguintes funções

- Deletar Usuario na tabela
- Mudança de unidade/porcentagem no canto superior direito