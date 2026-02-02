# Sistema de Caixa em Python

## Descrição do Projeto
Este projeto simula um **sistema de caixa** simples, inspirado em situações reais do comércio.  
O sistema permite cadastrar produtos, calcular valores com base em **preço × quantidade**, aplicar **regras de negócio** como desconto e parcelamento, e exibir o total da compra.

O foco do projeto não é apenas a linguagem Python, mas o **raciocínio lógico**, a modelagem das regras e a organização do fluxo do sistema.

---

## Objetivos do Projeto
- Praticar lógica de programação aplicada ao mundo real
- Utilizar estruturas fundamentais do Python:
  - listas e dicionários
  - laços de repetição (`while`)
  - estruturas condicionais (`if`, `elif`, `else`)
- Modelar regras de negócio antes da implementação
- Criar um sistema interativo via terminal

---

## Funcionalidades
- Cadastro de múltiplos produtos
- Cálculo automático do valor por item (preço × quantidade)
- Exibição imediata do total do item após o cadastro
- Cálculo do total geral da compra
- Aplicação de regras de desconto:
  - 3% de desconto para pagamentos via pix, débito ou dinheiro
  - Desconto válido apenas para compras acima de R$ 100,00
- Parcelamento disponível para pagamento no crédito
- Encerramento do sistema via comando `"fim"`

---

## Lógica Aplicada
O sistema utiliza um `while True` para permitir o cadastro contínuo de produtos, sendo encerrado apenas quando o usuário digita `"fim"`.  
As decisões de desconto e parcelamento são baseadas em **condições reais de negócio**, simulando o funcionamento de um caixa comercial.

---

## Tecnologias Utilizadas
- Python 3
- Terminal / Console

---

## Aprendizados
- Importância da indentação em Python
- Uso correto de loops para controle de fluxo
- Separação entre regra de negócio e implementação
- Pensamento lógico antes da escrita do código
- Melhoria da experiência do usuário com feedback imediato

---

## Próximos Passos
- Validação de entradas do usuário
- Geração de cupom fiscal formatado
- Organização do código em funções
- Evolução para interface gráfica ou web

---

##  Autora
Gabriela Basílio  
Estudante de Análise e Desenvolvimento de Sistemas
