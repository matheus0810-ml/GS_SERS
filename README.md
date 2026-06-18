# Mission Energy Monitor

## Global Solution 2026.1 — Soluções em Energias Renováveis e Sustentáveis

**Aluno:** Matheus Carpinheiro Moreno  
**RM:** 571770  
**Turma:** 1CCPX  
**Modalidade:** Trabalho individual  
**Curso:** Ciência da Computação — FIAP

## Descrição

O **Mission Energy Monitor** é um sistema em Python criado para monitorar dados simulados de uma missão espacial experimental. A solução interpreta informações de temperatura, bateria, comunicação, status do módulo, geração de energia solar e consumo elétrico.

A partir desses dados, o sistema calcula indicadores energéticos, gera alertas, classifica o estado da missão e toma decisões automáticas diante de situações críticas.

## Objetivo

Aplicar conceitos de energia, potência, energias renováveis e sustentabilidade em um sistema computacional simples e organizado, adequado ao primeiro semestre de Ciência da Computação.

## Funcionalidades

- inserção de dados simulados;
- validação dos valores informados;
- monitoramento de temperatura;
- monitoramento do nível da bateria;
- monitoramento da comunicação;
- monitoramento do status do módulo operacional;
- registro da potência gerada pelos painéis solares;
- registro da potência consumida pelos módulos;
- cálculo do saldo de potência;
- cálculo de energia gerada e consumida em kWh;
- cálculo da participação de energia renovável;
- geração automática de alertas;
- respostas automáticas a situações críticas;
- classificação da missão;
- visualização da última leitura;
- histórico das leituras;
- relatório energético e sustentável.

## Menu do sistema

```text
====================================================================
MISSION ENERGY MONITOR
Monitoramento sustentável de uma missão espacial experimental
====================================================================
1. Inserir dados da missão
2. Visualizar status atual
3. Executar análise automática
4. Exibir histórico das leituras
5. Exibir relatório energético
6. Encerrar sistema
====================================================================
```

## Indicadores utilizados

### Saldo de potência

```text
Saldo de potência = geração solar - consumo dos módulos
```

Quando o resultado é negativo, o consumo é maior que a geração solar.

### Energia

Cada leitura representa um ciclo de uma hora:

```text
Energia (kWh) = potência (W) × tempo (h) ÷ 1000
```

### Participação renovável

```text
Participação renovável = geração solar ÷ consumo × 100
```

O valor é limitado a 100% para representar a parcela do consumo atendida pela fonte solar.

## Alertas e decisões automáticas

O sistema pode identificar:

- superaquecimento;
- temperatura extremamente baixa;
- bateria crítica;
- falha de comunicação;
- falha no módulo operacional;
- consumo maior que a geração solar;
- baixa participação de energia renovável.

Para cada situação, o programa recomenda uma ação, como ativar resfriamento, economizar energia, tentar restabelecer a comunicação, isolar um módulo ou reduzir cargas não essenciais.

## Classificação da missão

- **MISSÃO NORMAL:** nenhum alerta;
- **MISSÃO EM ATENÇÃO:** um ou dois alertas;
- **MISSÃO CRÍTICA:** três ou mais alertas.

## Como executar

1. Instale o Python 3.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute:

```bash
python main.py
```

O projeto utiliza apenas recursos nativos do Python e não exige instalação de bibliotecas externas.

## Estrutura do repositório

```text
mission-energy-monitor/
├── main.py
├── README.md
├── entrega.txt
├── roteiro_video.md
└── docs/
    └── explicacao_tecnica.md
```

## Exemplo de cenário normal

```text
Temperatura: 25
Bateria: 85
Comunicação: 1
Módulo: 1
Geração solar: 1200 W
Consumo: 900 W
```

## Exemplo de cenário crítico

```text
Temperatura: 90
Bateria: 15
Comunicação: 0
Módulo: 0
Geração solar: 300 W
Consumo: 1100 W
```

## Sustentabilidade

A solução ajuda a identificar períodos de déficit energético e baixa participação de energia renovável. As decisões automáticas priorizam a preservação da bateria, a redução de cargas não essenciais e o melhor aproveitamento da geração solar.

## Entrega

A entrega da atividade deve conter:

- repositório público no GitHub;
- vídeo não listado no YouTube, com duração máxima de três minutos;
- arquivo `entrega.txt` preenchido com os links finais.

A narração do vídeo deve ser feita pelo próprio aluno.
