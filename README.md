# Recife-Assombrado
---
Relatório de desenvolvimento do jogo Recife Assombrado, desenvolvido para a disciplina de Introdução à Programação do curso de Inteligência Artificial - UFPE / Centro de Informática (CIn), período letivo 2026.1, Equipe 3.

---
## Índice
- [1. Equipe](#equipe)
  - [1.1 Membros](#membros)
  - [1.2 Divisão de tarefas](#divisao)
- [2. Principais Objetivos](#objetivos)
- [3. Sobre o Jogo](#sobre)
- [4. Como Instalar e Rodar o Jogo](#instalacao)
- [5. Controles](#controles)
- [6. Itens, Objetos e Recursos do Jogo](#itens)
- [7. Estrutura / Arquitetura do Projeto](#estrutura)
- [8. Ferramentas, Bibliotecas e Frameworks Utilizados](#ferramentas)
- [9. Conceitos da Disciplina Aplicados](#conceitos)
- [10. Desafios, Erros e Aprendizados](#desafios)
- [11. Galeria / Capturas de tela](#galeria)

---

<a id="equipe"></a>
## 1. Equipe

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
### 1.2 Divisão de Tarefas

- **Amanda Almeida de Oliveira Figueredo  <aaof>:** Responsável 
- **Geraldo Camargo Costa Maia Junior<gccmj>:** Responsável 
- **Kauan Gabriel de Oliveira <kgo>:** Responsável 
- **Lucas de Assis Silva<las11>:** Responsável 
- **Matheus Miranda Borges dos Santos <mmbs2>:** Responsável pela parte do código referente aos coletáveis e pela elaboração do relatório.
- **Ubiratan Jose Rodrigues de Lima Junior <ujrlj>:** Responsável 

---

<a id="objetivos"></a>
## 2. Principais Objetivos

- Estruturar o projeto de forma organizada atendendo aos requisitos pré-estabelecidos pelo projeto.
- Implementar um sistema de coleta com múltiplos tipos de itens e controle de experiência acumulada.
- Aplicar Lógica de programação e o paradigama de Programação Orientada à Objetos utilizando Python.
- Desenvolver mecânicas de progressão pela aquisição de experiência e inimigos em ondas com dificuldade crescente ao longo do jogo.
- Integrar os conceitos trabalhados em sala de aula, ao longo do período letivo, por meio do desenvolvimento de um jogo 2D interativo(movimentação de um objeto capaz de capturar -colecionar- outros três objetos.

---

<a id="sobre"></a>
## 3. Sobre o Jogo

**Recife Assombrado** é um jogo no estilo "bullet heaven" (Vampire Survivors) feito em Python com Pygame e POO, inspirado no folclore, cultura e pontos turísticos de Pernambuco.

### História
A Passista de Frevo, ou o Caboclo de Lança, começa a sua jornada no Marco Zero(onde tudo se inicia) e precisam lutar contra figuras folclóricas da cultura pernambucana com o intuito de sobreviver e demonstrar a superação do medo, digna do Leão do Norte.

### Personagens
- **Passista de Frevo** - Persinagem principal e jogável.
- **Caboclo de Lança** - Personagem principal e jogável.
- **Ataques da Perna Cabeluda** - Inimigos que provocam dano ao jogador.
- **Aparições da Emparedada da Rua Nova** - Inimigos que provocam dano ao jogador.
- **O Homem do Saco** - Inimigos que provocam dano ao jogador.

### Mecânicas de Jogo
- Movimento livre no mapa top-down.
- Combate à distâcia por meio de disparos de Lanças.
- Coleta de Almas do Capibaribe(XP), Fatias de Bolo de Rolo(cura) e Máscaras de Papangu(evento especial-onda que destrói inimigos mais fracos presentes na tela).
- Evolução de atributos ao subir de nível. 

---

<a id="instalacao"></a>
## 4. Como Instalar e Rodar o Jogo:

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
## 5. Controles

| Ação | Tecla / Entrada |
|------|----------------|
| Iniciar o Jogo | (Mouse) Clique botão direito "Jogar" |
| Selecionar o Personagem | (Mouse) Clique botão direito sobre o personagem desejado |
| Movimento | W, A, S, D |
| Mirar | Mouse |
| Reiniciar(após morte) | (Mouse) Clique botão direito "Jogar Novamente" |
| Seleção de cartas(durante o jogo) | (Mouse) Clique botão direito sobre a carta desejada |

---

<a id="itens"></a>
## 6. Itens, Objetos e Recursos do Jogo

| Item / Recurso | Sprite | Descrição e Utilidade |
| :---: | :---: | :---: |
| **Almas do Capibaribe** |<img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/alma.png" width="50px"> | Permite subir de nível, ao ser coletado, o que desencadeia uma escolha entre algumas opções de aprimoramento da jogabilidade do personagem.
| **Fatias de Bolo de Rolo** |<img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/bolo.png" width="50px"> | Quando coletado recupera uma determinada quantidade de vida do personagem principal.
| **Máscaras de Papangu** |<img src="https://github.com/aaof93/sobrevivencia-pernambucana/blob/main/src/assets/mascara.png" width="50px"> | Quando coletado desencadeia um evento especial: uma onda de choque que elimina os inimigos mais fracos presentes na tela.

