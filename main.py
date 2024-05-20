#IMPORTS
from tkinter import *
import random
import time

#GLOBALES
global key_verbal_memory 
global key_images_memory 
global key_pattern_memory

key_verbal_memory = False
key_images_memory = False
key_pattern_memory = False

global MVHighestScore
global MIHighestScore
global MPHighestScore
global MIXHighestScore

MVHighestScore = 0
MIHighestScore = 0
MPHighestScore = 0
MIXHighestScore = 0

global coords
coords = (400, 300)

#SCRIPT GENERAL
def script():

  def reset_coords():
    coords = (400, 300)

  #FONCTION DE LA MEMOIRE VERBALE
  def verbal_memory_start():
    reset_coords()
    SeenWords = []

    def restart_mv():
      def mvrestart():
        MVRestartFrame.destroy()
        verbal_memory_start()
      
      def mv_quit():
        MVRestartFrame.destroy()
        script()

      MVFrame.destroy()
      MVRestartFrame = Tk()
      MVRestartFrame.title("Partie Terminée | Mémoire Verbale")
      MVRestartFrame.geometry("600x350")
      MVRestartFrameTitle = Frame(MVRestartFrame, relief=GROOVE)
      MVRestartFrameTitle.pack(side=TOP)
      MVRestartTitleLabel = Label(MVRestartFrameTitle, text="Partie Terminée !", font=("Arial", 20))
      MVRestartTitleLabel.pack()
      MVRestartMainFrame = Frame(MVRestartFrame, relief=GROOVE)
      MVRestartMainFrame.pack(side=TOP)
      score = mvscore.get()
      if score >= 50:
        MVWinLab = Label(MVRestartMainFrame, text=(f"Vous avez gagné ! \n Votre score est de {score}."), font=("Arial", 15))
        MVWinLab.pack(side=TOP)
        MVWinLabSubLab = Label(MVRestartMainFrame, text=(f"Votre meilleur score est {MVHighestScore}!\n Vous obtenez la clé de la Mémoire Verbale !"), font=("Arial", 10))
        MVWinLabSubLab.pack(side=TOP, pady=30)
        cle_verbal_memory = PhotoImage(file="textures/cles/cle_verbal_memory.png")
        CanvaCle = Canvas(MVRestartMainFrame, width=80, height=80)
        CanvaCle.pack(side=TOP)
        CanvaCle.create_image(0, 0, anchor=NW, image=cle_verbal_memory)
        CanvaCle.image = cle_verbal_memory


      else:
        MVLoseLab = Label(MVRestartMainFrame, text=(f"Vous avez perdu ! \n Votre score est de {score}."), font=("Arial", 15))
        MVLoseLab.pack(side=TOP)
        diff = (50 - score)
        MVLoseLabSubLab = Label(MVRestartMainFrame, text=(f"Votre meilleur score est {MVHighestScore}!\n Encore un petit effort, il vous manquait\n {diff} points pour obtenir la clé de Mémoire Verbale"), font=("Arial", 10))
        MVLoseLabSubLab.pack(side=TOP, pady=30)
      MVRestartButtons = Frame(MVRestartFrame, relief=GROOVE)
      MVRestartButtons.pack(side=TOP, pady=10)
      MVRestartButton = Button(MVRestartButtons, text="Recommencer", command=mvrestart, background="aquamarine1")
      MVRestartButton.pack(side=LEFT, padx=20, pady=10)
      MVQuitButton = Button(MVRestartButtons, text="Quitter", command=mv_quit, background="aquamarine1")
      MVQuitButton.pack(side=RIGHT, padx=20, pady=10)



    def MVcheck_vie():
      global mvvies
      if mvvies == 2:
        CanvaVie3.delete(ThreeHearts)
        CanvaVie3.create_image(0, 0, anchor=NW, image=TwoHearts)
        CanvaVie3.pack(side=BOTTOM)
      elif mvvies == 1:
        CanvaVie3.delete(TwoHearts)
        CanvaVie3.create_image(0, 0, anchor=NW, image=OneHeart)
        CanvaVie3.pack(side=BOTTOM)
      elif mvvies == 0:
        restart_mv()


    #Lancement du jeu de mémoir verbale
    def VerbalMemoryStart():
      global mvvies
      global mvcoup
      mvvies = 3
      mvcoup=0
      StartBTN.destroy()
      FrameWord.pack(side=TOP)
      nouveaumotBTN.pack(side=RIGHT, padx=20)
      dejavuBTN.pack(side=LEFT, padx=20)
      mot = choice_mot()
      motVar.set(mot)

    #Fonction pour choisir un mot
    def choice_mot():
      with open("ressources/liste_francais.txt", "r", encoding='utf-8') as fichier:
        dico_FR = fichier.read().splitlines()
        chosen_word = random.choice(dico_FR)
      return chosen_word

    #Fonction si le joueur a cliqué sur le bouton déjà vu
    def check_dejavu ():
      global mvvies
      global mvcoup
      global MVHighestScore
      if mvcoup>0:
        randomizer = random.randint(0,11)
        if motVar.get() in SeenWords:
          score = mvscore.get()
          score += 1
          mvscore.set(score)
          if score >= MVHighestScore:
            print("hello")
            MVHighestScore = score
            mvHighestScore.set(score)
          MVcheckScore()
        else:
          SeenWords.append(motVar.get())
          mvvies -= 1
          MVcheck_vie()

        if randomizer <= 5 or len(SeenWords)<=1:
          mot = choice_mot()
          motVar.set(mot)
        else:
          verif=False
          while verif==False:
            mot = random.choice(SeenWords)
            mot2 = motVar.get()
            if mot!=mot2:
              verif=True
          motVar.set(mot)
        mvcoup+=1
      else:
        mvvies -= 1
        MVcheck_vie()
        mot = choice_mot()
        motVar.set(mot)
        mvcoup+=1

    #Fonction si le joueur a cliqué sur nouveau mot
    def check_nouveau_mot ():
      global mvcoup
      global mvvies
      global MVHighestScore
      if mvcoup>0:
        randomizer = random.randint(0,11)
        if motVar.get() in SeenWords:
          mvvies -= 1
          MVcheck_vie()
        else:
          score = mvscore.get()
          score += 1
          if score >= MVHighestScore:
            print("hello")
            MVHighestScore = score
            mvHighestScore.set(score)
          mvscore.set(score)
          SeenWords.append(motVar.get())
          MVcheckScore()
        if randomizer <= 5 or len(SeenWords)<=1:
          mot = choice_mot()
          motVar.set(mot)
        else:
          verif=False
          while verif==False:
            mot = random.choice(SeenWords)
            mot2 = motVar.get()
            if mot!=mot2:
              verif=True
          motVar.set(mot)
        mvcoup+=1
      else:
        mot = choice_mot()
        motVar.set(mot)
        mvcoup+=1
        score = mvscore.get()
        score += 1
        if score >= MVHighestScore:
          print("hello")
          MVHighestScore = score
          mvHighestScore.set(score)
        mvscore.set(score)
        MVcheckScore()

    #Affiches les règles de la mémoire verbale dans une nouvellle fen^tre
    def MVreglesPrint():
      def MVregles_quit():
        MVregles.destroy()
      MVregles = Tk()
      MVregles.title("Règles | Mémoire Verbale")
      MVregles.geometry("250x200")

      MVreglesText = Label(MVregles, text="Bienvenue dans le jeu Mémoire Verbale \n Les règles de ce jeu sont simples: \n Vous devez indiquer si vous avez déjà \n vu le mot qui apparait grâce \n aux boutons 'Déjà Vu' et \n 'Nouveau Mot'. Vous devez obtenir \n 50 poits pour récupérer la \n clé de l'épreuve. \n Vous pouvez obtenir un \neaster egg si vous parvenez à \nun certain nombre de points. \n Bonne chance !")
      MVreglesText.pack(side=TOP, padx=10, pady=10)

      MVreglesButton = Button(MVregles, text="OK", command=MVregles_quit, background="aquamarine1")
      MVreglesButton.pack(side=BOTTOM, padx=10, pady=10)

      MVregles.mainloop()

    def MVcheckScore():
      if mvscore.get() == 50:
        key_verbal_memory = True
        verbal_memory_reussi()
      if mvscore.get() == 75:
        verbal_memory_hint()

    def verbal_memory_hint():
      def mvindice_quit():
        MVIndice.destroy()

      MVIndice = Tk()
      MVIndice.title("INDICE N°1 |Mémoire Verbale")
      MVIndice.geometry("400x300")

      MVIndiceMainFrame = Frame(MVIndice, borderwidth=1, relief=GROOVE)
      MVIndiceMainFrame.pack(side=TOP)

      MVIndiceText = Label(MVIndiceMainFrame, text="Bravo pour avoir atteint 75 points dans le jeu de mémoire verbale,\n voici un indice pour accéder a une salle secrète:")
      MVIndiceText.pack(side=TOP, padx=5)

      MVIndiceIndice = Label(MVIndiceMainFrame, text="Code césar - partie 1")
      MVIndiceIndice.pack(side=BOTTOM, padx=5, pady= 10)

      MVIndiceButton = Button(MVIndice, text="Quitter", command=mvindice_quit, background="aquamarine1")
      MVIndiceButton.pack(side=BOTTOM)
      MVIndice.mainloop()

    def verbal_memory_reussi():
      def mvreussi_quit():
        MVReussi.destroy()

      MVReussi = Tk()
      MVReussi.title("Réussite | Mémoire Verbale")
      MVReussi.geometry("400x150")

      MVReussiText = Label(MVReussi, text="Bravo, vous avez réussi l'épreuve de mémoire \n verbale et avez obtenu une clé !")
      MVReussiText.pack(side=TOP, padx=15, pady=25)

      MVReussiButton = Button(MVReussi, text="OK", command=mvreussi_quit, background="aquamarine1")
      MVReussiButton.pack(side=BOTTOM, padx=15, pady=15)
      MVReussi.mainloop()


    #TKINTER MEMOIRE VERBALE
    MVFrame = Tk()

    mvHighestScore = IntVar()
    motVar = StringVar()
    mvscore = IntVar()

    MVFrame.title("Mémoire Verbale | Memory Game")
    MVFrame.geometry("600x500")

  
    FrameInfos = Frame(MVFrame, borderwidth=1, relief=GROOVE)
    FrameInfos.pack(side=TOP, padx=5)

    MemoireVerbaleLabel = Label(FrameInfos, text="Mémoire Verbale", font=("Arial",30))
    MemoireVerbaleLabel.pack(padx=5, pady=5)

    MVReglesBTN = Button(FrameInfos, text="Règles", font=("Arial", 10), command=MVreglesPrint, background="aquamarine1")
    MVReglesBTN.pack(side=RIGHT)

    MVScoreLabelTxt = Label(FrameInfos, text="Score :", font=("Arial", 10))
    MVScoreLabelTxt.pack(side=LEFT)
    MVScoreLabel = Label(FrameInfos, textvariable=mvscore, font=("Arial", 10))
    MVScoreLabel.pack(side=LEFT)
    MVHighestScoreLabelTxt = Label(FrameInfos, text="Meilleur Score :", font=("Arial", 10))
    MVHighestScoreLabelTxt.pack(side=LEFT)
    MVHighestScoreLabel = Label(FrameInfos, textvariable=mvHighestScore, font=("Arial", 10))
    MVHighestScoreLabel.pack(side=LEFT)

    FrameJeu = Frame(MVFrame, borderwidth=1, relief=GROOVE)
    FrameJeu.pack(pady=50, padx=10, side=TOP)
    StartBTN = Button(FrameJeu, command=VerbalMemoryStart, text="Commencer")
    StartBTN.pack(side=TOP)



    FrameWord = Frame(FrameJeu, relief=GROOVE)

    CurrentWord = Label(FrameWord, textvariable=motVar, font=("Arial", 15))
    CurrentWord.pack(side=TOP, pady=20)

    dejavuBTN = Button(FrameJeu, text="Déjà Vu", command=check_dejavu, background="azure", font=("Arial", 10))
    nouveaumotBTN = Button(FrameJeu, text="Nouveau Mot", command=check_nouveau_mot, background="azure", font=("Arial",10))

    FrameVie = Frame(MVFrame, borderwidth=1, relief=GROOVE)
    FrameVie.pack(side=BOTTOM, pady=75)
   

    ThreeHearts = PhotoImage(file="textures/vie/3hearts.png")
    TwoHearts = PhotoImage(file="textures/vie/2hearts.png")
    OneHeart = PhotoImage(file="textures/vie/1heart.png")


    CanvaVie3 = Canvas(FrameVie, width=ThreeHearts.width(), height=ThreeHearts.height())
    CanvaVie3.create_image(0, 0, anchor=NW, image=ThreeHearts)
    CanvaVie3.pack(side=BOTTOM)


    mvHighestScore.set(MVHighestScore)

    MVFrame.mainloop()

  #FONCTION MEMOIRE IMAGES
  def images_memory_start():
    reset_coords()
    SeenPics = []
    global current_image, current_image_id
    current_image = None
    current_image_id = None
    coords = (400,300)


    def restart_mi():
      def mirestart():
        MIRestartFrame.destroy()
        images_memory_start()
      
      def mi_quit():
        MIRestartFrame.destroy()
        script()

      MIFrame.destroy()
      MIRestartFrame = Tk()
      MIRestartFrame.title("Partie Terminée | Mémoire des Images")
      MIRestartFrame.geometry("600x350")
      MIRestartFrameTitle = Frame(MIRestartFrame, relief=GROOVE)
      MIRestartFrameTitle.pack(side=TOP)
      MIRestartTitleLabel = Label(MIRestartFrameTitle, text="Partie Terminée !", font=("Arial", 20))
      MIRestartTitleLabel.pack()
      MIRestartMainFrame = Frame(MIRestartFrame, relief=GROOVE)
      MIRestartMainFrame.pack(side=TOP)
      score = miscore.get()
      if score >= 50:
        MIWinLab = Label(MIRestartMainFrame, text=(f"Vous avez gagné ! \n Votre score est de {score}."), font=("Arial", 15))
        MIWinLab.pack(side=TOP)
        MIWinLabSubLab = Label(MIRestartMainFrame, text=(f"Votre meilleur score est {MIHighestScore}!\n Vous obtenez la clé de la Mémoire des Images !"), font=("Arial", 10))
        MIWinLabSubLab.pack(side=TOP, pady=30)
        cle_images_memory = PhotoImage(file="textures/cles/cle_images_memory.png")
        CanvaCle = Canvas(MIRestartMainFrame, width=80, height=80)
        CanvaCle.pack(side=TOP)
        CanvaCle.create_image(0, 0, anchor=NW, image=cle_images_memory)
        CanvaCle.image = cle_images_memory


      else:
        MILoseLab = Label(MIRestartMainFrame, text=(f"Vous avez perdu ! \n Votre score est de {score}."), font=("Arial", 15))
        MILoseLab.pack(side=TOP)
        diff = (50 - score)
        MILoseLabSubLab = Label(MIRestartMainFrame, text=(f"Votre meilleur score est {MIHighestScore}!\n Encore un petit effort, il vous manquait\n {diff} points pour obtenir la clé de Mémoire des Images"), font=("Arial", 10))
        MILoseLabSubLab.pack(side=TOP, pady=30)
      MIRestartButtons = Frame(MIRestartFrame, relief=GROOVE)
      MIRestartButtons.pack(side=TOP, pady=10)
      MIRestartButton = Button(MIRestartButtons, text="Recommencer", command=mirestart, background="aquamarine1")
      MIRestartButton.pack(side=LEFT, padx=20, pady=10)
      MIQuitButton = Button(MIRestartButtons, text="Quitter", command=mi_quit, background="aquamarine1")
      MIQuitButton.pack(side=RIGHT, padx=20, pady=10)



    def MIcheck_vie():
      global mivies
      if mivies == 2:
        CanvaVie3.delete(ThreeHearts)
        CanvaVie3.create_image(0, 0, anchor=NW, image=TwoHearts)
        CanvaVie3.pack(side=BOTTOM)
      elif mivies == 1:
        CanvaVie3.delete(TwoHearts)
        CanvaVie3.create_image(0, 0, anchor=NW, image=OneHeart)
        CanvaVie3.pack(side=BOTTOM)
      elif mivies == 0:
        restart_mi()


    #Lancement du jeu de mémoire des images
    def ImagesMemoryStart():
      global mivies, micoup
      mivies = 3
      micoup=0
      StartBTN.destroy()
      FrameCanvaPic.pack(side=TOP)
      nouvelleimageBTN.pack(side=RIGHT, padx=20)
      dejavuBTN.pack(side=LEFT, padx=20)
      current_path = random.choice(image_chemin)
      current_image = PhotoImage(file=current_path)
      CanvaPic.delete("all")
      current_image_id = CanvaPic.create_image(80, 80, image=current_image, anchor=NW)



    #Fonction pour choisir un mot
    def choice_image():
      global micoup
      randomizer = random.randint(0,11)
      if (randomizer <= 5):
        current_image = random.choice(SeenPics)
      else:
        current_path = random.choice(image_chemin)
        current_image = PhotoImage(file=current_path)
      CanvaPic.delete("current_image_id")
      current_image_id = CanvaPic.create_image(80, 80, image=current_image, anchor=NW)
      CanvaPic.image = current_image

    #Fonction si le joueur a cliqué sur le bouton déjà vu
    def micheck_dejavu ():
      global mivies, micoup, MIHighestScore
      if micoup > 0:
        if current_image in SeenPics:
          score = miscore.get()
          score += 1
          miscore.set(score)
          if score >= MIHighestScore:
            MIHighestScore = score
            miHighestScore.set(score)
          MIcheckScore()
        else:
          SeenPics.append(current_image)
          mivies -= 1
          MIcheck_vie()
        choice_image()
      else:
        mivies -= 1
        MIcheck_vie()
        micoup += 1
        choice_image()



    #Fonction si le joueur a cliqué sur nouvelle image
    def check_nouvelle_image ():
      global micoup, mivies, MIHighestScore
      if micoup > 0:
        if current_image in SeenPics:
          mivies -= 1
          MIcheck_vie()
        else:
          score = miscore.get()
          score += 1
          if score >= MIHighestScore:
            MIHighestScore = score
            miHighestScore.set(score)
          MIcheckScore()
          SeenPics.append(current_image)
        choice_image()
      else:
          score = miscore.get()
          score += 1
          miscore.set(score)
          if score >= MIHighestScore:
            MIHighestScore = score
            miHighestScore.set(score)
          MIcheckScore()
          micoup += 1
          SeenPics.append(current_image)
          choice_image()  

    #Affiches les règles de la mémoire des images dans une nouvellle fen^tre
    def MIreglesPrint():
      def MIregles_quit():
        MIregles.destroy()
      MIregles = Tk()
      MIregles.title("Règles | Mémoire des Images")
      MIregles.geometry("250x200")

      MIreglesText = Label(MIregles, text="Bienvenue dans le jeu Mémoire des Images \n Les règles de ce jeu sont simples: \n Vous devez indiquer si vous avez déjà \n vu l'image qui apparait grâce \n aux boutons 'Déjà Vu' et \n 'Nouvelle Image'. Vous devez obtenir \n 50 poits pour récupérer la \n clé de l'épreuve. \n Vous pouvez obtenir un \neaster egg si vous parvenez à \nun certain nombre de points. \n Bonne chance !")
      MIreglesText.pack(side=TOP, padx=10, pady=10)

      MIreglesButton = Button(MIregles, text="OK", command=MIregles_quit, background="aquamarine1")
      MIreglesButton.pack(side=BOTTOM, padx=10, pady=10)

      MIregles.mainloop()

    def MIcheckScore():
      if miscore.get() == 50:
        key_images_memory = True
        images_memory_reussi()
      if miscore.get() == 75:
        images_memory_hint()

    def images_memory_hint():
      def miindice_quit():
        MIIndice.destroy()

      MIndice = Tk()
      MIndice.title("INDICE N°2 |Mémoire des Images")
      MIndice.geometry("400x300")

      MIIndiceMainFrame = Frame(MIndice, borderwidth=1, relief=GROOVE)
      MIIndiceMainFrame.pack(side=TOP)

      MIIndiceText = Label(MIIndiceMainFrame, text="Bravo pour avoir atteint 75 points dans le jeu de mémoire des images,\n voici un indice pour accéder a une salle secrète:")
      MIIndiceText.pack(side=TOP, padx=5)

      MIIndiceIndice = Label(MIIndiceMainFrame, text="Code césar - partie 2")
      MIIndiceIndice.pack(side=BOTTOM, padx=5, pady= 10)

      MIIndiceButton = Button(MIIndice, text="Quitter", command=miindice_quit, background="aquamarine1")
      MIIndiceButton.pack(side=BOTTOM)
      MIIndice.mainloop()

    def images_memory_reussi():
      def mireussi_quit():
        MIReussi.destroy()

      MIReussi = Tk()
      MIReussi.title("Réussite | Mémoire des Images")
      MIReussi.geometry("400x150")

      MIReussiText = Label(MIReussi, text="Bravo, vous avez réussi l'épreuve de mémoire \n des images et avez obtenu une clé !")
      MIReussiText.pack(side=TOP, padx=15, pady=25)

      MIReussiButton = Button(MIReussi, text="OK", command=mireussi_quit, background="aquamarine1")
      MIReussiButton.pack(side=BOTTOM, padx=15, pady=15)
      MIReussi.mainloop()


    #TKINTER MEMOIRE DES IMAGES
    MIFrame = Tk()

    miHighestScore = IntVar()
    miscore = IntVar()

    image_chemin = []

    for i in range(3):
      image_chemin.append(f"ressources/images/image_{i}.png")



    MIFrame.title("Mémoire des Images | Memory Game")
    MIFrame.geometry("600x500")

  
    FrameInfos = Frame(MIFrame, borderwidth=1, relief=GROOVE)
    FrameInfos.pack(side=TOP, padx=5)

    MemoireImagesLabel = Label(FrameInfos, text="Mémoire des Images", font=("Arial",30))
    MemoireImagesLabel.pack(padx=5, pady=5)

    MIReglesBTN = Button(FrameInfos, text="Règles", font=("Arial", 10), command=MIreglesPrint, background="aquamarine1")
    MIReglesBTN.pack(side=RIGHT)

    MIScoreLabelTxt = Label(FrameInfos, text="Score :", font=("Arial", 10))
    MIScoreLabelTxt.pack(side=LEFT)
    MIScoreLabel = Label(FrameInfos, textvariable=miscore, font=("Arial", 10))
    MIScoreLabel.pack(side=LEFT)
    MIHighestScoreLabelTxt = Label(FrameInfos, text="Meilleur Score :", font=("Arial", 10))
    MIHighestScoreLabelTxt.pack(side=LEFT)
    MIHighestScoreLabel = Label(FrameInfos, textvariable=miHighestScore, font=("Arial", 10))
    MIHighestScoreLabel.pack(side=LEFT)

    FrameJeu = Frame(MIFrame, borderwidth=1, relief=GROOVE)
    FrameJeu.pack(pady=50, padx=10, side=TOP)
    StartBTN = Button(FrameJeu, command=ImagesMemoryStart, text="Commencer")
    StartBTN.pack(side=TOP)



    FrameCanvaPic = Frame(FrameJeu, relief=GROOVE)

    CanvaPic = Canvas(FrameCanvaPic, width=80, height=80, background="pink")
    CanvaPic.pack(side=TOP, pady=20)

    dejavuBTN = Button(FrameJeu, text="Déjà Vu", command=micheck_dejavu, background="azure", font=("Arial", 10))
    nouvelleimageBTN = Button(FrameJeu, text="Nouvelle Image", command=check_nouvelle_image, background="azure", font=("Arial",10))

    FrameVie = Frame(MIFrame, relief=GROOVE)
    FrameVie.pack(side=TOP, pady=25)
   

    ThreeHearts = PhotoImage(file="textures/vie/3hearts.png")
    TwoHearts = PhotoImage(file="textures/vie/2hearts.png")
    OneHeart = PhotoImage(file="textures/vie/1heart.png")


    CanvaVie3 = Canvas(FrameVie, width=ThreeHearts.width(), height=ThreeHearts.height())
    CanvaVie3.create_image(0, 0, anchor=NW, image=ThreeHearts)
    CanvaVie3.pack(side=BOTTOM)


    miHighestScore.set(MIHighestScore)

    MIFrame.mainloop()

  #FONCTION MEMOIRE PATTERNS
  def pattern_start():
    MPFrame = Tk()
    MPFrame.mainloop()
    MPFrame.title("Mémoire de pattern | Mémory Game")
    MPFrame.geometry("800x600")

  #FONCTION MIX
  def mix_start():


    if (key_images_memory == True) and (key_pattern_memory == True) and (key_verbal_memory == True):
      mainFrame.destroy()
      MIXFrame = Tk()
      MIXFrame.mainloop()
      MIXFrame.title("Mémoires Mix | Mémory Game")
      MIXFrame.geometry("800x600")
    else:
      def error_quit():
        Error.destroy()
      Error = Tk()
      
      IntMVHighestScore = IntVar(Error)
      IntMVHighestScore.set(MVHighestScore)
      IntMIHighestScore = IntVar(Error)
      IntMIHighestScore.set(MIHighestScore)
      IntMPHighestScore = IntVar(Error)
      IntMPHighestScore.set(MIHighestScore)

      Error.title("Erreur | Mémoires Mix")
      Error.geometry("450x200")
      ErrorFrame = Frame(Error, borderwidth=1, relief=GROOVE)
      ErrorFrame.pack(side=TOP)
      ErrorLabel = Label(ErrorFrame, text="Erreur, il vous manque au moins une clé pour accéder \n à la salle des épreuves mix.\n Complétez les objectifs suivants pour \n débloquer l'accès à la dernière épreuve:")
      ErrorLabel.pack(padx=10)
      ErrorMessagesFrame = Frame(Error, borderwidth=1, relief=GROOVE)

      ErrorFrameMV = Frame(ErrorMessagesFrame, relief=GROOVE)
      ErrorMVLabel1 = Label(ErrorFrameMV, text="Objectif à compléter pour obtenir la clé de mémoire verbale: (")
      ErrorMVLabel1.pack(side=LEFT)
      ErrorMVLabel2 = Label(ErrorFrameMV, textvariable=IntMVHighestScore)
      ErrorMVLabel2.pack(side=LEFT)
      ErrorMVLabel3 = Label(ErrorFrameMV, text="/ 50 )")
      ErrorMVLabel3.pack(side=LEFT)
      ErrorFrameMV.pack(side=TOP)

      ErrorFrameMI = Frame(ErrorMessagesFrame, relief=GROOVE)
      ErrorMILabel1 = Label(ErrorFrameMI, text="Objectif à compléter pour obtenir la clé de mémoire des images: (")
      ErrorMILabel1.pack(side=LEFT)
      ErrorMILabel2 = Label(ErrorFrameMI, textvariable=IntMIHighestScore)
      ErrorMILabel2.pack(side=LEFT)
      ErrorMILabel3 = Label(ErrorFrameMI, text="/ 50 )")
      ErrorMILabel3.pack(side=LEFT)
      ErrorFrameMI.pack(side=TOP)

      ErrorFrameMP = Frame(ErrorMessagesFrame, relief=GROOVE)
      ErrorMPLabel1 = Label(ErrorFrameMP, text="Objectif à compléter pour obtenir la clé de mémoire des patterns: (")
      ErrorMPLabel1.pack(side=LEFT)
      ErrorMPLabel2 = Label(ErrorFrameMP, textvariable=IntMPHighestScore)
      ErrorMPLabel2.pack(side=LEFT)
      ErrorMPLabel3 = Label(ErrorFrameMP, text="/ 15 )")
      ErrorMPLabel3.pack(side=LEFT)
      ErrorFrameMP.pack(side=TOP)

      ErrorMessagesFrame.pack(pady=15)
      ErrorQuitButton = Button(Error, text="OK", command=error_quit, background="aquamarine1")
      ErrorQuitButton.pack(side=BOTTOM, pady=5)

      Error.mainloop()



  #FONCTION DE DEPLACEMENT
  def deplacement(event):
    global coords
    touche = event.keysym

    if touche == "Up" and coords[1] > 40:
        coords = (coords[0], coords[1] - 20)
    elif touche == "Down" and coords[1] < 540:
        coords = (coords[0], coords[1] + 20)
    elif touche == "Right" and coords[0] < 740:
        coords = (coords[0] + 20, coords[1])
    elif touche == "Left" and coords[0] > 40:
        coords = (coords[0] - 20, coords[1])
    elif touche == "e":
        if (coords[0] == 40 and coords[1] == 300) or (coords[0] == 40 and coords[1] == 280):
            coords = (400,300)
            mainFrame.destroy()
            verbal_memory_start()
        elif (coords[0] == 740 and coords[1] == 300) or (coords[0] == 740 and coords[1] == 280):
            coords = (400, 300)
            mainFrame.destroy()
            pattern_start()
        elif (coords[0] == 400 and coords[1] == 540) or (coords[0] == 380 and coords[1] == 540):
            coords = (400, 300)
            mainFrame.destroy()
            images_memory_start()
        elif (coords[0] == 400 and coords[1] == 40) or (coords[0] == 380 and coords[1] == 40):
            coords = (400, 300)
            mix_start()
    if touche != "e":
        canva_tableau.coords(rectangle, coords[0], coords[1])


    
  ### TKINTER ###


  #TKINTER SALLE PRINCIPALE#
  mainFrame = Tk()
  mainFrame.title("Memory Game | Thomas & Gabriel")
  mainFrame.geometry("800x600")


  canva_tableau = Canvas(mainFrame, width=800, height=600, bg="green")


  MapPixelArt = PhotoImage(file="textures/map_pixelart.png")
  canva_tableau.create_image(0, 0, anchor=NW, image=MapPixelArt)

  sprite = PhotoImage(file="textures/sprite.png")
  rectangle = canva_tableau.create_image(400, 300, image=sprite, anchor=NW)

  canva_tableau.focus_set()
  canva_tableau.bind("<Key>", deplacement)

  canva_tableau.pack()


  mainFrame.mainloop()

def startGame():
  def credits():
    def credits_quit():
      credits.destroy()
    credits = Tk()
    credits.title("Crédits | Memory Game")
    credits.geometry("400x300")
    creditsTitleFrame = Frame(credits, relief=GROOVE)
    creditsTitleFrame.pack(side=TOP)
    creditsTitleLabel = Label(creditsTitleFrame, text="Memory Game \n Crédits", font=("Arial", 15))
    creditsTitleLabel.pack()
    creditsTextFrame = Frame(credits, relief=GROOVE)
    creditsTextFrame.pack(fill=BOTH, expand=True)
    creditsText = Text(creditsTextFrame,   font=("Arial", 10), wrap=WORD)
    creditsText.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbarCredits = Scrollbar(creditsTextFrame, orient=VERTICAL, command=creditsText.yview)
    scrollbarCredits.pack(side=RIGHT, fill=Y)
    
    creditsText.tag_configure("center", justify='center')

    creditsText.insert(END, "Le jeu 'Memory Game' a été réalisé par\n","center")
    creditsText.insert(END, "Thomas KELEMEN & Gabriel CADEAU-FLAUJAT,\n","center")
    creditsText.insert(END, "deux élèves de première NSI, passionnés par coder les idées de programmes leur passant par la tête.\n","center")
    creditsText.insert(END, "Le jeu 'Memory Game' a été inspiré de la plateforme de jeu 'Human Benchmark'.\n","center")
    creditsText.insert(END, "\n","center")
    creditsText.insert(END, "Développement :\n","center")
    creditsText.insert(END, "'Memory Game' a été développé entierement par Thomas KELEMEN et Gabriel CADEAU-FLAUJAT.\n","center")
    creditsText.insert(END, "\n","center")
    creditsText.insert(END, "Textures :\n","center")
    creditsText.insert(END, "Les texture de la map et des clés ont été réalisées par\n Gabriel CADEAU-FLAUJAT.\n","center")
    creditsText.insert(END, "Certaines textures, libres de droits vienent du site de ressources 'OpenGameArt'.\n","center")
    creditsText.insert(END, "\n","center")
    creditsText.insert(END, "Remerciements :\n","center")
    creditsText.insert(END, "Un grand merci à Cédric ESCOUTE, professeur de NSI, sans qui le projet n'aurait pas pu voir le jour.\n","center")
    creditsText.insert(END, "Merci à Quentin PLADEAU, qui a aidé sur l'aspect programmation du projet.\n","center")
    creditsText.insert(END, "\n","center")
    creditsText.insert(END, "Informations supplémentaires :\n","center")
    creditsText.insert(END, "'Memory Game' est un jeu programmé entièremment dans le language de programmation Python.\n","center")
    creditsText.insert(END, "L'aspect graphique du jeu a été assuré par al librairie Tkinter, native à Python\n","center")
    creditsText.insert(END, "\n","center")
    creditsText.insert(END, "'Memory Game' est un jeu soumis aux droits d'auteurs et est soumis à la propriété intellectuelle de\n","center")
    creditsText.insert(END, "Thomas KELEMEN et Gabriel CADEAU-FLAUJAT\n","center")
    creditsText.insert(END, "Ce jeu est destiné à un usage personnel et non commercial. Vous pouvez le partager avec des amis et des proches, mais toute distribution à des fins commerciales est strictement interdite sans autorisation préalable.\n","center")
    creditsText.insert(END, "En utilisant ce jeu, vous acceptez de vous conformer à toutes les lois et réglementations en vigueur en France concernant les droits d'auteur, la propriété intellectuelle et toute autre loi applicable.\n \n","center")

    creditsText.config(state=DISABLED)

    creditsQuitButton = Button(creditsText, text="OK", command=credits_quit, background="aquamarine1")

    def check_scroll(*args):
      creditsText.update_idletasks()
      # Obtenir la position actuelle de la scrollbar
      position = creditsText.yview()
      # Si la scrollbar est tout en bas (pos[1] == 1.0)
      if position[1] == 1.0:
          # Insérer le bouton si ce n'est pas déjà fait
          if not creditsQuitButton.winfo_ismapped():
              creditsText.window_create(END, window=creditsQuitButton, padx=185)
      else:
          # Supprimer le bouton si la scrollbar n'est pas tout en bas
          if creditsQuitButton.winfo_ismapped():
              creditsQuitButton.place_forget()

    creditsText.config(yscrollcommand=lambda *args: (scrollbarCredits.set(*args), check_scroll(*args)))

    credits.mainloop()


  def regles():
    def regles_quit():
      regles.destroy()
    regles = Tk()
    regles.title("Règles | Memory Game")
    regles.geometry("400x300")
    reglesTitleFrame = Frame(regles, relief=GROOVE)
    reglesTitleFrame.pack(side=TOP)
    reglesTitleLabel = Label(reglesTitleFrame, text="Memory Game \n Règles", font=("Arial", 15))
    reglesTitleLabel.pack()
    reglesTextFrame = Frame(regles, relief=GROOVE)
    reglesTextFrame.pack(fill=BOTH, expand=True)
    reglesText = Text(reglesTextFrame,   font=("Arial", 10), wrap=WORD)
    reglesText.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbarRegles = Scrollbar(reglesTextFrame, orient=VERTICAL, command=reglesText.yview)
    scrollbarRegles.pack(side=RIGHT, fill=Y)
    
    reglesText.tag_configure("center", justify='center')

    reglesText.insert(END, "Le jeu 'Memory Game' a été réalisé par\n","center")
    reglesText.insert(END, "Thomas KELEMEN & Gabriel CADEAU-FLAUJAT,\n","center")
    reglesText.insert(END, "deux élèves de première NSI, passionnés par coder les idées de programmes leur passant par la tête.\n","center")
    reglesText.insert(END, "\n","center")
    reglesText.insert(END, "Règles générales :\n","center")
    reglesText.insert(END, "'Memory Game' est un jeu composé de quatre salles, chacune d'elle représentant une épreuve.\n","center")
    reglesText.insert(END, "Ces épreuves sont:\n -La Mémoire Verbale (à gauche)\n -La Mémoire des Images (en bas)\n -La Mémoire des Patterns (à droite)\n -Les Mémoires Mix (en haut)","center")
    reglesText.insert(END, "Les règles de chacune de ses épreuves sont disponibles quand vous y accédez.\n","center")
    reglesText.insert(END, "\n","center")
    reglesText.insert(END, "Salle Principale :\n","center")
    reglesText.insert(END, "La salle principale est une salle libre dans laquelle vosu pouvez vous déplacer pour accéder aux différentes épreuves.\n","center")
    reglesText.insert(END, "Chacune des portes correspond à une épreuve différente.\n","center")
    reglesText.insert(END, "\n","center")
    reglesText.insert(END, "Contrôles :\n","center")
    reglesText.insert(END, "Afin de vous déplacer dans la salle principale, utilisez les flèches de votre clavier.\n","center")
    reglesText.insert(END, "Pour entrer dans les différentes salles, utilisez la touche 'e'.\n","center")
    reglesText.insert(END, "Dans les salles d'épreuves, utilisez la souris pour vous déplacer et le clique gauche pour intéragir avec les différents éléments\n","center")
    reglesText.insert(END, "\n","center")
    reglesText.insert(END, "Easter Egg :\n","center")
    reglesText.insert(END, "Des Easter Eggs sont dissimulés dans le jeu, soyez attentifs pour essayer de tous les trouver.\n","center")
    reglesText.insert(END, "Note: Vous pouvez utiliser les différents fichiers Python mis à votre disposition\n","center")
    reglesText.insert(END, "\n","center")
    reglesText.insert(END, "Accès à la salle MIX:\n","center")
    reglesText.insert(END, "Afin d'accéder à la salle finale du jeu, vous aurez besoin d'obtenir un certain score dans les trois autres épreuves:\n","center")
    reglesText.insert(END, "-Mémoire Verbale: 50 Points\n -Mémoire des Images: 50 Points\n -Mémoire des Patterns: 15 Points \n","center")
    reglesText.insert(END, "\n \n","center")
    
    reglesText.config(state=DISABLED)

    reglesQuitButton = Button(reglesText, text="OK", command=regles_quit, background="aquamarine1")

    def check_scroll(*args):
      reglesText.update_idletasks()
      # Obtenir la position actuelle de la scrollbar
      position = reglesText.yview()
      # Si la scrollbar est tout en bas (pos[1] == 1.0)
      if position[1] == 1.0:
          # Insérer le bouton si ce n'est pas déjà fait
          if not reglesQuitButton.winfo_ismapped():
             reglesText.window_create(END, window=reglesQuitButton, padx=185)
      else:
          # Supprimer le bouton si la scrollbar n'est pas tout en bas
          if reglesQuitButton.winfo_ismapped():
              reglesQuitButton.place_forget()

    reglesText.config(yscrollcommand=lambda *args: (scrollbarRegles.set(*args), check_scroll(*args)))

    regles.mainloop()

  def launcher():
    StartFenetre.destroy()
    script()

  StartFenetre = Tk()
  StartFenetre.title("Memory Game | Thomas & Gabriel")
  StartFenetre.geometry("750x350")

  StartTitleFrame = Frame(StartFenetre, borderwidth=1, relief=GROOVE)
  StartTitleFrame.pack(side=TOP,padx=10, pady=10)
  StartTitleLabel = Label(StartTitleFrame, text="Bienvenue dans le jeu \n 'Memory Game'", font=("Arial", 20))
  StartTitleLabel.pack(side=TOP)
  StartSubtitleLabel = Label(StartTitleFrame, text="Un jeu par Thomas KELEMEN et Gabriel CADEAU-FLAUJAT", font=("Arial", 15))
  StartSubtitleLabel.pack(side=TOP)

  LicenseLabel = Label(StartFenetre, text="Memory Game, Thomas KELEMEN & Gabriel CADEAU-FLAUJAT \n © Tous droits réservés. 2024 ")
  LicenseLabel.pack(side=BOTTOM)
  StartButtonsFrame = Frame(StartFenetre, borderwidth=1, relief=GROOVE)
  StartButtonsFrame.pack(padx=10, pady=10)
  StartButtonsFrameTop = Frame(StartButtonsFrame, relief=GROOVE)
  StartButtonsFrameTop.pack(side=TOP, padx=5, pady=5)
  StartButtonsFrameBottom = Frame(StartButtonsFrame, relief=GROOVE)
  StartButtonsFrameBottom.pack(side=BOTTOM, padx=5, pady=5)

  StartBtn = Button(StartButtonsFrameBottom, text="COMMENCER", font=("Arial", 10), command=launcher, background="aquamarine1")
  StartBtn.pack()

  CreditsBtn = Button(StartButtonsFrameTop, text="Crédits", command=credits, font=("Arial", 10), background="aquamarine3")
  CreditsBtn.pack(side=LEFT, pady=10, padx=25)

  ReglesBtn = Button(StartButtonsFrameTop, text="Règles", command=regles, font=("Arial", 10), background="aquamarine3")
  ReglesBtn.pack(side=RIGHT, pady=10, padx=25)


  StartFenetre.mainloop()

startGame()