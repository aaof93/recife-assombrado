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
- **Lucas de Assis Silva <las11>:** Responsável pela estruturação visual e *design* dos cenários de rolagem contínua, além de gerenciar os procedimentos de implantação (*deployment*) e garantia de execução do projeto final.
- **Matheus Miranda Borges dos Santos <mmbs2>:** Atuou como facilitador ágil e gestor da equipe (organização, conciliação de agendas e mediação dos *check-points* remotos do grupo). Tecnicamente responsável pelo desenvolvimento da lógica e estruturação das classes dos itens coletáveis, atuando também na elaboração das versões primárias do relatório técnico e dos slides de apresentação.
- **Ubiratan Jose Rodrigues de Lima Junior <ujrlj>:** Responsável pela proposição da ideia base do projeto (adaptação de mecânicas *bullet heaven*), prestando suporte técnico colaborativo na implementação das lógicas de colisões e no aprimoramento da classe do jogador.

---

<a id="objetivos"></a>
## 🎯 2. Principais Objetivos

- Estruturar o projeto de forma organizada atendendo aos requisitos pré-estabelecidos pelo projeto.
- Implementar um sistema de coleta com múltiplos tipos de itens e controle de experiência acumulada.
- Aplicar Lógica de programação e o paradigama de Programação Orientada à Objetos utilizando Python.
- Desenvolver mecânicas de progressão pela aquisição de experiência e inimigos em ondas com dificuldade crescente ao longo do jogo.
- Integrar os conceitos trabalhados em sala de aula, ao longo do período letivo, por meio do desenvolvimento de um jogo 2D interativo(movimentação de um objeto capaz de capturar -colecionar- outros três objetos.

---

<a id="sobre"></a>
## ☂️ 3. Sobre o Jogo

**Recife Assombrado** é um jogo no estilo "bullet heaven" (Vampire Survivors) feito em Python com Pygame e POO, inspirado no folclore, cultura e pontos turísticos de Pernambuco.

<a id="historia"></a>
### 📜 3.1 História
A Passista de Frevo, ou o Caboclo de Lança, começa a sua jornada no Marco Zero(onde tudo se inicia) e precisa lutar contra figuras folclóricas da cultura pernambucana com o intuito de sobreviver e demonstrar a superação do medo, digna do Leão do Norte.

<a id="personagens"></a>
### 🎭 3.2 Personagens
- **Passista de Frevo** - Persinagem principal e jogável.
- **Caboclo de Lança** - Personagem principal e jogável.
- **Ataques da Perna Cabeluda** - Inimigos que provocam dano ao jogador.
- **Aparições da Emparedada da Rua Nova** - Inimigos que provocam dano ao jogador.
- **O Homem do Saco** - Inimigos que provocam dano ao jogador.

<a id="mecanicas"></a>
### ⚙️ 3.3 Mecânicas de Jogo
- Movimento livre no mapa top-down.
- Combate à distâcia por meio de disparos de Lanças.
- Coleta de Almas do Capibaribe(XP), Fatias de Bolo de Rolo(cura) e Máscaras de Papangu(evento especial-onda que destrói inimigos mais fracos presentes na tela).
- Evolução de atributos ao subir de nível. 

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
git clone https://github.com/aaof93/sobrevivencia-pernambucana.git
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
| Iniciar o Jogo | (Mouse) Clique botão direito "Jogar" |
| Selecionar o Personagem | (Mouse) Clique botão direito sobre o personagem desejado |
| Movimento | W, A, S, D |
| Mirar | Mouse |
| Reiniciar(após morte) | (Mouse) Clique botão direito "Jogar Novamente" |
| Seleção de cartas(durante o jogo) | Botões superiores do teclado (1, 2, 3) |

---

<a id="itens"></a>
## 💎 6. Itens, Objetos e Recursos do Jogo

| Item / Recurso | Sprite | Descrição e Utilidade |
| :---: | :---: | :---: |
| **Almas do Capibaribe** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/alma.png" width="50px"> | Permite subir de nível, ao ser coletado, o que desencadeia uma escolha entre algumas opções de aprimoramento da jogabilidade do personagem.
| **Fatias de Bolo de Rolo** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/bolo.png" width="50px"> | Quando coletado recupera uma determinada quantidade de vida do personagem principal.
| **Máscaras de Papangu** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/mascara.png" width="50px"> | Quando coletado desencadeia um evento especial: uma onda de choque que elimina os inimigos mais fracos presentes na tela.

---

<a id="itens"></a>
## 🎭 7. Personagens Presentes no Jogo(Jogador e Inimigos)

| Personagem | Sprite | Descrição |
| :---: | :---: | :---: |
| **Passista de Frevo** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/frevo_esquerda.png" width="50px"> | Personagem principal e jogável.
| **Caboclo de Lança** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/caboclo_esquerda.png" width="50px"> | Personagem principal e jogável.
| **Ataques da perna Cabeluda** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/perna_cabeluda_esquerda.png" width="50px"> | Inimigos que provocam dano ao jogador.
| **Aparições da Emparedada da Rua Nova** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/emparedada_esquerda.png" width="50px"> | Inimigos que provocam dano ao jogador.
| **O Homem do Saco** | <img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/homem_saco_esquerda.png" width="50px"> | Inimigos que provocam dano ao jogador.

---

<a id="estrutura"></a>
## 🏠 8. Estrutura / Arquitetura do Projeto

A arquitetura do software foi concebida sob o paradigma da **Programação Orientada a Objetos (POO)**, visando o encapsulamento de lógicas, alta coesão e baixo acoplamento. O projeto segue um modelo de separação de responsabilidades estruturado da seguinte forma:

- **Módulo Principal (`main.py` e `jogo.py`):** Atuam como o motor central da aplicação, gerenciando o laço principal de repetição (*Game Loop*), a renderização de quadros por segundo (FPS) e a detecção de colisões bidimensionais.
- **Entidades (`jogador.py`, `inimigos.py`, `itens.py` e `armas.py`):** Módulos que contêm as classes instanciáveis. Fazem uso intensivo de herança para padronizar comportamentos comuns (como movimentação e renderização de caixas de colisão) enquanto aplicam polimorfismo para características específicas de cada objeto.
- **Recursos Estáticos (`assets/`, `config.py`, `sons.py`, `cenario.py`):** Isolam constantes do sistema, gerenciamento de memória de mídia (cache de imagens e áudios) e definições globais, evitando o uso de *"magic numbers"* no código principal e facilitando a manutenção.

```text
📂projeto
├──📂.idea
├──📂Prints do projeto
├──📂src
|  ├──📂__pycache__
|  |  ├──armas.cpython-312.pyc
|  |  ├──cartas.cpython-312.pyc
|  |  ├──cenario.cpython-312.pyc
|  |  ├──config.cpython-312.pyc
|  |  ├──inimigos.cpython-312.pyc
|  |  ├──itens.cpython-312.pyc
|  |  ├──jogador.cpython-312.pyc
|  |  ├──jogo.cpython-312.pyc
|  |  ├──jogo.cpython-314.pyc
|  |  └──sons.cpython-312.pyc
|  |
|  ├──📂assets
|  |  ├──a_praieira.mp3
|  |  ├──alma.png
|  |  ├──bolo.png
|  |  ├──botao_como_jogar.png
|  |  ├──botao_descricao.png
|  |  ├──botao_jogar.png
|  |  ├──botao_jogar_novamente.png
|  |  ├──caboclo_direita.png
|  |  ├──caboclo_esquerda.png
|  |  ├──da_lama_ao_caos_estilo.mp3
|  |  ├──emparedada_direita.png
|  |  ├──emparedada_esquerda.png
|  |  ├──frevo_direita.png
|  |  ├──frevo_esquerda.png
|  |  ├──homem_saco_direita.png
|  |  ├──homem_saco_esquerda.png
|  |  ├──intro_sob_pe.mp3
|  |  ├──lanca_final.png
|  |  ├──marco_zero.png
|  |  ├──mascara.png
|  |  ├──perna_cabeluda_direita.png
|  |  ├──perna_cabeluda_esquerda.png
|  |  ├──rua_bom_jesus.png
|  |  ├──sombrinha_giratoria.png
|  |  ├──tela_game_over.jpg
|  |  └──tela_inicial.jpg
|  |  
|  ├──armas.py
|  ├──cartas.py
|  ├──cenario.py
|  ├──config.py
|  ├──inimigos.py
|  ├──itens.py
|  ├──jogador.py
|  ├──jogo.py
|  ├──main.py
|  └──sons.py
|  
├──.gitignore.py
├──LICENSE
├──README.md
├──ideia.md
└──requirements.txt
```

---

<a id="ferramentas"></a>
## 🛠️ 9. Ferramentas, Bibliotecas e Frameworks Utilizados

- **Python**: Adotada por sua sintaxe legível e vasta documentação. Permite a rápida prototipagem de sistemas orientados a objetos e fácil integração com bibliotecas de renderização gráfica.
- **Pygame-ce (Community Edition)**: Escolhida em detrimento da biblioteca Pygame padrão devido às suas melhorias significativas de performance na renderização em tela e correções de bugs, garantindo uma taxa de quadros (FPS) estável mesmo com o processamento de dezenas de instâncias de inimigos simultaneamente.
- **Git & GitHub**: Essenciais para o controle de versão e integração contínua do código. A ferramenta permitiu o desenvolvimento paralelo entre os seis membros da equipe, mitigando conflitos de edição e garantindo o versionamento seguro das implementações.
- **Gemini**: Utilizado para a criação de telas de início e fim de jogo, além do auxílio na elaboração de lógicas complexas e de alguns sprites utilizados no jogo.
- **Pycharm & Visual Studio Code (VS Code)**: Editores de código utilizados para escrita, formatação e depuração da aplicação.
- **w3schools & Youtube**: Fontes complementares de aprendizado consultadas para referências rápidas e tutoriais de implementação.

---

<a id="conceitos"></a>
## 🧠 10. Conceitos da Disciplina Aplicados

### Estruturas Condicionais e de Repetição
O laço `while` é a base estrutural do *Game Loop* no método `executar()` do arquivo `jogo.py`.
As estruturas `if/elif/else` gerenciam o mapeamento de teclas no método `mover()` do arquivo `jogador.py` e o controle minucioso de estados do jogo (menu, seleção, gameplay, game over) em `jogo.py`.
Foram utilizadas para compor o comportamento do jogo a partir de decisões lógicas.
Exemplo: Ao clicar com o mause o botão o jogo inicia; ao pressionar a tecla Esc é possivel retornar ao menu, se selecionados as teclas 1, 2 ou 3, em uma determinada parte do jogo, uma das cartas de aprimoramento são adicionadas ao jogo. Um outro exemplo: se o jogador colide com o inimgo ocorre o evento dano.

### Programação Orientada a Objetos
O projeto foi estruturado com base em Programação Orientada a Objetos, utilizando Classes, métodos construtores, métodos e atributos para representar entidades como jogador, inimgos e itens coletáveis.
Classes abstratas e conceitos de herança estão amplamente presentes, como visto no arquivo `inimigos.py`, onde as classes `PernaCabeluda`, `Emparedada` e `HomemDoSaco` herdam da superclasse ancestral `InimigoBase`, reaproveitando métodos estruturais fundamentais (como `obter_retangulo()` e `desenhar_barra_vida()`).

### Funções
Utilização de funções para agrupar blocos de código reutilizáveis, o que facilita na legibilidade, manutenção e organização do código.

### Polimorfismo
Este conceito é evidenciado principalmente nas classes de armamentos (`armas.py`) e itens (`itens.py`), onde diferentes objetos derivados implementam comportamentos e efeitos distintos ao colidirem (ex: A `AlmaCapibaribe` fornece incremento à barra de XP, enquanto o `BoloDeRolo` afeta diretamente o atributo de HP do jogador instanciado).

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




