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
<a href="https://github.com/Matheus-MB1">
<img src="https://avatars.githubusercontent.com/u/240080750?v=4" width="100px"><br/>
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

- **Amanda Almeida de Oliveira Figueredo  <aaof>:** Responsável 
- **Geraldo Camargo Costa Maia Junior<gccmj>:** Responsável 
- **Kauan Gabriel de Oliveira <kgo>:** Responsável 
- **Lucas de Assis Silva<las11>:** Responsável 
- **Matheus Miranda Borges dos Santos <mmbs2>:** Responsável pela parte do código referente aos coletáveis e pela elaboração do relatório.
- **Ubiratan Jose Rodrigues de Lima Junior <ujrlj>:** Responsável 

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

### 📜 História
A Passista de Frevo, ou o Caboclo de Lança, começa a sua jornada no Marco Zero(onde tudo se inicia) e precisam lutar contra figuras folclóricas da cultura pernambucana com o intuito de sobreviver e demonstrar a superação do medo, digna do Leão do Norte.

### 🎭 Personagens
- **Passista de Frevo** - Persinagem principal e jogável.
- **Caboclo de Lança** - Personagem principal e jogável.
- **Ataques da Perna Cabeluda** - Inimigos que provocam dano ao jogador.
- **Aparições da Emparedada da Rua Nova** - Inimigos que provocam dano ao jogador.
- **O Homem do Saco** - Inimigos que provocam dano ao jogador.

### ⚙️ Mecânicas de Jogo
- Movimento livre no mapa top-down.
- Combate à distâcia por meio de disparos de Lanças.
- Coleta de Almas do Capibaribe(XP), Fatias de Bolo de Rolo(cura) e Máscaras de Papangu(evento especial-onda que destrói inimigos mais fracos presentes na tela).
- Evolução de atributos ao subir de nível. 

---

<a id="instalacao"></a>
## 🚀 4. Como Instalar e Rodar o Jogo:

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
## 8. Estrutura / Arquitetura do Projeto

```text
📂 projeto
├──
```

---

<a id="ferramentas"></a>
## 🛠️ 9. Ferramentas, Bibliotecas e Frameworks Utilizados

- **Python**: Linguagem de programação utilizada no desenvolvimento do jogo.
- **Pygame**: Biblioteca pricipal para desenvolvimento 2D, renderização, eventos e áudio.
- **Visual Studio Code (VS Code)**: Editor de código para escrita e depuração.
- **Git & GitHub**: Versionamento de código e colaboração.
- **w3schools**: Fonte complementar de aprendizado.
- **Youtube**: Fonte complementar de aprendizado.

---

<a id="conceitos"></a>
## 🧠 10. Conceitos da Disciplina Aplicados

### Estruturas Condicionais
Foram utilizadas para compor o comportamento do jogo a partir de decisões lógicas.
Exemplo: Ao clicar com o mause o botão o jogo inicia; ao pressionar a tecla Esc é possivel retornar ao menu, se selecionados as teclas 1, 2 ou 3, em uma determinada parte do jogo, uma das cartas de aprimoramento são adicionadas ao jogo. Um outro exemplo: se o jogador colide com o inimgo ocorre o evento dano.

### Programação Orientada a Objetos
O projeto foi estruturado com base em Programação Orientada a Objetos, utilizando Classes, métodos construtores, métodos e atributos para representar entidades como jogador, inimgos e itens coletáveis.

### Funções
Utilização de funções para agrupar blocos de código reutilizáveis, o que facilita na legibilidade, manutenção e organização do código.

---

<a id="desafios"></a>
## 🚧 11. Desafios, Erros e Aprendizados

### ❌ Maior Erro
A gestão de tempo poderia ter sido melhor abordada pelo grupo. Cada integrante com suas demandas externas tentou dar o melhor de si para ajustar esses entraves, que foram sendo superados para a finalização de cada uma das demandas associadas ao projeto.

### 🔥 Maior Desafio
Aprendizado de novas ferramentas como Git/GitHub e a gestão de tempo na realização de demandas do projeto em meio a outros compromissos externos ao projeto.

### ✅ Lições Aprendidas
A importância do trabalho em equipe ficou evidente ao longo do desenvolvimento do projeto, com integrantes a disposição para auxiliar e tirar dúvidas sobre os novos conceitos e ferramentas, durante as tarefas e demandas, ou dificuldades que surgiram no decorrer do projeto. A importância da gestão do tempo foi essencial para uma boa realização de um projeto desse escopo. Somado a isso, o trabalho colaborativo, atrelado a comunicação dinâmica(por meio de aplicativos), foi essencial para a realização do projeto, apesar das dificuldades enfrentadas com entendimento sobre ferramentas como Git e GitHub. Essas duas ferramentas nos proporcionaram um melhor entendimento de como se realizar trabalhos em equipe em um projeto de multiplas contribuições.

---

<a id="galeria"></a>
## 📸 12. Galeria / Capturas de tela

<div align="center">
<table width="100%">
  <tr>
    <td width="50%">
      <img src="" alt"Print 1" width="100%">
      <br><sub>Tela de Início</sub>
    </td>
    <td width="50%">
      <img src="" alt"Print 2" width="100%">
      <br><sub>Tela de escolha de personagem</sub>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="" alt"Print 3" width="100%">
      <br><sub>Tela do jogo em funcionamento 1</sub>
    </td>
    <td width="50%">
      <img src="" alt"Print 4" width="100%">
      <br><sub>Tela do jogo em funcionamento 2</sub>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="" alt"Print 5" width="100%">
      <br><sub>Tela de cartas para aprimoramento 1</sub>
    </td>
    <td width="50%">
      <img src="" alt"Print 6" width="100%">
      <br><sub>Tela de cartas para aprimoramento 2</sub>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="" alt"Print 7" width="100%">
      <br><sub>Tela de Game over (fim de jogo)</sub>
    </td>


