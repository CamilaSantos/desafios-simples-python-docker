# Estudos Python e Docker 

Este repositório documenta minha jornada de aprendizado em Python e Docker, com foco em aplicações para automação e desenvolvimento. Aqui você encontrará uma coleção de desafios práticos e projetos simples para iniciantes, cada um demonstrando conceitos fundamentais das linguagens e da tecnologia de containerização. 


## Desafios Práticos
#
A seguir, uma lista dos desafios realizados com uma breve descrição do objetivo e os principais conceitos explorados:

* **1\_ola\_mundo:**
    * **Objetivo:** Exibir a mensagem "Olá, Mundo!" no console.
    * **Conceitos:** `print()` em Python, containerização básica com Docker.
* **2\_saudacao\_personalizada:**
    * **Objetivo:** Solicitar o nome do usuário e imprimir uma saudação personalizada.
    * **Conceitos:** `input()`, formatação de strings.
* **3\_calculadora\_simples:**
    * **Objetivo:** Realizar operações matemáticas básicas com dois números.
    * **Conceitos:** Funções, operadores aritméticos, tratamento de erros simples.
* **4\_par\_ou\_impar:**
    * **Objetivo:** Verificar se um número informado pelo usuário é par ou ímpar.
    * **Conceitos:** Operador módulo (`%`), estruturas condicionais (`if/else`).
* **5\_lista\_de\_compras:**
    * **Objetivo:** Criar uma lista de compras simples com um número mínimo de itens.
    * **Conceitos:** Listas em Python, loops (`while`), entrada de dados.
* **6\_media\_notas:**
    * **Objetivo:** Calcular a média de notas de um aluno.
    * **Conceitos:** Listas, loops (`for`), cálculo de média.
* **7\_contagem\_regressiva:**
    * **Objetivo:** Implementar uma contagem regressiva a partir de um número fornecido.
    * **Conceitos:** Loop `while`, decremento de variáveis.
* **8\_tabuada:**
    * **Objetivo:** Exibir a tabuada de um número.
    * **Conceitos:** Loop `for`, formatação de saída.
* **9\_maior_de_três:**
    * **Objetivo:** Peça ao usuário para digitar três números e determine qual deles é o maior.
* **10\conversor_de_celsius_para_fahrenheit:**
    * **Objetivo:**  Solicite a temperatura em Celsius e converta para Fahrenheit usando a fórmula: F=(C×9/5)+32. Imprima o resultado.
#
## Como Executar os Desafios com Docker

Para executar qualquer um dos desafios, siga estes passos:

1.  Navegue até a pasta do desafio desejado:
    ```bash
    cd <nome_da_pasta_do_desafio>
    ```
2.  Construa a imagem Docker:
    ```bash
    docker build -t <nome_do_desafio>_app .
    ```
3.  Execute o container Docker:
    ```bash
    docker run <nome_do_desafio>_app
    ```
    * Para desafios que requerem interação (entrada de dados), você pode precisar adicionar a flag `-it`:
        ```bash
        docker run -it <nome_do_desafio>_app
        ```
#

## Tags

![python](https://img.shields.io/badge/Python-black?style=plastic&logo=python) ![docker](https://img.shields.io/badge/Docker-black?style=plastic&logo=docker) ![desafios-python](https://img.shields.io/badge/Desafios--Python-black?style=plastic) ![aprendizado-python](https://img.shields.io/badge/Aprendizado--Python-black?style=plastic) ![iniciantes-python](https://img.shields.io/badge/Iniciantes--Python-black?style=plastic) ![exemplos-python](https://img.shields.io/badge/Exemplos--Python-black?style=plastic) ![docker-para-iniciantes](https://img.shields.io/badge/Docker--para--Iniciantes-black?style=plastic) ![projetos-python](https://img.shields.io/badge/Projetos--Python-black?style=plastic) ![python-docker](https://img.shields.io/badge/Python--Docker-black?style=plastic)

