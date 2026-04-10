# Sistema Bancário Simples em Python

Este projeto é um **sistema bancário simples**, desenvolvido em Python com foco na prática de **Programação Orientada a Objetos (POO)** e boas práticas de desenvolvimento.

Ele simula operações básicas de um banco, como criação de clientes, contas, depósitos, saques e autenticação.

---

## Objetivo

O objetivo deste projeto é consolidar conceitos como:

- Abstração
- Herança
- Encapsulamento
- Polimorfismo
- Tipagem com Type Hinting
- Organização de código em módulos

---

## Conceitos Aplicados

### Programação Orientada a Objetos (POO)

O sistema foi modelado com base em classes que representam entidades reais:

- `Pessoa`: Classe base com nome e idade
- `Cliente`: Herda de Pessoa e possui uma conta
- `Conta`: Classe abstrata base
- `ContaCorrente`: Conta com limite
- `ContaPoupanca`: Conta sem limite
- `Banco`: Responsável pela autenticação e gerenciamento

---

### Tipagem (Type Hinting)

O projeto utiliza tipagem para tornar o código mais claro e seguro:

```python
def __init__(self, agencia: int, conta: int, saldo: float = 0)
```

Uso de tipos compostos:

```python
self.conta: contas.Conta | None = None
```

---

### Classe Abstrata

A classe `Conta` é abstrata, garantindo que subclasses implementem o método de saque:

```python
import abc

class Conta(abc.ABC):
    @abc.abstractmethod
    def sacar(self, valor_saque: float) -> float:
        pass
```

---

### Herança e Polimorfismo

As classes `ContaCorrente` e `ContaPoupanca` herdam de `Conta` e possuem comportamentos diferentes:

- **Conta Poupança**: só permite saque com saldo disponível
- **Conta Corrente**: permite saque usando limite

---

### Encapsulamento (Getters e Setters)

A classe `Pessoa` utiliza `@property` para controle de acesso:

```python
@property
def nome(self):
    return self._nome

@nome.setter
def nome(self, nome: str):
    self._nome = nome
```

Isso permite validações e protege os dados internos da classe.

---

### Código Limpo (Clean Code)

Boas práticas aplicadas no projeto:

- Separação de responsabilidades em arquivos
- Nomes claros e descritivos
- Métodos curtos e objetivos
- Uso de `__repr__` para facilitar debug
- Evita repetição de código

---

## Funcionalidades

- Criar clientes
- Criar contas (corrente e poupança)
- Depositar valores
- Sacar valores com regras específicas
- Autenticar cliente
- Validar:
  - Agência
  - Conta
  - Cliente
  - Relacionamento cliente-conta

---

## Sistema de Autenticação

A classe `Banco` possui um método responsável por validar as operações:

```python
def autentica(self, cliente, conta):
```

Validações realizadas:

- A agência da conta existe no banco
- A conta está cadastrada no banco
- O cliente está cadastrado
- A conta pertence ao cliente

Se todas as validações forem verdadeiras, a autenticação é realizada com sucesso.

---

## Exemplo de Uso

```python
from pessoas import Cliente
from contas import ContaCorrente
from banco import Banco

c1 = Cliente('André', 19)
cc1 = ContaCorrente(100, 222, 0, 0)
c1.conta = cc1

banco = Banco()
banco.clientes.append(c1)
banco.contas.append(cc1)
banco.agencias.append(100)

if banco.autentica(c1, cc1):
    cc1.depositar(100)
    print(cc1)
```

---

## Saída Esperada

```
O seu saldo é 100.00 (Depósito: 100)
ContaCorrente(100, 222, 100.0, 0)
```

---

## Possíveis Melhorias

- Interface gráfica (GUI)
- API com Flask ou FastAPI
- Persistência de dados (SQLite, PostgreSQL)
- Validações mais robustas
- Sistema de login real

---

## Autor

Desenvolvido por **André Zerger**  
Desenvolvedor Python Júnior

---

## Observação

Este projeto tem fins educacionais e foi desenvolvido para prática de conceitos fundamentais de Python e POO.
