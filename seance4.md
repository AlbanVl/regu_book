---
title: Séance4
description: Présentation du correcteurs PID.
---

# Objectifs de la séance

Dans ce cours, nous avons appris à analyser les caractéristiques d'un système en boucle fermée, à l'aide d'outils tels que la fonction de transfert (paramètres des formes canoniques d'un système du 1{sup}`er` et du 2{sup}`nd` ordre), la réponse indicielle, les diagrammes fréquentiels (Bode, Nyquist et Nichols) ou le lieu des racines (pôles et zéros). Ces outils nous permettent de déterminer à quel point un système est stable ou non, et quelles sont ses performances en termes de précision, de rapidité ou de robustesse.

Mais comment faire si le système ne répond pas à nos exigences ? Comment modifier son comportement pour l'améliorer ? C'est là qu'intervient le correcteur. Un correcteur est un dispositif qui agit sur la commande du système asservi pour réduire l'écart entre la sortie mesurée et la consigne désirée. Il existe différents types de correcteurs, mais nous allons nous intéresser au plus courant : le ***régulateur PID***.

# Le régulateur PID

Le ***régulateur PID*** est composé de trois actions : proportionnelle (P), intégrale (I) et dérivée (D). Chacune de ces actions a un effet différent sur le comportement du système asservi :

- L'action **proportionnelle** (***P***) produit une **correction *proportionnelle* à l'écart entre la valeur mesurée et la valeur désirée**. Elle permet de réduire rapidement cet écart, mais elle peut aussi provoquer des oscillations ou un dépassement de la consigne.
- L'action **intégrale** (***I***) produit une **correction proportionnelle à l'*intégrale* de l'écart dans le temps**. Elle permet d'augmenter la classe du système (=> éliminer par exemple l'erreur statique si le système est de classe 0). Elle peut aussi augmenter le temps de réponse ou la sensibilité aux perturbations.
- L'action **dérivée** (***D***) produit une **correction proportionnelle à la *dérivée* de l'écart par rapport au temps**. Elle permet d'anticiper les variations futures de l'écart et d'amortir les oscillations ou les dépassements. Elle peut aussi amplifier le bruit ou les variations rapides du signal mesuré.

Un régulateur PID est donc un compromis entre ces trois actions, qui doivent être réglées selon les caractéristiques du système asservi et les performances souhaitées. Il existe des méthodes empiriques ou analytiques pour déterminer les paramètres optimaux du régulateur PID.

Un régulateur PID est très utilisé dans l'industrie et dans divers domaines d'application, car il présente plusieurs avantages :

- Il est simple à mettre en œuvre et à comprendre.
- Il est robuste face aux variations des paramètres du système asservi ou aux perturbations extérieures.
- Il peut s'adapter à différents types de systèmes linéaires ou non linéaires, continus ou discrets, monovariables ou multivariables.
- Il peut offrir des performances satisfaisantes pour des objectifs variés : stabilité, précision, rapidité, etc.

Afin de bien comprendre l'utilité et la manière donc chaque paramètre d'un correcteur PID influence le comportement d'un système asservi, voici une [vidéo (*in English*) présentant ce correcteur d'une manière intuitive](https://www.youtube.com/watch?v=wkfEZmsQqiA&t) :

:::{iframe} https://www.youtube.com/embed/wkfEZmsQqiA
:width: 100%

[Qu'est-ce qu'un controlleur PID ?](https://www.youtube.com/watch?v=wkfEZmsQqiA&t)
:::

Si besoin, voici une [courte vidéo supplémentaire](https://www.youtube.com/watch?v=4Y7zG48uHRo) (*still in English*) présentant de nouveau l’effet des différents paramètres mais cette fois-ci sur un cas réel (*i.e.* un suiveur de ligne) :

:::{iframe} https://www.youtube.com/embed/4Y7zG48uHRo
:width: 100%
[Contrôle d'un suiveur de ligne](https://www.youtube.com/watch?v=4Y7zG48uHRo)
:::

Maintenant que vous avez un aperçu du régulateur PID et de ses principes, voyons en détail la relation entre chaque coefficient et le comportement du système. Ainsi, vous pourrez ensuite mettre en œuvre ce contrôleur lors de la prochaine séance pratique pour optimiser les caractéristiques d’un dispositif selon des critères donnés. Alors, prêt·e à passer à un peu de pratique ? 🤓

# Impacts des différents paramètres d'un régulateur PID

:::{tip}Exercice
Comme vous êtes maintenant des as de l’utilisation des jupyter notebook, suivez le [notebook *TheorieSeance4_1* disponible ici](https://git.helmo.be/p150077/regulation-cours/-/raw/main/Theory/Seance4/TheorieSeance4_1.ipynb?ref_type=heads&inline=false). Ainsi, vous pourrez jouer directement sur les différents paramètres d’un régulateur PID (Kp, Ki et Kd) et observer leurs effets sur les graphes utiles pour analyser le comportement d'un système. Prêt·e à commencer ? 🤓
:::

## Impacts du régulateur P

Voyons un peu ce que vous êtes censé avoir observé au cours de votre lecture du notebook. 🧐

:::{note}
Si vous n'avez pas relevé tous les effets cités pour chaque correcteur, je vous invite à retourner les vérifier dans le notebook en allant rejouer avec les différents paramètres concernant le correcteur pour lequel vos observations diffèrent des miennes histoire d'être sûr que vous les voyez bien.
:::

Concernant le correcteur proportionnel ***P***, vous avez normalement pu observer :

**En régime statique**, une augmentation du gain entraîne une **diminution de l’erreur**.

**En régime dynamique**, cette augmentation de gain rend le système **plus rapide** mais, au-delà d’une valeur limite, elle **augmente l’instabilité** du système.

L’effet sur la **réponse fréquentielle** se traduit par une **translation en module de la réponse**.

L’**inconvénient** du correcteur proportionnel est son **incapacité à annuler l’erreur en régime permanent** (d’un système de classe 0 ne possédant aucun pôle à l’origine) lorsque la grandeur d’entrée est de type échelon ($\rightarrow$ erreur statique).

## Impacts du régulateur PI

Concernant le correcteur proportionnel ***PI*** dont l'impact dans le domaine fréquentiel est représenté sur la [](#PI_Bode) :

Pour $t \rightarrow \infty$ (**régime statique** ou permanent) : l’effet du terme intégral est prépondérant : il **annule l’erreur statique**.

Pour $t \rightarrow 0$ (**régime dynamique** ou transitoire) : nous avons vu que le terme intégral avait pour inconvénient d’**augmenter le temps de réponse** (système moins rapide), et d’**augmenter l’instabilité** (introduction d’un déphasage supplémentaire de -90°). Le rôle de la partie P du correcteur PI est de remédier à ces inconvénients.

Par ailleurs, le terme intégral permet de **filtrer la variable à régler** d'où l'utilité pour le réglage des variables bruitées telles que la pression.

:::{figure} images/Seance4/PI_Bode.png
:label: PI_Bode
:alt: Impacts du régulateur PI
:align: center

Impacts du régulateur PI
:::

## Impacts du régulateur PD

Les effets que présente un correcteur ***PD*** (cf. [](#PD_Bode)) sont les suivants :

- **En régime dynamique**, l’intérêt principal de la correction dérivée est de **s’opposer aux grandes variations de l’erreur** (donc aux oscillations) puisque le correcteur D modifie la grandeur de réglage en fonction de la vitesse de variation du signal d’erreur (en pratique, l’impulsion est limitée à la constante de temps $\tau_D$). Elle permet donc de **stabiliser** le système et d’**améliorer le temps de réponse**.
- **En régime statique** (entrée en échelon ou évolution constante) : le D n’intervenant que sur la dérivée de l’erreur, si l’erreur est constante, le dérivateur n’a aucun effet, c’est donc le terme P qui agit en régime établi.

:::{figure} images/Seance4/PD_Bode.png
:label: PD_Bode
:alt: Impacts du régulateur PD
:align: center

Impacts du régulateur PD
:::

### Problèmes liés à l'action dérivée

L’action dérivée permet de compenser les inerties dues aux temps mort, d’**accélérer la réponse du système** et d’**améliorer la stabilité de la boucle**. Elle contribue notamment à **amortir rapidement les oscillations** provoquées par une perturbation ou une variation soudaine de la consigne. L’action dérivée est **utilisée dans l’industrie pour le réglage des variables lentes**, comme la température. Elle n’est **pas recommandée pour le réglage d’une variable bruitée ou trop dynamique**, comme la pression. En effet, en dérivant un bruit (fréquence >> $\Rightarrow$ dt<<), on **risque d’augmenter son amplitude au point de masquer le signal utile** (car d/dt >>).

Souvent, la consigne varie par paliers (type échelon) et donc le signal d’erreur change également par sauts brusques. L’effet du terme dérivé est alors théoriquement infini, ce qui peut saturer le régulateur et le rendre insensible aux variations du signal. **En pratique, on préfère souvent lier l’action du dérivateur aux variations de la grandeur à régler *y(t)* seule et non à l’écart mesure-consigne (= erreur)**, afin d’éviter les à-coups dus à une variation subite de la consigne.

## Impacts du régulateur PID

Le correcteur ***PID*** se comporte :

- Pour les **basses fréquences** comme un **intégrateur** donc le système sera précis d’un point de vue statique.
- Pour les **hautes fréquences** comme un **dérivateur** qui introduit une avance de phase de +90° donc une amélioration de la stabilité.
- Il a donc pour effet (sur toutes les fréquences) d'**annuler l'erreur statique** (en augmentant la classe du système), de **stabiliser** le système et d'**augmenter sa rapidité**.

Son comportment dans le domaine fréquentiel peut être observé sur la [](#PID_Bode).

:::{figure} images/Seance4/PID_Bode.png
:label: PID_Bode
:alt: Impacts du régulateur PID
:align: center

Impacts du régulateur PID
:::

# Fin de la séance

Bravo ! Vous avez terminé la séance théorique ! 🥳

Vous avez appris :

- Ce que sont les correcteurs P, PI, PD et PID ; 
- Quels sont les effets de chaque paramètre sur la réponse d’un système ([](#PID_Compensation_Animated)); 

    :::{figure} images/Seance4/PID_Compensation_Animated.gif
    :label: PID_Compensation_Animated
    :alt: Effets de la variation des paramètres PID (Kp,Ki,Kd) sur la réponse en échelon d'un système
    :align: center

    [Effets de la variation des paramètres PID (Kp,Ki,Kd) sur la réponse en échelon d'un système](https://upload.wikimedia.org/wikipedia/commons/3/33/PID_Compensation_Animated.gif)
    :::
    <!-- TODO: Trouver une image non animée présentant l'impact des différents paramètres pour la version papier tout en conservant le gif pour le site -->

- Les avantages et les inconvénients de chacun des correcteurs. 

Vous disposez maintenant de tous les outils nécessaires pour commencer à réguler des systèmes ! 😎

Il est temps de passer à la pratique et de réguler des systèmes selon des critères définis en choisissant le correcteur approprié et en le dimensionnant lors du prochain labo et des suivants ! 🤓

<!-- TODO: Ajouter un test de compréhension comme fait pour la séance 2 -->