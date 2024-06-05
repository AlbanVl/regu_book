---
title: Séance 6
description: Compléments sur le dimensionnement d'un correcteur et la représentation d'un système.
---

# Objectifs de la séance

Nous avons à présent exploré de nombreux principes de base utiles pour réguler des systèmes SISO (Single Input Single Output), ainsi que les éléments à prendre en compte lors du dimensionnement de systèmes réels.

Cependant, il reste encore un point crucial à considérer lors du dimensionnement d'un système en cascade. De plus, nous devons également observer l'impact qu'a un changement de consigne lorsque celle-ci n'est pas unitaire. Enfin, il n'est pas toujours possible ni nécessaire de modéliser un système. Dans de tels cas, des méthodes heuristiques peuvent être utilisées, et celles-ci seront présentées à la fin de cette séance.

Pour débuter, examinons les problèmes liés à la mise en cascade de systèmes !

# Contrainte de rapidité des systèmes en cascade

La ***régulation en cascade*** d'un système consiste à contrôler la sortie d'un système composé de plusieurs sous-systèmes en série, en agissant sur l'entrée du premier sous-système. Bien que ce type de régulation présente des avantages tels que la simplicité de mise en œuvre et la réduction des perturbations, il comporte également des **inconvénients** tels que la **dégradation des performances** et l'**instabilité**.

Pour rappel, lors de la deuxième séance théorique, nous avons déjà étudié un exemple de système en cascade avec un système de gestion de la position d'un moteur électrique[^demo_horloge] ([](#positionControl_cascadedSystem_S6)) :

:::{figure} images/Seance6/positionControl_cascadedSystem.png
:label: positionControl_cascadedSystem_S6
:alt: Schéma fonctionnel d’un système de contrôle de position en cascade
:align: center

Schéma fonctionnel d’un système de contrôle de position[^positionControl_cascadedSystem_fig]. {cite:p}`åström2021feedback{fig 1.13}`
:::

Les problèmes liés à la régulation en cascade sont principalement dus aux interactions entre les sous-systèmes et aux retards de transmission. En effet, chaque sous-système introduit un déphasage et une atténuation du signal de sortie par rapport au signal d'entrée, ce qui affecte la précision et la rapidité de la régulation. De plus, les retards de transmission entre les sous-systèmes entraînent des décalages temporels entre les actions correctives et les effets observés, ce qui peut provoquer des oscillations ou des divergences du système.

Pour éviter ces problèmes, il est important de choisir soigneusement les paramètres de réglage des régulateurs associés à chaque sous-système, en tenant compte des caractéristiques dynamiques et statiques de l'ensemble du système. Il est donc essentiel de s'assurer que les critères de performance des sous-systèmes sont suffisamment bons pour que le système global ne soit pas perturbé par leur fonctionnement. Reprenant l'exemple ci-dessus de la position d'un moteur électrique, il est nécessaire que la boucle d'asservissement du courant stabilise rapidement le courant par rapport à la boucle de régulation de la vitesse, de sorte que cette dernière ait l'impression que la consigne de courant génère directement le courant souhaité. Il en est de même pour la boucle d'asservissement de la vitesse par rapport à celle de la position.

Cependant, obtenir les performances requises pour chaque sous-système afin d'assurer le bon fonctionnement de l'ensemble du système peut être complexe. Il peut être nécessaire de recourir à des techniques de régulation avancées, telles que la régulation prédictive ou la régulation adaptative, pour améliorer les performances du système. Ces techniques ne seront néanmoins pas abordées dans ce cours.

[^demo_horloge]: cf. démonstration faite faite avec l'"horloge" lors de la première séance de cours.
[^positionControl_cascadedSystem_fig]: Le système dispose de trois boucles en cascade pour le contrôle du courant, de la vitesse et de la position. Chaque boucle a une valeur de référence fournie en externe (indiquée par l’indice 'r') qui définit la valeur nominale de l’entrée à la boucle, qui est ajoutée à la sortie de la boucle externe suivante pour déterminer la valeur commandée pour la boucle (appelée « point de consigne »).

# Saut de consigne à partir d'une consigne quelconque

Nous avons observé à chaque fois le comportement d'un système dont la consigne varie de zéro à 1 ($\rightarrow$ Réponse indicielle). Mais peut-on affirmer que ce comportement est valable pour n'importe quel saut de consigne, tel qu'un passage de 0 à 10 ou même de 10 à 30 ? Vérifions cela ensemble.

Considérons le système suivant :

$$G_{BO}(s) = \frac{6}{2s^2 + 3s +1}$$

$$\Downarrow$$

$$G_{BF}(s) = \frac{\frac{6}{7}}{\frac{2}{7}s^2 + \frac{3}{7}s + 1}$$

Observons sur la [](#ReponseIndicielle) sa ***réponse indicielle*** (0$\rightarrow$1) :

:::{figure} images/Seance6/ReponseIndicielle.png
:label: ReponseIndicielle
:alt: Réponse indicielle
:align: center

Réponse indicielle
:::

Maintenant, examinons la réponse de ce système à un **échelon passant de 0 à 10** ([](#ReponseEchelon_0_10)) :

:::{figure} images/Seance6/ReponseEchelon_0_10.png
:label: ReponseEchelon_0_10
:alt: Réponse à un saut de consigne de 0 à 10
:align: center

Réponse à un saut de consigne de 0 à 10
:::

On remarque que, à part la multiplication par 10 de toutes les valeurs absolues, tout est identique à la réponse à un échelon unitaire. Par conséquent, quel que soit le saut de consigne - que ce soit de $0\rightarrow 1$, $0\rightarrow10$, ou même $0 \rightarrow 273.4$ - les réponses du système restent proportionnellement identiques, avec comme rapport de proportionnalité la valeur du saut de consigne.

Regardons maintenant ce qui se passe si on effectue un saut de consigne de type échelon, **passant d'une valeur comme 10 à une autre valeur comme 30** ([](#ReponseEchelon_10_30)) :

:::{figure} images/Seance6/ReponseEchelon_10_30.png
:label: ReponseEchelon_10_30
:alt: Réponse à un saut de consigne de 10 à 30
:align: center

Réponse à un saut de consigne de 10 à 30
:::

Voici une seconde représentation de la réponse temporelle du système mettant en avant les deux sauts de consigne ([](#ReponseEchelon_0_10_30)) :

:::{figure} images/Seance6/ReponseEchelon_0_10_30.png
:label: ReponseEchelon_0_10_30
:alt: Réponse à un saut de consigne de 0 à 10 suivi d'un saut de 10 à 30
:align: center

Réponse à un saut de consigne de 0 à 10 suivi d'un saut de 10 à 30
:::

Au démarrage, nous observons une valeur de 8.58, correspondant à la valeur statique obtenue pour un échelon passant de 0 à 10. Le reste des valeurs semble également rester identique à celles obtenues lors des deux tests précédents. Cependant, si on y regarde de plus près, la valeur du dépassement a changé ! En effet, nous atteignons une valeur de 30.048, presque égale aux 30 de la consigne, alors qu'en toute logique, nous aurions dû atteindre 32.22 ($=30 \times 1.074$). D'ailleurs, cela se remarque sur la valeur du dépassement relatif qui ne vaut plus que 16.771% $\left(= \frac{30.048-25.732}{25.732}\right)$ contre 25.161% pour les cas précédents.

La raison en est simplement que le saut que nous effectuons en réalité est de 20 ($30-10$) et non de 30. Par conséquent, la valeur du dépassement relatif doit être appliquée à un saut de 20 et non de 30, ce qui donne une valeur absolue à laquelle nous devons ajouter la valeur au démarrage (8.58) pour obtenir la valeur absolue du pic (30.048). Mathématiquement, cela peut s'écrire de la manière suivante :

$$M_{p_{10 \rightarrow 30}} &= y_{ss_{10}} + (1 + OS_{\%}) \cdot (y_{ss_{30}} - y_{ss_{10}}) \\
&= 10 \cdot \frac{6}{7} + 1.25161 \cdot \left(30 \cdot \frac{6}{7} \cdot - 10 \cdot \frac{6}{7}\right) \\
&= 30.0276$$

$$\Downarrow$$
$$OS_{abs_{10 \rightarrow 30}} = M_{p_{10 \rightarrow 30}}-y_{ss_{30}} = 30.0276 - 30 \cdot \frac{6}{7} = 4.3133$$
$$\Downarrow$$
$$OS_{\%_{10 \rightarrow 30}} = \frac{OS_{abs_{10 \rightarrow 30}}}{y_{ss_{30}}} \cdot 100 = \frac{4.3133}{30 \cdot \frac{6}{7}} \cdot 100 = 16.774 \%$$

Les valeurs calculées diffèrent quelque peu des valeurs mesurées en raison du fait que ces dernières sont mesurées et comportent donc des erreurs de mesure, contrairement aux valeurs calculées qui sont exactes.

En résumé, la réponse d'un système à une consigne échelon partant de zéro conserve proportionnellement le même comportement que sa réponse indicielle. Cependant, si la valeur de départ est différente de 0, aucun indicateur de performance ne change, à l'exception de la valeur du dépassement qui suit la règle :

$$OS_{\%_{a \rightarrow b}} = \frac{OS_{abs_{a \rightarrow b}}}{y_{ss_{b}}} \cdot 100$$

avec

$$OS_{abs_{a \rightarrow b}} = M_{p_{a\rightarrow b}}-y_{ss_{b}}$$

Instinctivement, on aurait pu déduire que le dépassement serait plus faible, puisque l'on a tendance à agir ainsi lorsque l'on souhaite effectuer un changement de consigne important en le réalisant par petits sauts plutôt que d'effectuer directement l'intégralité du saut pour éviter les trop grands dépassements (ex: allumage d'un moteur). Vous comprenez maintenant pourquoi vous agissez naturellement de cette manière. 😉

# Méthode heuristiques

En pratique, il n'est pas toujours possible de disposer d'un modèle mathématique fiable du système à réguler, mais seulement de mesures sur celui-ci. Nous avons vu qu'il est possible d'identifier un modèle mathématique à partir de ces mesures, mais cela peut prendre du temps et les critères de performance peuvent ne pas justifier cette démarche, notamment pour des systèmes déjà naturellement stables avec peu de dépassement. Par conséquent, lorsque l'on souhaite réguler rapidement un système, on a recours à des méthodes pragmatiques qui ont fait leurs preuves pour certaines catégories de comportements dynamiques des systèmes asservis (ex: critère de Ziegler-Nichols, de Cohen-Coon, ou celui de Åström-Hägglund). Ces méthodes heuristiques permettent de trouver rapidement des paramètres plus ou moins corrects d'un correcteur PID pour obtenir un fonctionnement acceptable.

Voici une [vidéo présentant l'une de ces techniques](https://youtu.be/uXnDwojRb1g) que je vous invite à essayer sur le simulateur du bras robotique via la commande que vous connaisez maintenant à introduire dans un terminal dans `VS Code` : 

```{code}
voila .\Labo\Seance4\robot_arm\robot_arm.ipynb
```

:::{iframe} https://www.youtube.com/embed/uXnDwojRb1g
:width: 100%
[Critère de stabilité de Nyquist](https://youtu.be/uXnDwojRb1g)
:::

:::{hint}
Si vous désirez en apprendre plus à ce sujet ($\Rightarrow$ non obligatoire), je vous invite à consulter le chapitre 8 de l'ancien [syllabus du cours de régulation de Mme Vetcour](https://learn-technique.helmo.be/mod/resource/view.php?id=248446).
:::

<!-- TODO: Ajouter un test de compréhension comme fait pour la séance 2 -->