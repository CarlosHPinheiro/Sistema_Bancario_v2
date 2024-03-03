# **Desafio de Projeto**

## **Sistema Bancário com Python**
Nível: Intermediário

Conteúdo: Aplicação dos conceitos de modularidade, utilização de laços e criação de funções.

----
### **DESAFIO**

**Objetivo geral**
- Otimização do Sistema e criação de novas funcionalidades.
- Separar as opções existentes (saque, depósito e extrato) em funções.
- Criar função "Cadastrar Usuário" (cliente).
- Criar função "Cadastrar conta bancária".
----
**Operações (Saque/ Depósito/ Extrato)**

* Operação Saque

  A função Saque deve receber os argumentos por nome  (keyword only).

* Operação Depósito

  A função depósito deve receber os argumentos apenas por posição (positional only).

* Operação Extrato

  A função extrato deve receber os argumentos por posição e nome.

----

**Criar função "cadastrar usuário" (cliente)**

- O programa deve armazenar os usuários em uma lista.

- Um usuário deverá ser composto por: nome, data de nascimento, CPF e endereço.

- O endereço deverá ser uma string com o formato: logradouro, n°- bairro - cidade/ UF.

- Deverá ser armazenado somente os números do CPF.

- Não deve ser possível cadastrar 2 usuários com o mesmo CPF.

----
**Criar função "cadastrar conta bancária"**

- O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário.

- O número da conta é sequencial, iniciando em 1.

- O número da agência é fixo: 0001.

- O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
