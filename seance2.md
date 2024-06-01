---
title: Séance2
description: Matière centrée sur la modélisation et la mesure des performances d'un système.
---

# Objectifs de la séance

Le but de la séance est de continuer à apprendre à modéliser ainsi qu'à analyser un système en observant sa fonction de transfert et son comportement dans le domaine temporel. La séance se déroule au fil des étapes suivantes :

- Modélisation d'un système en cascade;
- Modélisation d'un retard;
- Analyse de la stabilité d'un système à partir de sa fonction de transfert;
- Analyse de la précision d'un système.

# Système en cascade

Pour rappel, voici le schéma complet d'un système contrôlé ([](#generalFeedbackSystem)) :

:::{figure} images/Seance2/generalFeedbackSystem.png
:label: generalFeedbackSystem
:alt: Représentation général d'un système asservis
:align: center

Représentation général d'un système asservis avec une consigne $r(t)$, des perturbations $d_{in}(t)$ et $d_{out}(t)$ et du bruit sur la mesure $n(t)$
:::

Les blocs $C(s)$, $P(s)$ et $F(s)$ sont respectivement les fonctions de transfert du régulateur (***C****ontroller*), du système (***P****rocess*) et de la boucle de contre-réaction (***F****eedback*).

:::{note}
`s` est la notation anglophone de la variable complexe qui peut représenter la fréquence dans la transformée de Laplace. Pour information, celle-ci se note généralement `p` dans les littératures française et allemande qui sont nettement moins courantes que l'anglais dans les écrits scientifiques.
:::

On peut observer qu'il y a quatre entrées :

1. La consigne $r(t)$ (en anglais: *reference input*)
1. La perturbation en entrée $d_{in}(t)$ (en anglais : *input disturbance*)
1. La perturbation en sortie $d_{out}(t)$ (en anglais : *output disturbance*)
1. Le bruit sur la mesure $n(t)$ (en anglais : *sensor noise*)

En général, les trois première sont plutôt des signaux de basses fréquences alors que la dernière est active dans les hautes fréquences.

:::{note}
Les signes `-` sur les perturbations et le bruit sont là par convention de notation mais pourraient très bien être des `+`.
:::

Néanmoins, un système peut être plus complexe que cela en étant composé de plusieurs sous-systèmes. On parle dans ce cas d'un système en cascade qui peut également être repésenté par un schéma bloc. Voici par exemple un système de gestion de la position d'un moteur électrique [^demo_horloge] ([](#positionControl_cascadedSystem)) :

:::{figure} images/Seance2/positionControl_cascadedSystem.png
:label: positionControl_cascadedSystem
:alt: Schéma fonctionnel d’un système de contrôle de position en cascade
:align: center

Schéma fonctionnel d’un système de contrôle de position. Le système dispose de trois boucles en cascade pour le contrôle du courant, de la vitesse et de la position. Chaque boucle a une valeur de référence fournie en externe (indiquée par l’indice 'r') qui définit la valeur nominale de l’entrée à la boucle, qui est ajoutée à la sortie de la boucle externe suivante pour déterminer la valeur commandée pour la boucle (appelée « point de consigne »). {cite:p}`åström2021feedback{fig 1.13}`
:::

Celui-ci est composé de 3 systèmes bouclés (= asservis) :

1. La boucle interne est la boucle de courant où le contrôleur (*CC*) pilote l'Amplificateur de telle manière que le courant qui arrive au moteur suive la commande désirée (= {term}`Consigne`).
1. La boucle au milieu utilise un contrôleur de vitesse (*VC*) pour gérer la consigne de courant de telle manière que la vitesse suive sa propre consigne.
1. La boucle externe pilote la consigne de la boucle de vitesse pour suivre la consigne fournie au contrôleur de position (*PC*).

Cette architecture de contrôle en cascade est courante et permet de simplifer la conception, la mise en oeuvre et l'exploitation d'un système complexe. Néanmoins, cela nécessite que chaque sous-système soit correctement régulé afin d'offrir un maximum de modularité (= chaque boucle de contrôle peut-être remplacée par une autre équivalente sans que cela ne modifie le comportement du système global). Si on considère que le contrôleur de courant (*CC*) dans notre exemple est bien dimensionné pour gérer le courant selon la consigne qui lui est fournie. Vu que le couple du moteur est proportionnel au courant, la dynamique reliant la vitesse du moteur à l'entrée du contrôleur de courant est approximativement un inégrateur. Ce modèle simplifié peut être utilisé pour concevoir la boucle de vitesse afin de réduire les effets de frottement et d’autres perturbations. Avec une boucle de vitesse bien conçue, la conception de la boucle de position est également simple. Les boucles peuvent également être réglées séquentiellement en commençant par la boucle interne. Dès lors, si tout est bien régulé, on peut simplifier la représentation du système de cette manière ([](#positionControl_reducedSystem)) :

:::{figure} images/Seance2/positionControl_reducedSystem.png
:label: positionControl_reducedSystem
:alt: Schéma fonctionnel d’un système de contrôle de position réduit
:align: center

Schéma fonctionnel du système de contrôle de position réduit
:::

Où on ne représente plus les sous-systèmes puisque ceux-ci ne modifient pas le comportement global du système et on se retrouve donc avec un système semblable à la représentation générale d'un système asservi.

Cette architecture montre comment la rétroaction peut être utilisée pour simplifier l’ensemble de la conception du contrôleur en divisant le problème en étapes. Cette architecture fournit également un niveau de modularité puisque chaque étape de conception ne dépend que du comportement en boucle fermée du système. Si nous remplaçons le moteur par un nouveau moteur, alors en redessinant le contrôleur de courant (*CC*) pour donner les mêmes performances en boucle fermée, nous pouvons laisser les boucles de niveau extérieur inchangées. De même, si nous devons reconcevoir l’un des contrôleurs de couche externe pour une application avec des spécifications différentes, nous pouvons souvent utiliser une conception de boucle interne existante (tant que la conception existante fournit des performances suffisantes pour satisfaire les exigences de la boucle externe).

[^demo_horloge]: cf. démonstration faite faite avec l'"horloge" lors de la première séance de cours.

# Modélisation d'un retard

Nous avons examiné ensemble, lors du premier laboratoire, les formes canoniques des systèmes du 1{sup}`er` et du 2{sup}`nd` ordre, rappelées ci-dessous :


Forme canonique d'un système d'ordre 1 :

$$G(s) = \frac{K}{\tau s + 1}$$

Où :

- $s$ est la variable complexe de Laplace,

- $K$ est le ***gain statique***,

- $\tau$ est la ***constante de temps***.


Forme canonique d'un système d'ordre 2 :

$$G(s) = \frac{K}{\frac{1}{\omega_n^2}s^2 + 2\frac{\zeta}{\omega_n} s + 1}$$

Où :

- $s$ est la variable complexe de Laplace,

- $K$ est le ***gain statique***,

- $\zeta$ est le ***coefficient d'amortissement***,

- $\omega_n$ est la ***pulsation naturelle*** du système.


Cependant, dans certains systèmes réels, la réponse peut présenter un retard par rapport à la variation de l'entrée, comme observé dans des contextes tels que la propagation nerveuse, les systèmes de communication et le transport de masse.

Pour calculer formellement la fonction de transfert d'un système, nous utilisons un signal particulier appelé signal exponentiel, de la forme $e^{st}$, où $s = \sigma + j\omega$ est un nombre complexe. Les signaux exponentiels jouent un rôle crucial dans les systèmes linéaires, apparaissant dans la solution des équations différentielles et dans la réponse impulsionnelle des systèmes linéaires.

Un système avec un délai de temporisation suit la relation d'entrée/sortie suivante :

$$y(t) = u(t-\theta_p)$$

Pour obtenir la fonction de transfert correspondante, l'entrée est $u(t) = e^{st}$, et la sortie devient :

$$y(t) = u(t-\theta_p) = e^{s(t-\theta_p)} = e^{-s\theta_p}e^{st} = e^{-s\theta_p}u(t)$$

On constate ainsi que la fonction de transfert d'une temporisation est $G(s) = e^{-s\theta_p}$, ce qui n'est pas une fonction rationnelle.

# Impact du coefficient d'amortissement sur la stabilitié d'un système du 2{sup}`nd` ordre

Le ***coefficient d'amortissement*** ($\zeta$) est un paramètre crucial dans la caractérisation des systèmes du second ordre. Il intervient dans l'équation différentielle du système et joue un rôle significatif dans la stabilité et la dynamique globale du système.

## Observation de l'impact de $\zeta$

Afin de visualiser l'impact de ce coefficient sur la réponse indicielle d'un système du second ordre, veuillez utiliser [ce Jupyter Notebook](https://git.helmo.be/p150077/regulation-cours/-/raw/main/Theory/Seance2/TheorieSeance2_1.ipynb?ref_type=heads&inline=false) et jouez avec $\zeta$ pour répondre au questions ci-dessous.

Pour une utilisation correcte du Jupyter Notebook, veuillez suivre ces étapes :
1. Placez-le dans le dossier nommé `Theory/Seance2` de l'archive que vous avez téléchargée lors de l'installation des outils avant la première séance de laboratoire.
2. Ouvrez l'espace de travail de Visual Studio Code au niveau du dossier `Regulation`.
3. Ouvrez le Jupyter Notebook via l'explorateur de fichiers de Visual Studio Code.
4. Cliquez sur le bouton `Run All` représenté par une double icône `play` ⏩.
5. Sélectionnez, si cela n'est pas fait automatiquement, le *kernel* (c'est-à-dire l'interpréteur) Python à utiliser.

::::{tip}Exercice
:::{note}
Afin de rendre l'exercice intéressant, veuillez le résoudre sur une feuille de papier avant de regarder les réponses.
:::

Pour chacune des valeurs de $\zeta$ suivantes :
* $\zeta < 0$
* $\zeta = 0$
* $0 < \zeta < 1$
* $\zeta = 1$
* $\zeta > 1$

veuillez donner le type de système associé :
* Système sous-amorti
* Système à la limite de la stabilité
* Système sur-amorti
* Système instable
* Système critiquement amorti

:::{dropdown}Réponses
1. $\zeta < 0$ $\Rightarrow$ Système instable
1. $\zeta = 0$ $\Rightarrow$ Système à la limite de la stabilité
1. $0 < \zeta < 1$ $\Rightarrow$ Système sous-amorti
1. $\zeta = 1$ $\Rightarrow$ Système critiquement amorti
1. $\zeta > 1$ $\Rightarrow$ Système sur-amorti
:::

::::

## Compléments aux observations

Pour compléter ce que vous avez observé, on voit sur la [](#2ndOrdre_Zeta) que plus ζ est grand, plus le système est amorti et inversément, plus ζ est faible, plus le système oscille d'où son nom ***coefficient d'amortissement***.

:::{figure} images/Seance2/2ndOrdre_Zeta.png
:label: 2ndOrdre_Zeta
:alt: Réponse indicielle d'un système en fonction de son coefficient d'amortissement
:align: center

Réponse indicielle d'un système en fonction de son coefficient d'amortissement {cite:p}`regu2016`
:::

<!-- TODO: Mettre un lien hypertexte vers le cas présenté à la séance 1 dans le paragraphe qui suit-->
On peut remarquer que si $\zeta >=1$, il n'y a aucune oscillations (on dit que le **système** est ***sur-amorti***) et que les oscillations aparaissent à partir du moment où $\zeta$ est inférieur à 1[^zeta=1]. Ces oscillations sont d'autant plus importantes que $\zeta \rightarrow 0$, ce qui nous permet de déduire que plus $\zeta$ se rapproche de 0, plus le système tend à être instable et si $\zeta = 0$, nous obtenons un système présentant des oscillations entretenues. Autrement dit, lorsque $\zeta = 0$, nous avons un **système** ***à la limite de la stabilité*** (cf. `cas 1` de la démonstration de régulation de position avec l'"horloge" réalisée lors de la première séance théorique). Enfin, par déduction, on devine très vite que si $\zeta < 0$, nous obtenons un sytème dont les oscillations vont être divergentes et donc obtenir un **système** ***instable***.

Vu que la qualité d'un système régulé dépend, entre autres de sa rapidité, nous allons par la suite dimensionner nos systèmes pour qu'ils soient stables sans pour autant qu'ils soient suramortis.

$$\Rightarrow 0<\zeta \leq1 \quad \text{(système sous-amorti)}$$
<!-- TODO: Retirer le nombre (cf. https://mystmd.org/guide/math#disabling-numbering) -->

Nous devons effectivement éviter d'avoir un système suramorti, car, comme le montre la partie droite de l'abaque suivante ([](#abaqueTr5)), le temps de réponse augmente ($\Rightarrow$ rapidité $\searrow$) avec la valeur de $\zeta$. Vous pouvez également vérifier cela en retournant dans le Jupyter Notebook afin de jouer à nouveau avec $\zeta$ et de lire la valeur du temps de réponse à 5% (SettlingTime). Soyez particulièrement attentif·ve autour de la valeur spécifique de $\zeta$ pour laquelle le système se stabilise le plus rapidement dans la plage des 5% autour de sa valeur finale (= point minimum de l'abaque ci-dessous), à savoir : $\zeta = 0.7$.

[^zeta=1]: Un système dont le $\zeta$ est égale à 1 est appelé ***critiquement amorti***.

:::{figure} images/Seance2/abaqueTr5.png
:label: abaqueTr5
:alt: Abaque du temps de réponse à 5% réduit en fonction du coefficient d'amortissement
:align: center

Abaque du temps de réponse à 5% réduit en fonction du coefficient d'amortissement
:::

::::{tip}Question
À ton avis, pourquoi le temps de réponse en fonction du coefficient d'amortissement présente-t-il un comportement en "escalier" à gauche du point minimum ($\zeta=0.7$) et un comportement linéaire à sa droite ?

:::{dropdown}Réponse
Ce comportement en "escalier" est dû aux dépassements de la zone des 5% autour de la valeur atteinte en régime établi. À chaque fois que le système dépasse cette zone, il faut un certain temps pour y retourner ($\Rightarrow$ marche). 

La valeur $\zeta=0.7$ (0.707 plus précisément) correpond à la valeur du coefficient d'amortissement pour laquelle le système est le plus rapide à se stabiliser sans sortir de la plage des 5%. Autrement dit, c'est la valeur à laquelle la réponse indicielle vient tangenter la limite supérieure des 5% au-dessus de la valeur de régime établi sans la dépasser. 

Les valeurs supérieures à celle-ci rende le système plus amorti et donc plus lent, ce qui explique la droite (logarithmique) croissante à la droite du point 0.7.

<!-- TODO: AJouter une image pour expliciter la réponse. -->
:::

::::

# Stabilité d'un système quelconque

Nous avons vu qu'un système du premier ordre n'oscille pas et est par conséquent stable[^stab_casParticulier]. Un du second ordre est plus ou moins amorti ($\Rightarrow$ stable) en fonction de la valeur de son coefficient d'amortissement ($\zeta$). Qu'en est-il pour des systèmes d'ordre supérieur ?

Malheureusement, nous ne connaissont pas les formes canoniques de ces systèmes et il est donc impossible d'identifier leur stabilité à partir de leurs paramètres comme c'est le cas pour des systèmes du second ordre... Heureusement, il existe d'autres outils qui nous permettront de déduire la stabilité plus ou moins grande d'un système ! 🥳

Un de ces outils est le plan de la position des pôles et zéros de la fonction de transfert qui répond sous le doux nom de ***PZMAP***. Celui-ci consiste à représenter les pôles et les zéros d'une fonction de transfert dans le plan complexe (aussi appelé *s-plane*). Afin de comprendre comment cet outil fonctionne, veuillez utiliser [ce Jupyter Notebook](https://git.helmo.be/p150077/regulation-cours/-/raw/main/Theory/Seance2/TheorieSeance2_2.ipynb?ref_type=heads&inline=false) (à placer dans le dossier "Theory/Seance2" avec le précédent et le prochain de cette séance).


[^stab_casParticulier]: En réalité, nous verrons qu'il existe un cas particulier pour lequel ce type de système est instable.

# Précision d'un système

Pour terminer, voyons comment déterminer la précision de notre système. Afin de varier un peu les plaisirs, voici [une vidéo *in english*](https://youtu.be/PXxveGoNRUw) pour vous expliquer comment déterminer la précision d'un système en fonction de sa ***classe*** (*type* en anglais) 🍿

:::{attention}
Il y a deux erreurs écrites dans cette vidéo mais l'auteur les signale et les corrige à l'oral. Celles-ci ont lieu aux instants 7:55 et 11:52.
:::

:::{iframe} https://www.youtube.com/embed/PXxveGoNRUw
:width: 100%
Final Value Theorem and Steady State Error
:::

Afin de compléter les explications données dans la précédente vidéo et pour ceux qui auraient plus de mal avec la langue de Shakespeare, voici la démonstration permettant de trouver les formules nous donnant les valeurs des différents types d'erreur en fonction de la ***classe*** (*type* en anglais) d'un système.

Soit le système asservi à retour unitaire suivant ([](#Sys_retUnitaire_general)) :

<!-- TODO: Modifier la figure et la note pour correspondre aux notation anglophones. -->

:::{figure} images/Seance2/Sys_retUnitaire_general.svg
:label: Sys_retUnitaire_general
:alt: Système à retour unitaire
:align: center

Système à retour unitaire
:::

:::{note}
$G_{BO}$ signifie "Gain en Boucle Ouverte" et $G_{BF}$ signifie "Gain en Boucle Fermée".
:::

On définit l'***erreur*** comme l'**écart entre la sortie obtenue $Y(s)$ et la sortie désirée $R(s)$** :

$$ \varepsilon(s) &= R(s)-Y(s) \\
&= R(s) - R(s)\cdot G_{BF}(s) \\
&= R(s) - R(s)\cdot \frac{G_{BO}(s)}{G_{BO}(s)+1} \\
&= \frac{R(s)}{G_{BO}(s) + 1}$$

Cette formule indique que l'**erreur dépend du type de consigne $R(s)$ et de la fonction de transfert en boucle ouverte $G_{BO}(s)$**.

## Types de consigne

- Consigne de type ***échelon*** (erreur de **degré 0**) : $R(s)=\frac{1}{s}$;
- Consigne de type ***rampe*** (erreur de **degré 1)** : $R(s)=\frac{1}{s^2}$;
- Consigne de type ***parabole*** (erreur de **degré 2**) : $R(s)=\frac{1}{s^3}$;
- ...

De manière générale, on écrira :

$$\boxed{R(s)=\frac{1}{s^{r+1}}} \qquad \text{avec }r\text{ : degr\'{e} d'erreur }(r=0, 1, ...)$$

## Forme canonique de la fonction de transfert en BO

$$G_{BO} &= K\cdot \frac{b_m\cdot s^m+b_{m-1}\cdot s^{m-1}+ \ldots + b_1\cdot s+1}{s^\alpha\cdot (a_n\cdot s^{n-\alpha}+a_{n-1}\cdot s^{n-\alpha-1}+ \ldots +a_1\cdot s+1)} \\
&= K \cdot \frac{B(s)}{s^\alpha \cdot A(s) }$$

Où $\alpha$ représente le nombre de pôles à l'origine que peut comporter la fonction de transfert en BO.

$\alpha$ définit la ***classe*** (*type* en anglais) d'un système.

Autrement dit, l'erreur s'exprime :

$$\varepsilon(s) &= \frac{1}{s^{r+1}}\cdot \frac{1}{1+K \cdot \frac{B(s)}{s^{\alpha} \cdot A(s)}} \\
&= \frac{1}{s^{r+1}}\cdot \frac{s^{\alpha}\cdot A(s)}{s^{\alpha} \cdot A(s) + K \cdot B(s)}$$

Le calcul d'erreur s'obtient en exploitant le théorème de la valeur finale :

$$\lim\limits_{t\to\infty} \varepsilon(t) &= \lim\limits_{s\to0} s \cdot \varepsilon(s) \\
&= \lim\limits_{s\to0} s \cdot \frac{1}{s^{r+1}}\cdot \frac{s^{\alpha}\cdot A(s)}{s^{\alpha} \cdot A(s) + K \cdot B(s)} \\
&= \lim\limits_{s\to0} s^{\alpha-r} \cdot \frac{A(s)}{s^{\alpha} \cdot A(s) + K \cdot B(s)}$$

Les résultats pour les différentes erreurs sont repris dans le tableau ci-dessous ([](#TableauErreurs)), selon le type d'entrée (degré d'erreur : $r$) et la classe ($\alpha$) du système **en Boucle Ouverte** :

<!-- TODO: transformer la figure suivante en tableau -->
:::{figure} images/Seance2/TableauErreurs.png
:label: TableauErreurs
:alt: Tableau des erreurs en fonction de la classe du système
:align: center

Tableau des erreurs en fonction de la classe du système
:::

Afin de vérifier la validité de ces formules en observant les réponses à un échelon et à une rampe d'un système de classe 0 à 2, utilisez [ce Jupyter Notebook](https://git.helmo.be/p150077/regulation-cours/-/raw/main/Theory/Seance2/TheorieSeance2_3.ipynb?ref_type=heads&inline=false) 🧐.

# Fin de la séance

Voilà on y est ! La séance théorique est terminée ! 🥳

On donc vu comment :

- modéliser un système en cascade;
- modéliser un système présentant un retard;
- analyser la ***stabilité*** d'un système à partir de sa fonction de transfert à l'aide de $\zeta$ pour un système du 2nd ordre et/ou via la **position de ses pôles** qu'on peut obtenir facilement via l'outil ***PZMAP*** ([](#pzmap));

    :::{figure} images/Seance2/pzmap.png
    :label: pzmap
    :alt: Impact de la position des pôles d'un système sur sa stabilité
    :align: center

    Impact de la position des pôles d'un système sur sa stabilité
    :::

- analyser la ***précision*** **d'un système à retour unitaire** à partir de sa fonction de transfert à l'aide du nombre de pôles à l'origine qu'elle possède (= ***classe*** du système).

Il est donc temps de commencer à jouer avec ces nouvelles connaissances lors de votre prochain labo afin de pouvoir **identifier un système à partir de ses caractéristiques** ! 🤓

Mais avant cela, je vous propose un [petit test formatif](https://learn-technique.helmo.be/mod/quiz/view.php?id=274863) ($\Rightarrow$ pas besoin de "tricher") pour vérifier votre compréhension 🧐

