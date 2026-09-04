# Sistema Turma do Bem

Projeto acadêmico desenvolvido para auxiliar no cadastro e encaminhamento de profissionais e beneficiários que precisam de atendimento.

## Funcionalidades

- Cadastro de profissionais.
- Listagem de profissionais cadastrados.
- Atualização do telefone de um profissional.
- Exclusão de profissionais por ID.
- Cadastro de beneficiários.
- Triagem da necessidade informada.
- Indicação do tipo de profissional adequado.
- Busca de profissional disponível na cidade do beneficiário.
- Listagem de beneficiários e seus encaminhamentos.
- Armazenamento dos dados em arquivos JSON.

## Tecnologias

- Python 3
- JSON
- SQL/Oracle, por meio do script de banco de dados
- JavaScript, por meio do arquivo `tdb.js`

## Estrutura do projeto

```text
.
├── dados/
│   ├── beneficiarios.json
│   └── profissionais.json
├── tdb.py
├── tdb.js
├── Scripit do Banco de Dados.txt
├── Integrantes do Grupo.txt
└── README.md
```

## Como executar

1. Instale o Python 3.
2. Abra o terminal na pasta do projeto.
3. Crie a pasta de dados, caso ela ainda não exista:

```powershell
New-Item -ItemType Directory -Force dados
```

4. Crie os arquivos `dados/profissionais.json` e `dados/beneficiarios.json` com o conteúdo inicial:

```json
[]
```

5. Execute o sistema:

```powershell
python tdb.py
```

No Windows, também é possível usar:

```powershell
py tdb.py
```

## Como usar

Após iniciar o programa, escolha uma opção no menu digitando o número correspondente:

```text
1 - Cadastrar profissional
2 - Listar profissionais
3 - Atualizar profissional
4 - Deletar profissional
5 - Cadastrar beneficiário
6 - Listar beneficiários
0 - Sair
```

Os dados cadastrados são salvos automaticamente na pasta `dados`.

## Banco de dados

O arquivo `Scripit do Banco de Dados.txt` contém a criação das tabelas, inserção de dados e consultas SQL do projeto. Ele pode ser executado em um ambiente Oracle compatível, conforme a configuração da disciplina.

## Integrantes 

- Ilda Ester Mussungayi Afonso - RM 568233
- Renata Lessa de Almeida - RM 568510
