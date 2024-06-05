---
title: Séance 3
description: Matière centrée sur la représentation fréquentiel de la réponse d'un système.
---

# Objectifs de la séance

Le but de la séance est d'approfondir votre aprentissage de l'analyse du comportement d'un système. Cela se déroulera au fil des étapes suivantes :

- Observations du comportement d'un sytème dans le domaine fréquentiel
- Condition graphique de stabilité d'un système bouclé

# Analyse fréquentielle d'un système

Jusqu'à présent, notre analyse d'un système s'est concentrée sur l'observation de sa réponse indicielle dans le domaine temporel. Cependant, il peut également être intéressant d'analyser cette réponse dans le domaine fréquentiel pour obtenir des informations complémentaires à celles observées dans le domaine temporel. En effet, celle-ci nous permet d'évaluer le dernier critère de performance d'un système régulé : sa robustesse, c'est-à-dire sa capacité à fonctionner correctement malgré une modification plus ou moins importante de son comportement normal (sa fonction de transfert).

Pour analyser cette ***réponse fréquentielle***, nous utiliserons trois outils différents : les diagrammes de ***Bode***, ***Nyquist*** et Black-***Nichols*** qui sont présentés dans [la vidéo suivante](https://youtu.be/QAfk8TuOM68). Celle-ci n'a pas pour but d'entrer dans les détails, mais plutôt de vous montrer à quoi ces diagrammes servent et comment les interpréter. Nous aborderons ensuite la manière de les tracer et, à partir de ces informations, de définir la robustesse de notre système 💪.

:::{iframe} https://www.youtube.com/embed/QAfk8TuOM68
:width: 100%
[Comparaison des graphiques de Nichols, de Nyquist et de Bode](https://youtu.be/QAfk8TuOM68)
:::

# Traçage des diagrammes de Bode et Nyquist

Vous avez pu voir dans la précédente vidéo qu'il existe trois façons de représenter la réponse fréquentielle d'un système, en fonction de vos besoins. Afin de comprendre comment lire ces diagrammes, le mieux encore est de voir comment les construire. Dans le cadre de ce cours, nous n'allons pas nous amuser à redessiner à la main ces différents diagrammes, mais nous utiliserons la puissance de Python pour les tracer. Puisqu'une vidéo vaut mieux qu'un dessin, qui vaut lui-même mieux qu'un long discours, voici deux vidéos présentant la manière de construire le diagramme de Bode et de Nyquist à partir de la fonction de transfert du système à étudier. Nous n'aborderons pas en détails la construction de celui de Black-Nichols, car la vidéo précédente a déjà expliqué comment il est construit à partir de celui de Bode pour afficher directement le gain en fonction de la phase.


## Diagramme de Bode

Comme vous l'avez appris en BAC3, le diagramme de Bode a pour but de représenter le gain et la phase de la réponse d'un système en fonction de sa fréquence. Voici [une vidéo présentant la procédure à suivre pour dessiner ce diagramme à partir d'une fonction de transfert donnée](https://youtu.be/FvvArII7afo) :

:::{iframe} https://www.youtube.com/embed/FvvArII7afo
:width: 100%
[Exemple de tracé de Bode](https://youtu.be/FvvArII7afo)
:::

## Diagramme de Nyquist  

Le diagramme de Nyquist se construit en traçant la courbe qui représente la variation de la réponse en fréquence du système **dans le plan complexe**. Autrement dit, le principe de ce diagramme consiste à remplacer la variable de Laplace "s" par "$j \omega$", de faire varier $\omega$ de $-\infty$ à $+\infty$ de la fonction de transfert **en boucle ouverte** et de tracer les points obtenus dans le plan complexe.

[Une vidéo expliquant la manière de tracer ce diagramme à partir de la fonction de transfert du système étudié](https://youtu.be/lZbUp-ywSq8) sera certainement plus apte à vous faire comprendre cette procédure :

:::{note}
Suivez cette vidéo jusqu'à la fin de l'exercice 2 ($\rightarrow$ 9:37 sur la barre de lecture de la vidéo intégrée).
:::

:::{iframe} https://www.youtube.com/embed/lZbUp-ywSq8
:width: 100%
[Exemple de tracé de Nyquist](https://youtu.be/lZbUp-ywSq8)
:::

Cette vidéo vous a également montré comment déterminer la stabilité du système en suivant les étapes suivantes :

1. Tracer le diagramme de Nyquist de la fonction en boucle ouverte.

2. Compter le nombre $N$ de tours effectués autour du ***point critique "-1"*** par le lieu complet de Nyquist. Utiliser le signe `+` si le parcours est dans le sens trigonométrique, et le signe `-` dans le cas contraire.

3. Déterminer le nombre de pôles instables $P$ par rapport au nombre de zéros dans la partie droite du plan complexe.

4. Vérifier l'équation : $N=P$, qui indique que le **système asservi *à retour unitaire* est stable** si cette équation est vérifiée, et instable sinon.

Rendez-vous au point suivant pour comprendre l'origine de cette équation, appelée ***critère de Nyquist***.

:::{hint}
Si vous souhaitez explorer par vous-même l'impact des pôles et des zéros sur le diagramme de Nyquist, voici un outil qui vous permettra d'assouvir votre soif de compréhension : [Nyquist Criterion (mit.edu)](http://web.mit.edu/jorloff/www/jmoapplets/nyquist/nyquistCrit.html#) 🤓
:::

# Stabilité d'un système dans le domaine fréquentiel

Lorsque l'expression mathématique de la fonction de transfert n'est pas connue, les méthodes algébriques comme le calcul des pôles ne sont pas applicables. De plus, ces critères sont absolus (stabilité ou instabilité) mais ne fournissent pas d'informations sur le degré ou les marges de stabilité avant que le système ne devienne instable.

Si nous disposons seulement d'une connaissance expérimentale du système sous la forme d'un diagramme de Bode ou de Nyquist, nous utilisons un critère graphique pour déterminer la stabilité d'un système bouclé. Ce critère graphique nous permet de prévoir la stabilité en boucle fermée à partir du diagramme de Bode ou de Nyquist de la fonction de transfert en boucle ouverte $G_{BO}(s)$.

Nous connaissons l'expression générale de la fonction de transfert d'un système bouclé à retour unitaire [^retour_unitaire] ([](#SystemeAsservi_SchemaGeneral)):

::::{grid} 1 2 2 2

:::{figure} images/Seance3/SystemeAsservi_SchemaGeneral.svg
:label: SystemeAsservi_SchemaGeneral
:alt: Système à retour unitaire
:width: 400px
:align: left

Système à retour unitaire
:::

$$\boxed{G_{BF}(s)=\frac{G_{BO}(s)}{1 + G_{BO}(s)}}$$

::::

Un système est considéré comme **stable au sens BIBO** (***borned input, borned output***) si tout signal d'entrée borné produit un signal de sortie borné. Il est donc impératif d'éviter que le dénominateur de $G_{BF}(s)$ soit nul, d'où la **condition d'oscillation** :

$$\boxed{G_{BO}(s) = -1}$$

Si un point de $G_{BO}(s)$ passe par -1, cela signifie qu'il existe une **fréquence pour laquelle $|G_{BO}| = 1$ et $\angle{G_{BO}} = -180°$**, conduisant à un signal en sortie ($Y \neq 0$) sans signal à l'entrée ($R=0$). Cette fréquence est appelée la ***fréquence d'oscillation***.

Graphiquement, cela se traduit par l'existence, sur les diagrammes fréquentiels de Bode, de Black-Nichols ou de Nyquist de la fonction de transfert en boucle ouverte $G_{BO}(s)$, d'une fréquence pour laquelle $|G_{BO}| = 1$ et $\angle{G_{BO}} = -180°$.
De là, nous pouvons déduire l'**équation de stabilité dans le diagramme de Nyquist**, présentée au point précédent, comme suit :

> Lorsque dans le plan complexe s, l'image de s décrit une fois le contour de Nyquist dans le sens des aiguilles d'une montre, l'image de $H(s)$ tourne dans le sens trigonométrique autour du point critique d'un nombre de tours égal à $N=P-Z$, où $Z$ est le nombre de zéros de $1+H(s)$ à partie réelle strictement positive et $P$ est le nombre de pôles de $H(s)$ à partie réelle strictement positive. Le système asservi à retour unitaire est asymptotiquement stable à la condition que $Z=0 \Leftrightarrow N=P$.

Autrement dit : 
>Un système continu en boucle fermée à retour unitaire est asymptotiquement stable à la condition nécessaire et suffisante que son lieu de transfert en boucle ouverte, parcouru de $\omega=-\infty$ à $+\infty$, entoure le point critique **-1** dans le sens trigonométrique un nombre de fois égal au nombre de pôles instables de la fonction de transfert en boucle ouverte.

Afin de vérifier ce critère vous-même et d'observer l'impact des paramètres connus d'un système du second ordre sur le comportement de sa réponse fréquentielle dans les trois diagrammes, veuillez télécharger et suivre [ce notebook](https://git.helmo.be/p150077/regulation-cours/-/raw/main/Theory/Seance3/TheorieSeance3_1.ipynb?ref_type=heads&inline=false) (à placer dans un dossier "Seance3" dans le dossier "Theory").

Si vous souhaitez ($\Rightarrow$ facultatif) approfondir votre compréhension de ce critère de stabilité et de la manière dont le diagramme de Nyquist fonctionne, voici [une vidéo supplémentaire qui pourrait vous être utile](https://youtu.be/sof3meN96MA) :

:::{iframe} https://www.youtube.com/embed/sof3meN96MA
:width: 100%
[Critère de stabilité de Nyquist](https://youtu.be/sof3meN96MA)
:::

[^retour_unitaire]: L’étude des systèmes asservis est standardisée avec un **retour unitaire** ce qui est d’ailleurs en pratique le cas, puisque la sortie du processus $y(t)$ est traduite par un capteur en une grandeur $x_r(t)$, image de $y(t)$. C’est en réalité $y(t)$ qui est directement comparée à la consigne $y_e(t)$ qui sera exprimée par son image $x(t)$ par le biais d’une fonction de transfert identique au capteur.

    :::{figure} images/Seance3/RemarqueSystemeAsserviRetourUnitaire.png
    :alt: Système à retour non-unitaire
    :align: center

    Système à retour non-unitaire
    :::
<!-- TODO: La figure de la note de bas de page n'apparaît pas dans la version pdf ! -->

# Marges de stabilité

Nous savons maintenant comment déterminer si un système est stable ou non à partir de sa réponse fréquentielle sur les diagrammes de Bode, Nyquist et Black-Nichols. Cependant, cela se limite, pour le moment, à un statut binaire : stable ou instable. La véritable puissance de ces représentations réside dans leur capacité à évaluer à quel point un système est stable ou non. Cette évaluation de la stabilité d'un système repose sur les marges de stabilité, à savoir : la marge de gain et la marge de phase. Afin de vous expliquer en détail ces concepts, je vous invite à suivre la [vidéo suivante](https://youtu.be/ThoA4amCAX4), qui présente ce que représentent ces marges et comment les mesurer sur les diagrammes de Bode et Nyquist. Encore une fois, vu que le diagramme de Black-Nichols est basé sur celui de Bode, ce qui est expliqué concernant les marges de stabilité pour Bode est directement transposable pour le diagramme de Black-Nichols.

:::{iframe} https://www.youtube.com/embed/ThoA4amCAX4
:width: 100%
[Présentation des marges de phase et de gain](https://youtu.be/ThoA4amCAX4)
:::

# Fin de la séance

Voilà, nous y sommes ! La séance théorique est terminée ! 🥳

Nous avons donc vu :

- Comment représenter la réponse d'un système dans le domaine fréquentiel à l'aide des **diagrammes de Bode, Nyquist, et Nichols**;
- Quels sont les impacts d'un zéro et d'un pôle sur le diagrame de Bode :
    - Un zéro :
        - N'aura pas d'effet sur le module en dessous sa fréquence de coupure $f_c$ ;
        - Provoque une **augmentation** de **+20** dB/décade à partir de $f_c$ ;
        - Présente une phase de 0° avant $f=\frac{f_c}{10}$ et **+90°** après $f=10\cdot f_c$ ;
        - Engendre une rotation de phase de **+45°**/décade entre $f=\frac{f_c}{10}$ et $f=10\cdot f_c$.
    - Un pôle :
        - N'aura pas d'effet sur le module en dessous sa fréquence de coupure $f_c$ ;
        - Provoque une **décroissance** de **-20** dB/décade à partir de $f_c$ ;
        - Présente une phase de 0° avant $f=\frac{f_c}{10}$ et **-90°** après $f=10\cdot f_c$ ;
        - Engendre une rotation de phase de **-45°**/décade entre $f=\frac{f_c}{10}$ et $f=10\cdot f_c$.
    - Un pôle à l'origine :
        - Provoque une **décroissance** de **-20** dB/décade à partir de 0 ;
        - Intersecte l'axe des fréquences lorsque la fréquence vaut 1 (= 100) ;
        - Engendre un déphasage de **-90°**.
- Comment déterminer graphiquement la **stabilité** d'un **système asservi à *retour unitaire* à partir de sa fonction de transfert *en boucle ouverte*** à l'aide du ***critère de Nyquist*** :
    - Sur le ***diagramme de Nyquist*** ([](#CritereNyquist_Nyquist)): le système sera stable si le point critique **-1** est entouré dans le sens trigonométrique un nombre de fois égal au nombre de pôles instables de la fonction de transfert en boucle ouverte. Si celui-ci ne comporte aucun pôle ou zéro à partie réelle positive en boucle ouverte, le critère devient : "le système sera stable si, en parcourant le lieu de transfert de sa fonction de transfert $G_{BO}(s)$ dans le sens des $\omega$ croissants, on laisse le point critique (-1, 0) sur la **gauche**."

        :::{figure} images/Seance3/CritereNyquist_Nyquist.png
        :label: CritereNyquist_Nyquist
        :alt: Stabilité d'un système via le diagramme de Nyquist
        :width: 250px
        :align: center

        Stabilité d'un système via le diagramme de Nyquist
        :::

    - Sur le ***diagramme de Bode*** ([](#CritereNyquist_Bode)): le système sera stable si, lorsque la courbe de phase de sa fonction de transfert $G_{BO}(s)$ passe par -180°, la courbe de gain se trouve en dessous de 0 dB.

        :::{figure} images/Seance3/CritereNyquist_Bode.png
        :label: CritereNyquist_Bode
        :alt: Stabilité d'un système via le diagramme de Bode
        :width: 250px
        :align: center

        Stabilité d'un système via le diagramme de Bode
        :::

    - Sur le ***diagramme de Black-Nichols*** ([](#CritereNyquist_Nichols)): le système sera stable si, en parcourant le lieu de transfert de sa fonction de transfert $G_{BO}(s)$ dans le sens des $\omega$ croissants, on laisse le point critique (-180°, 0 dB) sur la **droite**.

        :::{figure} images/Seance3/CritereNyquist_Nichols.png
        :label: CritereNyquist_Nichols
        :alt: Stabilité d'un système via le diagramme de Black-Nichols
        :width: 250px
        :align: center

        Stabilité d'un système via le diagramme de Black-Nichols
        :::

- Comment déterminer la ***marge de phase*** $\varphi( \omega)$ et la ***marge de gain*** $M( \omega)$ à partir d'un diagramme fréquentiel.


Il est donc temps de commencer à mettre en pratique ces nouvelles connaissances lors de votre troisième laboratoire ! 🤓

<!-- TODO: Ajouter un test de compréhension comme fait pour la séance 2 -->