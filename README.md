# How to compile the files

1. Follow the MyST tool given on the [MyST site](https://mystmd.org/guide/installing)
1. Install InkSkape (problème avec les conversions des svg => doit installer à partir du site de IknSkape et non la version directe d'Ubuntu):
    1. `sudo add-apt-repository ppa:inkscape.dev/stable`
    1. `sudo apt update`
    1. `sudo apt-get install inkscape=1:1.3.2+202311252150+091e20ef0f~ubuntu22.04.1`

## Generate the pdf version

1. Install the **full** version of Latex : https://www.tug.org/texlive/quickinstall.html ;
1. Generate the pdf via Latex files :
    1. Open a terminal in the main folder ;
    1. `myst build --tex nameOfTheFile.tex` ;
    1. Copy the `correct_latex.py` into the folder containing the Latex files : `cp correct_latex.py _build/exports/nameOfTheFile_tex/` ;
    1. Go into the folder containing the Latex files : `cd _build/exports/nameOfTheFile_pdf_tex/` ;
    1. Run the python file : `python3 correct_latex.py` ;
    1. Run the python file `correct_latex_regu.py` to correct the latex file **for the RegulationBook** : `python3 correct_latex_regu.py` ;
    1. Generate the pdf via Latex : `pdflatex nameOfTheFile.tex` ;

        **NOTE :** To generate the pdf without being stopped : `pdflatex -interaction=nonstopmode nameOfTheFile.tex`
        
    1. Generate the glossary : `makeglossaries main` ;
    1. (Generate the pdf via Latex : `pdflatex nameOfTheFile.tex`.)

        **NOTE :** To generate the pdf without being stopped : `pdflatex -interaction=nonstopmode nameOfTheFile.tex`

    1. Generate the bibliography : `biber main` ;
    1. Generate **2X** the pdf via Latex : `pdflatex nameOfTheFile.tex`.

        **NOTE :** To generate the pdf without being stopped : `pdflatex -interaction=nonstopmode nameOfTheFile.tex`

# TODO List

- [x] Gérer les [Subfigures](https://mystmd.org/guide/figures#subfigures) au niveau du pdf.
    Exemple : Seance5:

    Les figure imbriquées sont imbriquées sous forme de figure et non de sous-figures.

    Le latex généré devrait être le suivant :

    ```
    \begin{figure}[!htbp]
    \centering
    \begin{subfigure}{\textwidth}
    \centering
    \includegraphics[width=0.7\linewidth]{files/GeneralSimpleFeedbac-5b4b02a1572b03b8e10ce7e4256c9621.png}
    \caption[]{}
    \label{my-figure-a}
    \end{subfigure}
    
    \begin{subfigure}{\textwidth}
    \centering
    \includegraphics[width=0.7\linewidth]{files/GeneralSimpleFeedbac-169444c7871d084a515f37dc9aec82e6.png}
    \caption[]{}
    \label{my-figure-b}
    \end{subfigure}
    
    \begin{subfigure}{\textwidth}
    \centering
    \includegraphics[width=0.7\linewidth]{files/GeneralSimpleFeedbac-cb7b1f89a0b8757e5e6891793ef0575f.png}
    \caption[]{}
    \label{my-figure-c}
    \end{subfigure}
    
    \begin{subfigure}{\textwidth}
    \centering
    \includegraphics[width=0.7\linewidth]{files/GeneralSimpleFeedbac-e6baa06324cd9b3fa55d592e0342e0b7.png}
    \caption[]{}
    \label{my-figure-d}
    \end{subfigure}
    \caption[]{Résolution du système pour $D_{in}$}
    \label{my-figure}
    \end{figure}
    ```

- [x] L'intégration d'une image dans un avertissement (admonition) ne fonctionne pas (Exemple : Seance5.2.1)

- [x] L'intégration d'une image dans une note de bas de page ne fonctionne pas (Exemple : Seance3.4)

- [ ] Problème de renvoi vers la figure 4 de la séance 3, section : Stabilité d’un système dans le domaine fréquentiel 
    
    -> Provient du fait d'avoir une figure dans la grille qui n'est pas convertie, ce qui ne marche pas...

- [x] Mettre une image pour marquer la présence d'une vidéo avec le lien hypertexte permmettant d'y aller.

- [ ] Gérer le problème d'affichage des noms des Parts trop longs.

    -> Regarder au niveau du package `avant` dans la partie `FONTS` du fichier Legrand...cls

- [x] Modifier le look des citations pour ressembler à ce qu'on obtient sur le site (cf. Séance 3 section 4).

- [ ] Modifier le style des listes avec des points plutôt que des tirets comme dans le pdf généré de base (ex: Séance 2.3)

- [x] Utiliser le style de listes numérotées avec des lignes entre les points comme dans le pdf généré de base (ex: Séance 2.2)

- [x] Utiliser la police de texte plus fine comme dans le pdf généré de base

- [x] Corriger les références en se basant sur le pdf généré de base (ex: Séance2->Fig2)

- [ ] Insérer le glossaire et acronymes générés dans le fichier `index.tex` pour le mettre dans le `main.tex`
    -> Glossaire : le fichier tex généré ne signale pas les termes repris dans le fichier Markdown...
        {term}`Consigne` -> \Gls{Consigne} ou \gls{Consigne} si minuscule => plsrs formats différents de sorties => analiser la première lettre pour afficher correctement.

- [ ] Insérer les includes générés dans le fichier `index.tex` pour le mettre dans le `main.tex`

- [ ] Améliorer l'affichage de ligne de code (ex : Séance6.4)

- [ ] Note de bas de page dans une légende ne s'affichent pas (ex: Séance2.2)

- [ ] Corriger le renvoi vers un chapitre (ex : Séance 7 vers le Solutionnaire)
    - Ajouter l'instruction `\label{Solutionnaire}` au niveau du titre ;
    - Utiliser l'instruction `\nameref{Solutionnaire}` lors du renvoi au lieu de `\href{/solutions-exercices}{Solutionnaire}`.

- [ ] (Retirer les référence math inutiles (ex: Séance6.3 : Flèches))