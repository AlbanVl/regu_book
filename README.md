# How to compile the files

1. Follow the MyST tool given on the [MyST site](https://mystmd.org/guide/installing)
1. Install InkSkape (problème avec les conversions des svg => doit installer à partir du site de IknSkape et non la version directe d'Ubuntu):
    1. sudo add-apt-repository ppa:inkscape.dev/stable
    1. sudo apt update
    1. sudo apt-get install inkscape=1:1.3.2+202311252150+091e20ef0f~ubuntu22.04.1


# TODO List

- [ ] Gérer les [Subfigures](https://mystmd.org/guide/figures#subfigures) au niveau du pdf.
    Exemple : Seance5:

    Les figure imbriquées sont imbriquées sous forme de figure et non de sous-figures.

    Le latex généré devrait être le suivant :

    ```
    \begin{figure}[!htbp]
    \centering
    \begin{subfigure}
    \centering
    \includegraphics[width=0.7\linewidth]{files/GeneralSimpleFeedbac-5b4b02a1572b03b8e10ce7e4256c9621.png}
    \caption[]{}
    \label{my-figure-a}
    \end{subfigure}
    
    \begin{subfigure}
    \centering
    \includegraphics[width=0.7\linewidth]{files/GeneralSimpleFeedbac-169444c7871d084a515f37dc9aec82e6.png}
    \caption[]{}
    \label{my-figure-b}
    \end{subfigure}
    
    \begin{subfigure}
    \centering
    \includegraphics[width=0.7\linewidth]{files/GeneralSimpleFeedbac-cb7b1f89a0b8757e5e6891793ef0575f.png}
    \caption[]{}
    \label{my-figure-c}
    \end{subfigure}
    
    \begin{subfigure}
    \centering
    \includegraphics[width=0.7\linewidth]{files/GeneralSimpleFeedbac-e6baa06324cd9b3fa55d592e0342e0b7.png}
    \caption[]{}
    \label{my-figure-d}
    \end{subfigure}
    \caption[]{Résolution du système pour $D_{in}$}
    \label{my-figure-d}
    \end{figure}
    ```

- [ ] L'intégration d'une image dans un avertissement (admonition) ne fonctionne pas (Exemple : Seance5, même endroit que le précédent)
