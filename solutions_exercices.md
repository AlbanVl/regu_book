---
title: Solutionnaire
description: Solutionnaire d'exercices.
---
(Solutions)=
# Solutionnaire

# Séance théorique n°7

## Exercice de dimensionnement d’un correcteur PID n°1

### Énoncé

Soit le système asservi à retour unitaire dont la fonction de boucle ouverte est :

$$H(s)=\frac{20}{(5+s)(2s+3)(4+3s)}$$

On demande de déterminer le correcteur dont le but est de permettre une erreur statique nulle et une erreur de vitesse minimale, tout en assurant une réponse indicielle dont le dépassement est limité à 5%.

### Stratégie de dimensionnement du correcteur adéquat

Puisqu'on cherche à avoir une erreur statique nulle, la théorie nous dit que le système doit être au moins de classe 1 (cf. [](#TableauErreurs)). Or, il n'y a pas de pôle à l'origine[^pole_dom] donc nous sommes avec un système de classe 0. Il faut dès lors augmenter la classe de notre système, ce qui peut se faire en intégrant ce dernier.

L'erreur de vitesse devant être minimale, il faudra fixer un $K_{BO}$ le plus grand possible vu qu'on obtient un système de classe 1 après l'avoir intégré et que l'erreur de vitesse est égale à $\frac{1}{K_{BO}}$ dans ce cas.

Enfin, on doit limiter le dépassement à 5%, ce qui limitera notre $K$. Le problème est qu'on se retrouve avec un système d'ordre 3 à condition d'utiliser la technique de compensation du pôle dominant pour dimensionner $\tau_I$. Les pôles n'étant pas si différents ($\frac{\tau_1}{\tau_2}<3 \ ou \ 4$), nous ne pouvons pas nous permettre de simplifier le système à un système du second ordre et nous devons donc ajouter un correcteur $D$ par compensation du pôle dominant afin de réduire l'ordre de notre système et ainsi retrouver un système d'ordre 2 dont on connaît la forme canonique et pour lequel nous pouvons donc exploiter la technique de l'identification pour fixer $K$.

[^pole_dom]: Autrement dit, nous ne pouvons pas mettre de pôle en évidence.

### Dimensionnement du correcteur

En mettant la fonction de transfert sous forme canonique, on obtient :

$$H(s)=\frac{\frac{1}{3}}{(\frac{1}{5}s+1)(\frac{2}{3}s+1)(\frac{3}{4}s+1)}$$

Le pôle dominant étant celui lié à la constante de temps $\tau$ la plus grande, nous avons $\tau_1=\frac{3}{4}$ et le second pôle dominant vaut $\tau_2=\frac{2}{3}$.

Dès lors, en appliquant la technique de compensation des pôles dominants, nous pouvons déterminer $\tau_i$ et $\tau_d$ (de la forme série) comme suit :

$$\left\{ \begin{aligned} \begin{array}{ll} \tau_i = \tau_1 = \frac{3}{4} \\ \tau_d = \tau_2 = \frac{2}{3} \end{array} \end{aligned}\right.$$

Nous obtenons donc le correcteur PID suivant :

$$C(s)=K_C \frac{(\frac{3}{4}s+1)\cdot(\frac{2}{3}s+1)}{\frac{3}{4} \cdot s}$$

Ce qui nous donne comme fonction de transfert pour la boucle ouverte :

$$G_{BO}(s) = \frac{K_C\cdot\frac{4}{3} \cdot \frac{1}{3}}{s (\frac{1}{5}s+1)} = \frac{\frac{4}{9} K_C}{\frac{1}{5}s^2+s}$$

La boucle fermée étant à retour unitaire, on obtient :

$$G_{BF}(s) = \frac{\frac{4}{9} K_C}{\frac{1}{5}s^2+s+\frac{4}{9} K_C} = \frac{1}{\frac{9}{20K_C}s^2+\frac{9}{4K_C}s+1}$$

Par identification, on trouve :

$$\left\{ \begin{aligned} \begin{array}{ll} \frac{2\zeta}{\omega_n} = \frac{9}{4K_C} \\ \frac{1}{\omega_n^2} = \frac{9}{20K_C} \end{array} \end{aligned}\right.$$
    
Or,
   
$$OS_{\%_k}=100*e^{-\frac{k\pi\zeta}{\sqrt{1-\zeta^2}}} \Rightarrow 5 = 100*e^{-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}} \Rightarrow \zeta=0.69$$
   
Ce qui nous permet de trouver :
   
$$\left\{ \begin{aligned} \begin{array}{ll} K_C = 5.906 \\ \omega_n = 3.623 \ rad/s \end{array} \end{aligned}\right.$$

Le correcteur PID (sous forme série) qui permet d'assurer un erreur statique nulle, une erreur de vitesse minimum et un dépassement de 5% pour le système donné est donc :

$$C(s)=5.906\frac{(\frac{2}{3}s+1)(\frac{3}{4}s+1)}{\frac{3}{4}s}$$

Notre système ainsi corrigé présente donc bien les caractéristiques souhaitées, à savoir :
    
- une erreur statique nulle : on obtient bien 1 en régime statique lorsqu'on injecte une signal de type échelon unitaire en entrée (cf. [](#S7_Ex1_StepResponse)) ;
- un dépassement de 5% (cf. [](#S7_Ex1_StepResponse) [^step_fct]) ;
- une erreur de vitesse minimale (on ne peut pas avoir une $\varepsilon_v$ plus petite $\Rightarrow$ Kp plus grand sans augmenter le dépassement), à savoir : 38% (cf. [](#S7_Ex1_SpeedError) [^plot_speed_error_fct]).

:::{figure} images/Solutions/S7_Ex1_StepResponse.png
:label: S7_Ex1_StepResponse
:alt: Réponse indicielle du système corrigé
:align: center

Réponse indicielle du système corrigé
:::

:::{figure} images/Solutions/S7_Ex1_SpeedError.png
:label: S7_Ex1_SpeedError
:alt: Erreur de vitesse du système corrigé
:align: center

Erreur de vitesse du système corrigé
:::

<!-- TODO: Faire un lien vers la formule du PID en // une fois qu'elle sera présentée dans le syllabus -->
:::{hint}
La forme parallèle du correcteur PID est la suivante (cf. séance 4) :

$$K_P+\frac{K_I}{s}+K_D \cdot s = 11.156 + \frac{7.875}{s} + 3.937 \cdot s$$
:::

[^step_fct]: Pour pouvoir directement afficher les caractéristiques de performance sur le graphique, vous pouvez ajouter l'option `plot_infos=True` lorsque vous utilisez la fonction `step()` du package `ReguLabFct` 
$\Rightarrow$ `rlf.step(system_to_plot, plot_infos=True)`
[^plot_speed_error_fct]: Pour obtenir ce graphe vous pouvez maintenant directement utiliser la fonction `plot_speed_error()` du package `ReguLabFct` 
$\Rightarrow$ `rlf.plot_speed_error(system_to_plot)`



## Exercice de dimensionnement d’un correcteur PID n°2

Afin de vérifier vos réponses, veuillez consulter le [solutionnaire suivant](https://albanvl.github.io/ReguLaboGramme/regu/LaboSeance7.html#exercice-type-examen).

:::{note}
Les graphes peuvent différer quelque peu par rapport à ce que vous obtenez via votre code car il s'agit d'une ancienne version du package ReguLabFct. Vérifiez juste que vous obtenez bien les mêmes résultats numériques et que les allures de vos différents graphes correspondent.
:::