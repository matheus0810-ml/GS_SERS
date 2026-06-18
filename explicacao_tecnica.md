# Explicação técnica — Mission Energy Monitor

## 1. Visão geral

O projeto mantém uma estrutura introdutória baseada em funções, lista, dicionários, condicionais e laço de repetição. Cada leitura é armazenada como um dicionário dentro da lista `historico_leituras`.

## 2. Estrutura principal

### `historico_leituras`

Lista global responsável por armazenar todos os ciclos monitorados.

### `exibir_menu()`

Mostra as seis opções disponíveis ao usuário.

### `inserir_dados()`

Recebe e valida os dados de temperatura, bateria, comunicação, módulo, geração solar e consumo. Em seguida, calcula os indicadores, executa a análise e salva a leitura.

### `calcular_indicadores_energeticos()`

Calcula:

- saldo de potência;
- energia gerada;
- energia consumida;
- percentual de participação renovável.

Cada leitura representa um ciclo de uma hora.

### `analisar_dados()`

Verifica condições críticas e cria duas listas:

- `alertas`;
- `decisoes`.

A função também atualiza o status operacional da missão.

### `mostrar_leitura()`

Centraliza a apresentação detalhada de uma leitura para evitar repetição de código.

### `visualizar_status_atual()`

Mostra a leitura mais recente.

### `executar_analise_automatica()`

Repete a análise da última leitura e apresenta os alertas e respostas automáticas.

### `exibir_historico()`

Percorre a lista de leituras utilizando um laço `for`.

### `exibir_relatorio_energetico()`

Soma os resultados de todos os ciclos e apresenta indicadores gerais de energia e sustentabilidade.

### `sistema_principal()`

Mantém o menu em execução por meio de um laço `while True`. O programa é encerrado quando o usuário escolhe a opção 6.

## 3. Dados monitorados

- temperatura da nave em graus Celsius;
- nível da bateria em porcentagem;
- status da comunicação;
- status do módulo operacional;
- potência solar gerada em watts;
- potência consumida em watts.

## 4. Cálculos

### Saldo de potência

`geração solar - consumo`

Um resultado positivo significa que a geração atende ao consumo. Um resultado negativo representa déficit.

### Energia em kWh

`potência × 1 hora ÷ 1000`

### Participação renovável

`geração solar ÷ consumo × 100`

O resultado é limitado a 100%.

## 5. Tomada de decisão

Os alertas não são apenas exibidos. Cada um produz uma resposta automatizada. Por exemplo:

- bateria crítica → ativar modo de economia;
- déficit energético → reduzir cargas não essenciais;
- falha no módulo → isolar o módulo e iniciar diagnóstico;
- superaquecimento → ativar resfriamento.

## 6. Relação com a disciplina

O projeto utiliza conceitos de potência, energia elétrica, energia solar, consumo, eficiência e sustentabilidade. A análise permite avaliar se a geração renovável é suficiente para manter os módulos da missão.

## 7. Tecnologias

- Python 3;
- recursos nativos da linguagem;
- sem bibliotecas externas;
- execução em terminal ou ambiente como VS Code, PyCharm ou Google Colab.
