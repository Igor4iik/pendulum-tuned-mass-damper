# Pendulum Tuned Mass Damper
## Amortisseur harmonique à pendule
[📄 Lire le rapport complet](Rapport_Amortisseur_harmonique.pdf)

## Présentation
Le but du projet était d’étudier le principe de fonctionnement d’un amortisseur harmonique et de mettre en évidence le phénomène d’atténuation des oscillations lors de la résonance.
J'ai choisi un amortisseur harmonique à pendule car on peut facilement jouer sur sa fréquence propre (en modifiant sa longueur) et aussi parce que le pendule permet de beaucoup mieux visualiser le phénomène ;)

## Maquette expérimentale
La maquette est basée sur la tour Taipei 101. Deux plateformes sont reliées par 4 tiges et représentent la structure simplifiée de la tour.. Le pendule est en liaison pivot avec la plateforme supérieure. Le système bielle-manivelle est en liaison rotule avec la plateforme du bas et simule les tremblements de terre.
Les 2 accéléromètres permettent de comparer les accélérations d'entrée et de sortie pour construire le diagramme de Bode.

<img width="807" height="534" alt="La maquette" src="https://github.com/user-attachments/assets/eb1ad336-58c8-4d5f-ae17-fa370aa9e29c" />


## Résultats
L'étude simplifiée d'un amortisseur harmonique à pendule a permis de mettre en évidence le phénomène d'atténuation des oscillations lors de la résonance. Lors de l'expérience, le pendule a permis de diminuer le gain d'environ 25 dB à la fréquence de résonance. Mais le pendule a également entraîné l'apparition d'un pic de résonance secondaire (une augmentation du gain de 10 dB) qui n'était pas présent sans le pendule.

## Utilisation de IA
L'IA a été utilisée dans le respect de l'éthique scientifique pour les tâches suivantes :
- Aide à la transcription des formules en LaTeX
- Vérification des résultats théoriques et du code
- Corrections linguistiques et de fautes de frappe

## Licences

© 2026 Igor (Igor4iik)

- **Code source (`code/`) :** [MIT License](https://opensource.org/license/mit)
- **Rapport et illustrations originales :** [Creative Commons CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr)

Les contenus provenant de sources externes restent soumis à leurs licences respectives.
