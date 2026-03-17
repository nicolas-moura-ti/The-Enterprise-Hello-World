# 📖 Wiki de Design: A Filosofia da Complexidade Desnecessária

## Introdução
Por que imprimir "Hello World" em 1ms se podemos gastar US$ 5.000,00 por mês em infraestrutura para fazer o mesmo em 40 segundos? Esta página detalha nossa **Filosofia de Design Orientada a Faturas (IBD - Invoice Based Development)**.

## Princípios Arquiteturais
1.  **Abstração da Abstração:** Se o código é legível, ele não é suficientemente "Enterprise". Use pelo menos 5 padrões de design (Strategy, Factory, Proxy, Observer e Decorator) para imprimir uma letra.
2.  **Silos de Dados:** Cada caractere da frase "Hello World" deve residir em um banco de dados diferente para forçar o uso de transações distribuídas (Saga Pattern).
3.  **Resiliência Extrema:** Se o serviço da vírgula cair, o sistema deve entrar em modo de pânico e disparar e-mails para todos os VPs.

## Justificativa de Custo
O uso de Kafka e gRPC para uma string de 11 caracteres justifica a contratação de 3 novos SREs e um contrato de suporte Premium com a Cloud Provider.
