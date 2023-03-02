# Space Ninjas With Attitude
APS 1 - Algebra Linear e Teoria da Informação - 2023.1

# 1.Integrantes:
- Felipe Maluli de Carvalho Dias
- Lucca Hiratsuca Costa

# 1. Sobre o jogo:  
<div align="center">
  <img src="src/assets/images/katana-ninja.png" width="350" title">
</div>
                                                                  
O jogo "Space Ninjas With Attitude" é uma criação da disciplina de Álgebra Linear e Teoria da Informação, ministrada pelo professor Tiago Fernandes Tavares. Ele é uma adaptação do popular jogo "Angry Birds no espaço" e foi desenvolvido utilizando a linguagem de programação Python, juntamente com a biblioteca Pygame.

O objetivo do jogo é controlar um grupo de ninjas espaciais que devem enfrentar diversos desafios em sua missão. Os jogadores precisam usar suas habilidades de raciocínio lógico e conhecimento de Álgebra Linear para superar os obstáculos e vencer cada fase.

Ao longo do desenvolvimento do jogo, a equipe responsável pela criação teve que aplicar diversos conceitos aprendidos em sala de aula, como matrizes, vetores e sistemas lineares. Além disso, o uso da biblioteca Pygame permitiu a criação de gráficos e efeitos sonoros de alta qualidade, proporcionando uma experiência imersiva para os jogadores.

O resultado final do projeto foi um jogo divertido e desafiador, que uniu o aprendizado teórico da disciplina com a prática de programação e desenvolvimento de jogos. O jogo "Space Ninjas With Attitude" é um exemplo de como a tecnologia pode ser utilizada como ferramenta de ensino, permitindo que os alunos desenvolvam suas habilidades e coloquem em prática os conhecimentos adquiridos em sala de aula.

# 2.Vídeo

Link: https://www.youtube.com/watch?v=G_kvQDHNcSc

# 3. Como rodar?

<div align="center">
  <img src="https://icones.pro/wp-content/uploads/2021/06/icone-github-violet.png" width="350" title">
</div>

## 3.1 Clonar o repositório
Primeiramente, é necessário que se clone o repositório do jogo. <br>
<b> Obs.: </b> Se você não sabe como clonar um repositório, não tem problema! Basta seguir o link a seguir para resolver isso: "https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository"

## 3.2 Instalar dependências
1) Após ter o repositório em sua máquina, é necessário que se instale as dependências as quais o jogo utiliza para o seu funcionamento. Para isso, é necessário que, com o projeto aberto em seu editor de código (VS Code, Intelli J, etc.), seja criado um terminal e que esse esteja também esteja com o diretório do jogo aberto (utilizar comandos 'cd' - Windows ou 'ls' - Linux) para muder de diretório.
2) Certifique-se de que você tem o pip (gerenciador de pacotes Python) instalado. Caso contrário, você pode instalá-lo utilizando o comando sudo apt install python-pip (para sistemas baseados em Debian/Ubuntu) ou sudo yum install python-pip (para sistemas baseados em CentOS/Fedora).
3) Com o diretório do jogo no terminal, podemos baixar todas as dependências necessárias. Para isso, utilize o seguinte comando: <br>
``` 
pip install -r requirements.txt 
```
  Esse comando instalará todas as dependências especificadas no arquivo "requirements.txt" automaticamente.
  
 4) Aguarde até que todas as dependências sejam instaladas. Isso pode levar algum tempo, dependendo do número de pacotes listados e suas respectivas dependências.
 5) Depois que todas as dependências forem instaladas com sucesso, você poderá executar o seu projeto Python normalmente, sem se preocupar com a falta de pacotes necessários.
 
 ## 3.3.Rodar o arquivo.py
 Para rodar o jogo, procure o arquivo 'main.py' - Localizado em src\main.py - diretório do projeto

# 4. Formulação matemática | Modelo Físico:


## 4.1 Força gravitacional - Planetas
```
def calcula_gravidade(self,pos_bola, bola_aceleracao, bola_velocidade):
        distancia_pontos = self.distancia_entre_pontos(self.pos, pos_bola)
        if distancia_pontos <= self.alcance:
            direcao = self.pos - pos_bola # vetor direção da bola em relação ao planeta

            modulo_vetor = np.linalg.norm(direcao) # módulo do vetor direção, ou seja, a distância entre os dois pontos
            vetor_aceleracao = direcao/ modulo_vetor # vetor com a mesma direção do vetor da direção, porém com módulo 1

            mag_a = self.c / modulo_vetor ** 2 # força gravitacional entre os dois corpos (planeta e bola)

            bola_aceleracao = vetor_aceleracao * mag_a # vetor aceleração da bola
            bola_velocidade = bola_velocidade + bola_aceleracao # velocidade da bola

        return bola_aceleracao, bola_velocidade
```
A função "calcula_gravidade" recebe um objeto "self", a posição da bola "pos_bola", a aceleração atual da bola "bola_aceleracao" e a velocidade atual da bola "bola_velocidade" como entrada.

A função calcula a força gravitacional entre a bola e o objeto Planeta (class Planet) com base na distância entre os dois objetos e adiciona essa força à aceleração e velocidade da bola, caso a bola esteja dentro do alcance do objeto.

A função inicia calculando a distância entre a bola e o objeto contendo a função (self.pos) usando a função "distancia_entre_pontos". Se a distância é menor ou igual ao alcance do objeto, a bola é afetada pela força gravitacional.

A função então calcula o vetor direção da bola em relação ao objeto, determina o módulo desse vetor direção (distância entre os dois pontos), e calcula um vetor aceleração com a mesma direção, mas com módulo igual a 1.

A magnitude da força gravitacional entre os objetos é calculada a partir de uma constante gravitacional "c" dividida pelo quadrado do módulo do vetor direção. Essa magnitude é usada para calcular um vetor aceleração para a bola, que é adicionado à sua aceleração atual. Em seguida, a velocidade da bola é atualizada adicionando a nova aceleração.

Finalmente, a função retorna a nova aceleração e velocidade da bola após terem sido afetadas pela força gravitacional.

## 4.2 Lançamento da bolinha:

```
    def lancamento(self, pos_mouse):
        if self.status == 'NÃO LANÇADA':
            self.direcao = pos_mouse - self.posicao
            self.norm_vetor = self.modulo_vetor(self.direcao)
            self.aceleracao = self.direcao/self.norm_vetor
            self.magnitude = 5
            self.velocidade = self.aceleracao * self.magnitude
            self.status = 'LANÇADA'
            self.qtd_lancamentos += 1
        return True
```
A função "lancamento" recebe um objeto "self" e uma posição de mouse "pos_mouse" como entrada. A função é parte de uma classe (Ball) que modela um projétil sendo lançado a partir de uma posição inicial.

A função verifica se o status do projétil é "NÃO LANÇADA". Se o status for esse, a função realiza os seguintes cálculos:

Define a direção do lançamento como a diferença entre a posição do mouse e a posição atual do projétil (self.direcao = pos_mouse - self.posicao).
Calcula o módulo do vetor direção usando a função "modulo_vetor".
Define a aceleração como a direção dividida pelo seu módulo (self.aceleracao = self.direcao/self.norm_vetor).
Define a magnitude da velocidade do projétil como 5 (self.magnitude = 5).
Define a velocidade como a aceleração multiplicada pela magnitude (self.velocidade = self.aceleracao * self.magnitude).
Atualiza o status do projétil para 'LANÇADA'.
Incrementa a quantidade de lançamentos realizados (self.qtd_lancamentos += 1).
A função retorna "True" após completar essas operações.

```
    def movimentar_bola(self):
        return self.posicao + 0.1 * self.velocidade
```

A função "movimentar_bola" também faz parte da classe (Ball). Como entrada, essa função recebe um objeto "self" como entrada e não tem outros parâmetros.

A função calcula a nova posição da bola após um curto período de tempo. A nova posição é calculada usando a posição atual da bola (self.posicao) e a sua velocidade atual (self.velocidade).

O cálculo da nova posição é feito através da multiplicação da velocidade por um fator de tempo fixo de 0.1 e, em seguida, adicionando esse valor à posição atual da bola. Isso assume que a velocidade da bola é constante durante esse período de tempo curto.

Assim, a função "movimentar_bola" retorna a nova posição da bola após ela ter sido movida por um curto período de tempo.
