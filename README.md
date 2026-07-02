# 👻 Recife Assombrado
---
Relatório de desenvolvimento do jogo Recife Assombrado, desenvolvido para a disciplina de Introdução à Programação do curso de Inteligência Artificial - UFPE / Centro de Informática (CIn), período letivo 2026.1, Equipe 3.

---
## 📑 Índice
- [1. Equipe](#equipe)
  - [1.1 Membros](#membros)
  - [1.2 Divisão de tarefas](#divisao)
- [2. Principais Objetivos](#objetivos)
- [3. Sobre o Jogo](#sobre)
  - [3.1 História](#historia)
  - [3.2 Personagens](#personagens)
  - [3.3 Mecânicas](#mecanicas)
- [4. Como Instalar e Rodar o Jogo](#instalacao)
- [5. Controles](#controles)
- [6. Itens, Objetos e Recursos do Jogo](#itens)
- [7. Personagens Presentes no Jogo(Jogador e Inimigos)](#personagens)
- [8. Estrutura / Arquitetura do Projeto](#estrutura)
- [9. Ferramentas, Bibliotecas e Frameworks Utilizados](#ferramentas)
- [10. Conceitos da Disciplina Aplicados](#conceitos)
- [11. Desafios, Erros e Aprendizados](#desafios)
- [12. Galeria / Capturas de tela](#galeria)

---

<a id="equipe"></a>
## 👥 1. Equipe

<a id="membros"></a>
### 1.1 Membros

<div align="center">
<table width="100%">
<tr>
<td align="center">
<a href="https://github.com/aaof93">
<img src="https://avatars.githubusercontent.com/u/281218739?v=4" width="100px"><br/>
<sub><b>Amanda Almeida de Oliveira Figueredo</b></sub>
</a></br>
<sub>aaof</sub>
</td>

<td align="center">
<a href="https://github.com/Camargo-Geraldo">
<img src="https://avatars.githubusercontent.com/u/16636718?v=4" width="100px"><br/>
<sub><b>Geraldo Camargo Costa Maia Junior</b></sub>
</a></br>
<sub>gccmj</sub>
</td>

<td align="center">
<a href="https://github.com/kauan-programmer">
<img src="https://avatars.githubusercontent.com/u/289440203?v=4" width="100px"><br/>
<sub><b>Kauan Gabriel de Oliveira</b></sub>
</a></br>
<sub>kgo</sub>
</td>

<td align="center">
<a href="https://github.com/Lucas-A-Silva00">
<img src="https://avatars.githubusercontent.com/u/291781644?v=4" width="100px"><br/>
<sub><b>Lucas de Assis Silva</b></sub>
</a></br>
<sub>las11</sub>
</td>

<td align="center">
<a href="https://github.com/Matheus-MB1">
<img src="https://avatars.githubusercontent.com/u/240080750?v=4" width="100px"><br/>
<sub><b>Matheus Miranda Borges dos Santos</b></sub>
</a></br>
<sub>mmbs2</sub>
</td>

<td align="center">
<a href="https://github.com/JoseUbira/">
<img src="https://avatars.githubusercontent.com/u/189497672?v=4" width="100px"><br/>
<sub><b>Ubiratan Jose Rodrigues de Lima Junior </b></sub>
</a></br>
<sub>ujrlj</sub>
</td>
</tr>
</table>
</div>

---

<a id="divisao"></a>
### 📋 1.2 Divisão de Tarefas

- **Amanda Almeida de Oliveira Figueredo <aaof>:** Responsável pela adaptação cultural e concepção criativa do projeto (contextualização para a temática pernambucana, definição formal de coletáveis e inimigos), estruturação do documento base de requisitos (`ideia.md`), inicialização e gestão do repositório no GitHub, arquitetura dos módulos iniciais, desenvolvimento da lógica bidimensional de colisões e da classe do jogador. Atuou também na revisão e consolidação do relatório e da apresentação de slides.
- **Geraldo Camargo Costa Maia Junior <gccmj>:** Responsável pelo desenvolvimento da classe de inimigos e estruturação do laço principal (*Game Loop* no `main.py`). Desempenhou papel fundamental na resolução de conflitos de versionamento e compatibilização de código (*merge* e *bug fixing*), na expansão da arquitetura de software (identificação da necessidade de novos módulos) e na geração dos *assets* visuais do projeto.
- **Kauan Gabriel de Oliveira <kgo>:** Responsável pela codificação e implementação das mecânicas, atributos e métodos específicos atrelados à classe do personagem principal.
- **Lucas de Assis Silva <las11>:** Responsável pela estruturação visual e *design* dos cenários, além de gerenciar os procedimentos de implantação (*deployment*) e garantia de execução do projeto final em múltiplos sistemas operacionais.
- **Matheus Miranda Borges dos Santos <mmbs2>:** Atuou como facilitador ágil e gestor da equipe (organização, conciliação de agendas e mediação dos *check-points* remotos do grupo). Tecnicamente responsável pelo desenvolvimento da lógica e estruturação das classes dos itens coletáveis, atuando também na elaboração das versões primárias do relatório técnico e dos slides de apresentação.
- **Ubiratan Jose Rodrigues de Lima Junior <ujrlj>:** Responsável pela proposição da ideia base do projeto (adaptação de mecânicas *bullet heaven*), prestando suporte técnico colaborativo na implementação das lógicas de colisões e no aprimoramento da classe do jogador.

---

<a id="objetivos"></a>
## 🎯 2. Principais Objetivos

- Estruturar o projeto de forma organizada, atendendo integralmente aos requisitos pré-estabelecidos.
- Implementar um sistema de coleta com múltiplos tipos de itens e controle de experiência acumulada.
- Aplicar a lógica de programação e o paradigma da Programação Orientada a Objetos (POO) utilizando a linguagem Python.
- Desenvolver mecânicas de progressão pela aquisição de experiência e implementação de inimigos em ondas com dificuldade crescente ao longo do tempo.
- Integrar os conceitos trabalhados em sala de aula ao longo do período letivo, por meio do desenvolvimento de um jogo 2D interativo (movimentação de um objeto capaz de capturar e colecionar outros três objetos distintos).

---

<a id="sobre"></a>
## ☂️ 3. Sobre o Jogo

**Recife Assombrado** é um jogo no estilo "bullet heaven" (Vampire Survivors) feito em Python com Pygame e POO, inspirado no folclore, na cultura e nos pontos turísticos de Pernambuco.

<a id="historia"></a>
### 📜 3.1 História
A Passista de Frevo, ou o Caboclo de Lança, começa a sua jornada no Marco Zero (onde tudo se inicia) e precisa lutar contra figuras folclóricas da cultura pernambucana com o intuito de sobreviver e demonstrar a superação do medo, digna do Leão do Norte.

<a id="personagens"></a>
### 🎭 3.2 Personagens
- **Passista de Frevo** - Personagem principal e jogável.
- **Caboclo de Lança** - Personagem principal e jogável.
- **Ataques da Perna Cabeluda** - Inimigos velozes que provocam dano direto ao jogador.
- **Aparições da Emparedada da Rua Nova** - Espíritos etéreos que provocam dano ao jogador e se movem em padrões senoidais.
- **O Homem do Saco** - Chefe (*Boss*) de grande resistência que restringe a navegação do usuário no cenário.

<a id="mecanicas"></a>
### ⚙️ 3.3 Mecânicas de Jogo
- Movimento livre no mapa em perspectiva *top-down*.
- Combate à distância por meio de disparos e ataques automatizados (baseados em tempos de recarga - *cooldowns*).
- Coleta dinâmica de Almas do Capibaribe (XP), Fatias de Bolo de Rolo (cura) e Máscaras de Papangu (evento especial: onda de choque que destrói inimigos menores presentes na tela).
- Sistema de *upgrade* e evolução de atributos a cada progressão de nível.

---

<a id="instalacao"></a>
## 🚀 4. Como Instalar e Rodar o Jogo:

### 0. Pré-requisitos
```
* Python 3.10 ou superior instalado.
* Git configurado na máquina.
```
### 1. Clone o Repositório
```bash
git clone [https://github.com/aaof93/sobrevivencia-pernambucana.git](https://github.com/aaof93/sobrevivencia-pernambucana.git)
cd sobrevivencia-pernambucana

```
### 2. Criar um ambiente virtual local:
```bash
python -m venv .venv
```
### 3. Ativar o ambiente virtual:

#### No Windows(PowerShell):
```bash
.venv\Scripts\Activate.ps1
```
#### 3.1 Se der Erro:
```bash
# Se der erro de "execução de scripts desabilitada", rode este primeiro:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Depois, ative o ambiente:
.venv\Scripts\Activate.ps1
```
#### No Windows(Prompt CMD tradicional):
```bash
.venv\Scripts\Activate.bat
```
#### No Linux / Mac:
```bash
source .venv/bin/activate
```
### 4. Instale as dependências
```bash
pip install -r requirements.txt
```
### 5. Execute o jogo
```bash
python src/main.py
```

<a id="controles"></a>
## 🎮 5. Controles

| Ação | Tecla / Entrada |
|------|----------------|
| Iniciar o Jogo | (Mouse) Clique com o botão esquerdo em "Jogar" |
| Selecionar o Personagem | (Mouse) Clique com o botão esquerdo sobre o personagem desejado |
| Movimento | W, A, S, D |
| Mirar | Cursor do Mouse |
| Reiniciar(após morte) | (Mouse) Clique com o botão esquerdo em "Jogar Novamente" |
| Seleção de cartas(durante o jogo) | Botões superiores do teclado numérico (1, 2, 3) |

---

<a id="itens"></a>
## 💎 6. Itens, Objetos e Recursos do Jogo

| Item / Recurso | Sprite | Descrição e Utilidade |
| :---: | :---: | :---: |
| **Almas do Capibaribe** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/alma.png" width="50px"> | Permite subir de nível ao ser coletado, o que desencadeia uma tela de escolha entre opções de aprimoramento da jogabilidade (upgrades).
| **Fatias de Bolo de Rolo** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/bolo.png" width="50px"> | Consumível de restauração. Quando coletado, recupera uma determinada quantidade de vida do personagem principal.
| **Máscaras de Papangu** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/mascara.png" width="50px"> | Quando coletada, desencadeia um evento especial: uma onda de choque de varredura que elimina os inimigos mais fracos presentes na tela.

---

<a id="itens"></a>
## 🎭 7. Personagens Presentes no Jogo(Jogador e Inimigos)

| Personagem | Sprite | Descrição |
| :---: | :---: | :---: |
| **Passista de Frevo** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/frevo_esquerda.png" width="50px"> | Personagem principal e jogável. Possui alta mobilidade e atributos focados em esquiva.
| **Caboclo de Lança** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/caboclo_esquerda.png" width="50px"> | Personagem principal e jogável. Possui alta resistência, focando em defesa e ataques robustos.
| **Perna Cabeluda** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/perna_cabeluda_esquerda.png" width="50px"> | Inimigo agressivo e veloz que provoca dano ao jogador por aproximação direta.
| **Emparedada da Rua Nova** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/emparedada_esquerda.png" width="50px"> | Inimigo etéreo que exige manobras constantes de esquiva devido ao seu padrão de movimento senoidal.
| **O Homem do Saco** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/homem_saco_esquerda.png" width="50px"> | Entidade do tipo "Chefe" (Boss). Inimigo de grande porte com altíssima resistência que restringe o espaço do mapa.

---

<a id="estrutura"></a>
## 🏠 8. Estrutura / Arquitetura do Projeto

A arquitetura do software foi concebida sob o paradigma da **Programação Orientada a Objetos (POO)**, visando o encapsulamento de lógicas, alta coesão e baixo acoplamento. O projeto segue um modelo de separação de responsabilidades estruturado da seguinte forma:

- **Módulo Principal (`main.py` e `jogo.py`):** Atuam como o motor central da aplicação, gerenciando o laço principal de repetição (*Game Loop*), a renderização de quadros por segundo (FPS) e a detecção de colisões bidimensionais.
- **Entidades (`jogador.py`, `inimigos.py`, `itens.py` e `armas.py`):** Módulos que contêm as classes instanciáveis. Fazem uso intensivo de herança para padronizar comportamentos estruturais (como movimentação e dimensionamento das matrizes de colisão), enquanto aplicam polimorfismo para garantir as características e reações específicas de cada objeto interagido.
- **Recursos Estáticos (`assets/`, `config.py`, `sons.py`, `cenario.py`):** Arquivos que isolam constantes do sistema, gerenciamento otimizado de memória de mídia (cache de imagens e áudios) e definições métricas globais, evitando a poluição do código principal e facilitando a manutenção e escalabilidade.

```text
📂projeto
├──📂.idea             |#Configurações automáticas da IDE(Pycharm)
├──📂Prints do projeto |#Capturas de tela, com o jogo em funcionamento, para a galeria do relatório.
├──📂src               |#Diretório principal que concentra todo o código fonte e os recursos do jogo
|  ├──📂__pycache__    |#Arquivos temporários criados pelo Python para rodar o código mais rápido.
|  ├──📂assets         |#Pasta reservada para guardar imagens, sprites, fontes e aúdios.
|  |  
|  ├──armas.py          |#Mecânicas específicas e objetos interativos que o jogador pode usar.
|  ├──cartas.py         |#Mecânicas específicas e objetos interativos que o jogador pode usar.
|  ├──cenario.py        |#Gerenciamento do mapa, planos de fundo e colisões do ambiente.
|  ├──config.py         |#Variáveis globais e configurações(tamanho da tela, cores, FPS)
|  ├──inimigos.py       |#Lógica, atributos e movimentos dos personagens do jogo.
|  ├──itens.py          |#Mecânicas específicas e objetos interativos que o jogador pode usar.
|  ├──jogador.py        |#Lógica, atributos e movimentos dos personagens do jogo.
|  ├──jogo.py           |#Gerencia o fluxo principal(loop do jogo, telas menus e eventos).
|  ├──main.py           |O arquivo principal que inicializa e roda o jogo.
|  └──sons.py           |#Controle do sistema de efeitos sonoros e músicas de fundo.
|  
├──.gitignore           |#Arquivos que o Git deve ignorar.
├──LICENSE              |#Liçensa
├──README.md            |#Relatório do projeto/Manual do projeto.
├──ideia.md             |#Rascunho de ideias.
└──requirements.txt     |#Lista de bibliotecas para instalar.
```

---

<a id="ferramentas"></a>
## 🛠️ 9. Ferramentas, Bibliotecas e Frameworks Utilizados

- **Python**: Adotada por sua sintaxe legível e vasta documentação. Permite a rápida prototipagem de sistemas orientados a objetos e fácil integração com bibliotecas de renderização gráfica.
- **Pygame-ce (Community Edition)**: Escolhida em detrimento da biblioteca Pygame padrão devido às suas melhorias significativas de performance na renderização em tela e correções de bugs, garantindo uma taxa de quadros (FPS) estável mesmo com o processamento simultâneo de dezenas de instâncias de inimigos.
- **Git & GitHub**: Essenciais para o controle de versão e integração contínua do código. A ferramenta permitiu o desenvolvimento paralelo entre os seis membros da equipe, mitigando conflitos de edição (merge conflicts) e garantindo o versionamento seguro das implementações.
- **Gemini**: Utilizado para o direcionamento de tarefas de gestão, ideação do design de interfaces (como telas de início e fim de jogo) e geração procedural de sprites visuais, superando a barreira da ausência de experiência em design gráfico no grupo.
- **Pycharm & Visual Studio Code (VS Code)**: Editores de código fonte (IDEs) utilizados para escrita, formatação sintática e depuração da aplicação.
- **w3schools & Youtube**: Fontes complementares vitais para o aprendizado autodidata da equipe, servindo de material de consulta para a transição ao paradigma Orientado a Objetos.

---

<a id="conceitos"></a>
## 🧠 10. Conceitos da Disciplina Aplicados

### Estruturas Condicionais e de Repetição

As estruturas de repetição (while, for) e condicionais (if/elif/else) foram empregadas para fundamentar as árvores de decisão lógicas do sistema. Como exemplo, o laço while sustenta o funcionamento ininterrupto do Game Loop no método `executar()` do arquivo `jogo.py`. 
Em paralelo, as validações condicionais operam em frentes críticas: desde a captação de eventos periféricos (como o clique do mouse no botão iniciar ou o pressionamento das teclas 1, 2, 3 para seleção de cartas de upgrade), até o mapeamento vetorial da movimentação (teclas W, A, S, D) e o cálculo de colisões determinando se a sobreposição espacial resultará em dano recebido ou item coletado.

### Programação Orientada a Objetos
O projeto foi estruturado com base em Programação Orientada a Objetos, utilizando Classes, métodos construtores, métodos e atributos para representar entidades como jogador, inimgos e itens coletáveis.
Classes abstratas e conceitos de herança estão amplamente presentes, como visto no arquivo `inimigos.py`, onde as subclasses `PernaCabeluda`, `Emparedada` e `HomemDoSaco` herdam da superclasse ancestral `InimigoBase`, reaproveitando eficientemente métodos estruturais de atualização geométrica (como `obter_retangulo()`) e renderização de UI (como `desenhar_barra_vida()`).

### Funções
Utilização de funções para agrupar blocos de código reutilizáveis, o que facilita na legibilidade, manutenção e organização do código.

### Polimorfismo e Encapsulamento
O conceito de polimorfismo é evidenciado nas classes de armamentos (`armas.py`) e itens consumíveis (`itens.py`), nas quais objetos derivados de origens em comum sobrescrevem métodos para implementar comportamentos e efeitos estritamente individuais ao colidirem (por exemplo: enquanto a `AlmaCapibaribe` fornece incremento à barra de XP, o item `BoloDeRolo` afeta isoladamente a variável de restauração de HP).

---

<a id="desafios"></a>
## 🚧 11. Desafios, Erros e Aprendizados

### ❌ Maior Erro
O principal equívoco do projeto residiu na substimação da complexidade inerente ao desenvolvimento de software e no mau dimensionamento do tempo necessário para a integração dos módulos individuais.
Na fase de concepção, a ausência de experiência prévia fez com que a equipe minimizasse a dificuldade de transpor ideias teóricas para a prática, resultando em discussões prolongadas e inconclusivas sobre o escopo do jogo.
Inicialmente, a arquitetura foi planejada de forma ineficiente para conter apenas cinco módulos, mas ao longo do processo percebeu-se a necessidade de expansão, exigindo a criação imprevista de novos arquivos estruturais para gerenciar áudios, sistema de cartas e transições de cenários. Essa imprecisão no dimensionamento arquitetônico resultou no não cumprimento de deadlines internas, forçando a equipe a reajustar cronogramas continuamente.
Ademais, o volume de horas despendido no desenvolvimento prático superou bastante as projeções iniciais, gerando impactos diretos e negativos na gestão de tempo dos integrantes em relação a outras exigências acadêmicas, especialmente durante o período de avaliações. Para mitigar essas falhas de planejamento, a equipe precisou reestruturar o escopo lógico — priorizando a robustez dos requisitos mínimos — e implementou uma rotina de reuniões de alinhamento mais frequentes, aliada a uma comunicação intensiva via aplicativos de mensagens para conter o atraso nas entregas.

### 🔥 Maior Desafio
O desafio técnico mais substancial enfrentado pela equipe consistiu na abrupta transição de paradigma de programação. Tendo acompanhado uma ementa focada em lógicas lineares e estruturadas durante os três primeiros meses da disciplina, o grupo deparou-se com a necessidade de assimilar e aplicar do zero a Programação Orientada a Objetos (POO) — compreendendo abstrações como classes, herança e polimorfismo — em um curto intervalo de menos de duas semanas. Essa defasagem de conhecimento gerou períodos de desorientação técnica sobre as etapas de desenvolvimento, sendo parcialmente superada mediante horas de estudo autodidata através de plataformas de vídeo (YouTube).
Em paralelo, a compatibilização do código em um ambiente colaborativo via Git/GitHub configurou-se como um obstáculo crítico. A inexperiência com o desenvolvimento simultâneo fez com que a junção de trechos funcionais individuais frequentemente resultasse em falhas sistêmicas (quebras) no jogo, evidenciando a extrema dificuldade de intervir e realizar manutenção em códigos desenvolvidos por terceiros.
Por fim, a ausência de habilidades em design gráfico e gestão de projetos colaborativos foi contornada com a intervenção da monitoria: substituímos os protótipos geométricos iniciais (círculos e quadrados) por assets visuais gerados via Inteligência Artificial (Gemini), ferramenta que também foi fundamental para auxiliar a equipe na elaboração lógica dos próximos passos e na distribuição equilibrada das tarefas.

### ✅ Lições Aprendidas
A principal lição extraída deste projeto é a validação de que a construção de um software transcende a mera escrita de algoritmos, dependendo fundamentalmente de um planejamento arquitetônico prévio. A experiência demonstrou a criticidade da engenharia de software na prática: metodologias como a componentização do código em múltiplos arquivos, o encapsulamento de métodos e a adoção de boas práticas tornaram-se fundamentais para garantir a integridade do sistema quando múltiplos desenvolvedores interagem com a mesma base de código.
Além disso, a importância do trabalho em equipe e da resiliência coletiva ficou evidente ao longo do desenvolvimento do projeto; a disposição dos integrantes para auxiliar mutuamente nas dúvidas sobre os novos paradigmas (POO) e durante as falhas de compatibilização foi o alicerce que sustentou o avanço do jogo. Apesar das inúmeras frustrações enfrentadas com o aprendizado acelerado e os conflitos de versionamento no GitHub, essas adversidades proporcionaram um entendimento prático sobre a dinâmica real e desafiadora do desenvolvimento colaborativo de software.
Conclui-se que o uso disciplinado de repositórios, aliado à comunicação transparente e à flexibilidade para readaptar rotas, é essencial para entregar um produto final coeso, funcional e que atenda aos requisitos acadêmicos estabelecidos.

---

<a id="galeria"></a>
## 📸 12. Galeria / Capturas de tela

<div align="center">
<table width="100%">
  <tr>
    <td width="50%">
      <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/Prints%20do%20projeto/Print1.png" alt"Print 1" width="100%">
      <br><sub>Tela de Início</sub>
    </td>
    <td width="50%">
      <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/Prints%20do%20projeto/Print2.png" alt"Print 2" width="100%">
      <br><sub>Tela de escolha de personagem</sub>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/Prints%20do%20projeto/Print3.png" alt"Print 3" width="100%">
      <br><sub>Tela do jogo em funcionamento 1</sub>
    </td>
    <td width="50%">
      <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/Prints%20do%20projeto/Print4.png" alt"Print 4" width="100%">
      <br><sub>Tela do jogo em funcionamento 2</sub>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/Prints%20do%20projeto/Print5.png" alt"Print 5" width="100%">
      <br><sub>Tela de cartas para aprimoramento 1</sub>
    </td>
    <td width="50%">
      <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/Prints%20do%20projeto/Print6.png" alt"Print 6" width="100%">
      <br><sub>Tela de cartas para aprimoramento 2</sub>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/Prints%20do%20projeto/Print7.png" alt"Print 7" width="100%">
      <br><sub>Tela de cartas para aprimoramento 3</sub>
    </td>
        <td width="50%">
      <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/Prints%20do%20projeto/Print8.png" alt"Print 8" width="100%">
      <br><sub>Tela de Game over (fim de jogo)</sub>
    </td>




