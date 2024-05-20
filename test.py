import tkinter as tk
from tkinter import messagebox
import random

# Initialiser la fenêtre Tkinter
root = tk.Tk()
root.title("Jeu d'images : Déjà vu ou Nouveau mot")

# Canvas pour afficher l'image
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Charger et stocker les images (supposons qu'elles soient dans un dossier 'images')
image_paths = [f"ressources/images/image_{i}.png" for i in range(2)]
images = [tk.PhotoImage(file=path) for path in image_paths]

# Variables de jeu
seen_images = []
current_image = None
current_image_id = None
score = 0
lives = 3

# Étiquettes pour afficher le score et les vies
score_label = tk.Label(root, text=f"Score: {score}")
score_label.pack()
lives_label = tk.Label(root, text=f"Vies: {lives}")
lives_label.pack()

def update_labels():
    score_label.config(text=f"Score: {score}")
    lives_label.config(text=f"Vies: {lives}")

def show_new_image():
    global current_image, current_image_id
    if random.random() < 0.5 and seen_images:
        # Montrer une image déjà vue
        current_image = random.choice(seen_images)
    else:
        # Montrer une nouvelle image
        current_image = random.choice(images)
        if current_image not in seen_images:
            seen_images.append(current_image)
    
    # Supprimer l'image précédente du canvas
    if current_image_id is not None:
        canvas.delete(current_image_id)
    
    # Afficher la nouvelle image
    current_image_id = canvas.create_image(200, 200, image=current_image)

def deja_vu():
    global score, lives
    if current_image in seen_images:
        score += 1
    else:
        lives -= 1
    update_game()

def nouveau_mot():
    global score, lives
    if current_image not in seen_images:
        score += 1
    else:
        lives -= 1
    update_game()

def update_game():
    global lives
    update_labels()
    if lives <= 0:
        messagebox.showinfo("Game Over", f"Game Over! Your final score is {score}.")
        root.destroy()
    else:
        show_new_image()

# Boutons pour les réponses du joueur
button_frame = tk.Frame(root)
button_frame.pack()

deja_vu_button = tk.Button(button_frame, text="Déjà vu", command=deja_vu)
deja_vu_button.pack(side=tk.LEFT)

nouveau_mot_button = tk.Button(button_frame, text="Nouveau mot", command=nouveau_mot)
nouveau_mot_button.pack(side=tk.RIGHT)

# Commencer le jeu
show_new_image()

# Lancer la boucle principale de Tkinter
root.mainloop()
