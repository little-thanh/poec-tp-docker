# TP DOCKER
### Doc version : v1 - 08/11/2023
## Project description
Calculer un prix avec la TVA.

## Technical info / folder architecture
- src : source code
    - calc.py
    - main.py
    - test_calc.py
- Dockerfile

## Prerequisites
- Docker

## How to dev
Cloner le projet via le terminal avec la ligne suivante :
- git clone https://github.com/thanh-epsi/poec-tp-docker.git

## How to use
#### Dans le terminal

Créer un docker build :
- taper la commande : docker build -t tp-docker . (ne pas oublier le point à la fin)

Tester différents prix/pourcentage en modifiant X et Y
- taper la commande docker run -it tp-docker python src/main.py X Y

#### Exemple :
- docker run -it tp-docker python src/main.py 100 20
- docker run -it tp-docker python src/main.py 100 -10
- docker run -it tp-docker python src/main.py 'abc' 10
- docker run -it tp-docker python src/main.py 100 130

## How to test
### Dans le terminal
Lancer un docker build s'il n'a pas été lancé avant
- taper la commande : docker build -t tp-docker . (ne pas oublier le point à la fin)

Pour lancer les tests :
- taper la commande : docker run -it tp-docker python src/test_calc.py


## Annexe
- Markdown langage : https://www.markdownguide.org/

© Little-thanh