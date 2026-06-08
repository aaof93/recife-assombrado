# Sobrevivência Pernambucana ☂️🎭

Um jogo estilo *bullet heaven* / *arena survival* bidimensional focado na cultura, folclore e cenários históricos de Pernambuco. O projeto foi desenvolvido em **Python** utilizando a biblioteca **Pygame**, aplicando conceitos avançados de **Programação Orientada a Objetos (POO)** e otimização de memória para renderização de multidões.

---

## 🎮 A Dinâmica do Jogo

O jogo funde a mecânica de sobrevivência em arena com combate automatizado contra multidões massivas de inimigos.

* **Cenário Dinâmico:** Mapa bidimensional com rolagem de tela infinita que simula pontos turísticos históricos, alternando gradualmente entre o **Marco Zero**, a **Rua do Bom Jesus** e as **ladeiras de Olinda**.
* **Heróis Locais:** O jogador pode escolher entre duas classes de personagens:
  * **Passista de Frevo:** Personagem ágil focado em velocidade e esquiva.
  * **Caboclo de Lança:** Personagem resistente focado em defesa e longo alcance.
* **Combate Automatizado:** A movimentação do personagem é totalmente livre, enquanto os ataques são disparados automaticamente baseados em temporizadores internos (*cooldowns*).
* **Sistema de Progressão:** Ao derrotar inimigos e acumular experiência, o jogo pausa para que o usuário acesse uma tela de seleção de cartas de aprimoramento, permitindo criar combinações cumulativas de habilidades (ex: sombrinhas giratórias defensivas ou lanças mágicas perfurantes).

---

## 💎 Itens Coletáveis

| Item | Nome | Função |
| :---: | :--- | :--- |
| ✨ | **Almas do Capibaribe** | Fragmentos de energia deixados por inimigos que incrementam a barra de experiência (XP), acionando a janela de evolução. |
| 🍰 | **Fatias de Bolo de Rolo** | Consumíveis clássicos de restauração que recuperam instantaneamente uma porcentagem fixa de pontos de vida (HP) ao colidir com o jogador. |
| 🎭 | **Máscaras de Papangu** | Artefatos raros que ativam uma onda de choque ao serem coletados, eliminando imediatamente todos os inimigos de classe menor visíveis na tela. |

---

## 👾 Obstáculos e Inimigos

### 🦴 Ataques da Perna Cabeluda
Grandes bandos de entidades velozes e agressivas que surgem das bordas da tela às centenas. Utilizam vetores de aproximação direta baseados nas coordenadas do jogador para tentar encurralá-lo.

### 👻 Aparições da Emparedada da Rua Nova
Espíritos etéreos que se movem em padrões senoidais imprevisíveis. Possuem a capacidade de ignorar colisões com estruturas sólidas do mapa, exigindo manobras constantes de esquiva.

### 🧳 O Homem do Saco (*Chefe de Onda*)
Inimigos de grande porte e altíssima resistência que surgem em minutos predefinidos do cronômetro. Possuem uma caixa de colisão geométrica expandida e arremessam detritos no mapa para restringir o espaço de navegação do usuário.

---

## 🛠️ Arquitetura de Software & Foco em POO

O coração técnico do software destaca-se pela aplicação rigorosa de padrões de projeto e princípios de POO para garantir escalabilidade e alta performance:

### 1. Herança e Polimorfismo
* **Sistema de Armas:** O arsenal herda de uma classe abstrata denominada `ArmaBase`, que padroniza os métodos de resfriamento (*cooldown*) e atualização geométrica da área de efeito.
* **Sistema de Inimigos:** Os inimigos compartilham uma classe ancestral comum (`InimigoBase`), mas sobrescrevem o método de movimentação de forma distinta:
  * A `PernaCabeluda` utiliza simulação de saltos e velocidade linear.
  * A `Emparedada` sobrescreve a matriz de colisão para não interagir com o ambiente estático.

### 2. Otimização de Memória & Performance
Para suportar a renderização de multidões de entidades simultâneas sem queda de FPS (quadros por segundo), o sistema implementa gerenciadores de grupos customizados (**Render Groups**baseados em `pygame.sprite.Group`). Esses grupos instanciam e destroem automaticamente os objetos na memória conforme eles entram ou saem da área de processamento visual contígua ao jogador.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.10 ou superior instalado.
* Git configurado na máquina.

### Passo a Passo

```bash
# 1. Clone o repositório
git clone [https://github.com/aaof93/sobrevivencia-pernambucana.git](https://github.com/aaof93/sobrevivencia-pernambucana.git)

# 2. Acesse a pasta
cd sobrevivencia-pernambucana

# 3. Crie e ative o ambiente virtual (Recomendado)
python -m venv venv
# No Windows (CMD):
venv\Scripts\activate

# 4. Instale as dependências
pip install pygame

# 5. Execute o jogo
python src/main.py