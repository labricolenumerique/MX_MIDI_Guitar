# MX MIDI Guitar
[Adafruit MX MIDI Guitar](https://learn.adafruit.com/mx-midi-guitar)

![Guitar](https://cdn-learn.adafruit.com/assets/assets/000/089/544/thumb160/3d_printing_hero-controllers.jpg?1584538832)

## Présentation

Inspiré par le tristement célèbre contrôleur Guitar Hero, ce projet transforme un contrôleur MIDI en une guitare imprimée en 3D. Doté de 12 interrupteurs Cherry MX dans le manche, il procure une sensation tactile satisfaisante. La barre whammy permet de modifier la hauteur de la note, ce qui donne l'impression d'une guitare électrique. Il est également doté d'un mode "strumming" qui vous permet d'enchaîner les accords et les notes, vous offrant ainsi un style de jeu différent de celui des contrôleurs MIDI classiques. Grâce à l'accéléromètre, vous pouvez déplacer la guitare pour ajuster la modulation, ce qui vous donne un style de jeu expressif.

Ce projet est codé en CircuitPython et utilise la [bibliothèque USB MIDI](https://docs.circuitpython.org/projects/midi/en/latest/api.html). Il propose des fonctions de vélocité, de modulation, de pitch bending et d'activation/désactivation des notes. Il dispose de 8 jeux de notes différents pour jouer des octaves différentes ou des jeux de notes pour créer vos propres accords. Deux interrupteurs vous permettent d'activer différentes fonctions telles que le mode strum, le mode trigger et le mode accéléromètre. Deux potentiomètres permettent d'ajuster la vélocité et la modulation.

Les pièces sont imprimées en 3D sans aucun matériau de support. Les parties supérieure et inférieure du corps de la guitare s'emboîtent pour faciliter l'ouverture et la fermeture. Les pièces sont conçues pour être imprimées sur la plupart des imprimantes 3D avec un volume de construction de 250x210x200mm. Les pièces et les composants sont fixés ensemble avec des vis de type M3. Les fichiers de conception sont open source et peuvent être téléchargés gratuitement. Les fichiers CAO présentent un assemblage paramétrique permettant d'ajouter/modifier facilement pour créer un contrôleur personnalisé.

Les interrupteurs MX sont disponibles en différents types et styles. La couleur des 
### Vidéos

  * @adafruit: [MIDI Guitar #3DPrinting](https://www.youtube.com/watch?v=BDwOBYsL71Q)
  * @BlitzCityDIY: [MIDI Guitar 🎸](https://www.youtube.com/watch?v=q6v2C1idLWU)

https://cdn-learn.adafruit.com/assets/assets/000/089/544/thumb160/3d_printing_hero-controllers.jpg?1584538832
## Préparation

### Composants

### Electronique
**Composants nécéssaires**
 * [Adafruit Grand Central M4 Express featuring SAMD51](https://www.digikey.fr/en/products/detail/adafruit-industries-llc/4084/10107217)
 * [Adafruit LIS3DH Triple-Axis Accelerometer](https://www.digikey.fr/en/products/detail/adafruit-industries-llc/2809/5774319)
 * [Mini 8-Way Rotary Selector Switch - SP8T](https://www.digikey.fr/en/products/detail/adafruit-industries-llc/2925/17282424)
 * Potentiometer with Built In Knob - 10K ohm
 * Panel Mount 10K potentiometer
 * Mini Panel Mount SPDT Toggle Switch
 * Micro Switch w/Lever - 2 Terminal
 * Panel Mount Extension USB Cable - Micro B Male to Micro B Female
 * USB A to Micro B Cable - 2 meter long

### Impression 3D

 * [Pièces imprimées en 3D](https://learn.adafruit.com/mx-midi-guitar/3d-printing)

## Assemblage

### Câblage

Le [diagramme](https://learn.adafruit.com/mx-midi-guitar/circuit-diagram) fournit une référence visuelle pour le câblage des composants.

* Câblage de l'[accéléromètre à trois axes](https://learn.adafruit.com/mx-midi-guitar/install-the-lis3dh)
* Câblage de l'[interrupteur à 8 voies]( https://learn.adafruit.com/mx-midi-guitar/wiring-8-way-switch)
* Câblage des [potentiomètres](https://learn.adafruit.com/mx-midi-guitar/wiring-pots)
* Câblage des [commutateurs](https://learn.adafruit.com/mx-midi-guitar/wiring-toggle-switches)
* Câblage des [touches MX](https://learn.adafruit.com/mx-midi-guitar/wiring-mx-switches)

### Assemblage des éléments

 * Tête du manche
   * [Assemblage de la tête du manche](https://learn.adafruit.com/mx-midi-guitar/neck-head-assembly)
   * [Assemblage de la façade de la tête du manche](https://learn.adafruit.com/mx-midi-guitar/head-cover-assembly)
   * [Assemblage du bandeau LED](https://learn.adafruit.com/mx-midi-guitar/strip-assembly)
 * Caisse
   * [Assemblage de la caisse](https://learn.adafruit.com/mx-midi-guitar/body-assembly)
   * [Assemblage de la caisse](https://learn.adafruit.com/mx-midi-guitar/body-assembly)
   * [Assemblage du Strum](https://learn.adafruit.com/mx-midi-guitar/strum-assembly)
   * [Assemblage de la barre whammy](https://learn.adafruit.com/mx-midi-guitar/whammy-assembly)
   * [Assemblage des composants sur les panneaux](https://learn.adafruit.com/mx-midi-guitar/panel-mount-components)
   * [Assemblage carte centrale](https://learn.adafruit.com/mx-midi-guitar/assemble-grand-central)
 * [Assemblage final](https://learn.adafruit.com/mx-midi-guitar/final-assembly)

## Programmation

  * Tutoriel de la carte Grand Central M4 Express: [Introducing the Adafruit Grand Central M4 Express](https://learn.adafruit.com/adafruit-grand-central)


### Code

  * [Dépôt Git](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/MX_MIDI_Guitar/code.py)

  * Brancher la carte **Grand Central M4 Express** au PC
  * Télécharger CircuitPython sur la page [Grand Central M4 Express](https://circuitpython.org/board/grandcentral_m4_express)
  * Installer circuit 
  * Télécharger le [code.py](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/MX_MIDI_Guitar/code.py)
  * Copier le fichier code.py sur le lecteur de disque de la carte

### Fonctionnement
**Fonctionnement du code**
 * [Code Walkthrough](https://learn.adafruit.com/mx-midi-guitar/code-walkthrough)

## Utilisation

 * Item 1
