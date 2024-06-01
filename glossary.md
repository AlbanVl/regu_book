---
title: Glossaire
description: Glossary of terms used throughout the MyST ecosystem.
---

:::{glossary}

[Consigne](https://fr.wikipedia.org/wiki/Consigne)
: Terme utilisé en asservissement et en régulation, ordre donné à un appareil ou à une machine qui se traduit par une valeur à atteindre (ex. : je règle mon four à 200 °C ; dans mon habitation, je « programme » sur le thermostat du système de chauffage la température à une valeur de 17 °C la nuit et 19 °C le jour).

[seuil](http://w3.cran.univ-lorraine.fr/perso/hugues.garnier/Enseignement/Auto/B-Auto-Modelisation.pdf)
: Un système présente un seuil si la sortie n’évolue que lorsque l’entrée dépasse une valeur minimale (seuil). Les seuils ont souvent pour origine des frottements
secs.
    :::{figure} images/Glossary/seuil.png
    :alt: Seuil
    :width: 50%
    :align: center
    :::

[saturation](http://w3.cran.univ-lorraine.fr/perso/hugues.garnier/Enseignement/Auto/B-Auto-Modelisation.pdf)
: Un système présente une saturation lorsque la sortie n’évolue plus au-delà d’une valeur limite. Ces saturations sont dues soit aux limites mécaniques du système (butées) soit aux limites des interfaces de puissance (saturation des amplificateurs opérationnels).
    :::{figure} images/Glossary/saturation.png
    :alt: Saturation
    :width: 50%
    :align: center
    :::

[Hystérésis](http://w3.cran.univ-lorraine.fr/perso/hugues.garnier/Enseignement/Auto/B-Auto-Modelisation.pdf)
: Un système présente une réponse avec une hystérésis lorsque le comportement est différent suivant le sens d’évolution de la variable d’entrée.
    :::{figure} images/Glossary/hysteresis.png
    :alt: Saturation
    :width: 50%
    :align: center
    :::

[Courbure](http://w3.cran.univ-lorraine.fr/perso/hugues.garnier/Enseignement/Auto/B-Auto-Modelisation.pdf)
: La quasi totalité des systèmes présente des courbures plus ou moins prononcées. Dans la plupart des cas le système est approché par une droite passant par l’origine, mais il est aussi possible de linéariser autour d’un point de fonctionnement.
    :::{figure} images/Glossary/courbure.png
    :alt: Saturation
    :width: 50%
    :align: center
    :::

[Linéarisation](http://w3.cran.univ-lorraine.fr/perso/hugues.garnier/Enseignement/Auto/B-Auto-Modelisation.pdf)
: A partir d’un modèle de connaissance établi à partir des lois de la Physique, on peut déterminer une version linéaire approchée par linéarisation des fonctions non-linéaires valable autour du d’un point de fonctionnement pour lequel les signaux d’entrée/sortie du système varient faiblement.
    :::{figure} images/Glossary/linearisation.png
    :alt: Linéarisation
    :width: 50%
    :align: center
    :::

*anti-windup*
: Technique consistant à limiter la saturation du correcteur intégral en empêchant l'accumulation de l'erreur au-delà de certaines limites prédéfinies.