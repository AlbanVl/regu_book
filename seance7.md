---
title: Séance 7
description: Exercices de dimensionnement d'un correcteur.
---

# Objectifs de la séance

Nous voilà arrivés à la dernière séance en autonomie ! Nous savons tout ce qu'il nous faut pour dimensionner un correcteur PID en fonction des contraintes fournies dans un cahier des charges et être attentif·ve aux problèmes liés aux différents correcteurs. Cette séance aura donc pour but de continuer à vous familiariser avec le dimensionnement d'un correcteur en fonction des besoins d'un cahier des charges.

# Exercice de dimensionnement d'un correcteur PID

Afin de vous exercer à dimensionner un correcteur PID comme lors des deux dernières séances de laboratoire, je vous invite à résoudre le problème suivant :

:::{tip}Exercice
Soit le système asservi à retour unitaire dont la fonction de boucle ouverte est :

$$H(s)=\frac{20}{(5+s)(2s+3)(4+3s)}$$

On demande de déterminer le correcteur dont le but est de permettre une erreur statique nulle et une erreur de vitesse minimale, tout en assurant une réponse indicielle dont le dépassement est limité à 5%.
:::

:::{note}
L'ensemble des solutions vous sont fournies dans le [](#Solutions). Plus spécifiquement pour cet exercice, vous y trouverez la stratégie de résolution, ainsi que sa solution pour que vous puissiez vérifier votre raisonnement et votre réponse mais **évitez de les lire avant d’avoir résolu l’exercice** sous peine de passer à côté de l’objectif de vous entraîner à résoudre seul·e ce genre d’exercice. Nous avons vu tout ce qu'il faut pour que vous y arriviez donc fouillez dans vos notes et séances précédentes si besoin. 😉
:::

# Exercice type examen

Voici à nouveau un exercice de dimensionnement (sous forme d'un notebook à placer dans le dossier `Seance7` dans le dossier `Theory`) tiré d'un ancien questionnaire d'examen du cours tel qu'il était auparavant ($\Rightarrow$ la variable de Laplace `s` = `p`).

Essayez de le résoudre en vous aidant de vos notes et/ou formulaire.

Vous trouverez évidemment les solutions dans le [](#Solutions) mais évitez de vous y rendre avant d'avoir résolu (ou du moins essayé de résoudre) l'exercice par vous-même. C'est la dernière occasion de vérifier votre maîtrise de dimensionnement seul·e face à un exercice "inédit". 😉

# Fin de la séance

Bravo ! Vous avez terminé la dernière séance théorique ! 🥳

La séance ayant été orientée ce coup-ci beaucoup plus sur la pratique, cette séance vous a permis d'appliquer ce que vous avez vu jusqu'ici sur 2 exercices de dimensionnement de correcteurs et également vu ce qui est attendu comme raisonnement pour cette partie de l'examen.

Lors du prochain et dernier laboratoire, nous continuerons à nous exercer à dimensionner des correcteurs en fonction de contraintes fournies donc n'oubliez pas vos notes et/ou votre formulaire ! 🤓