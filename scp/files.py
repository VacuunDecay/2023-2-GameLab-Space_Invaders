import pygame
import os
import json
from datetime import datetime

from PPlay.window import Window
from scp.text import Text
from scp.tela import Tela

class ScoreKeeper():
    def __init__(self, score, screen):
        self.screen = screen
        self.fileName = "score.json"
        self.input_text = Text("Diga seu nome pro placar: ")
        self.input_text.set_position(50, (self.screen.height/2) - 30)
        self.score = score
        self.running = True

    def add_score(self, name='AAA'):
        name = name[26:]  # Limiting name length to 25 characters
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            'name': name,
            'score': round(self.score),
            'date': now
        }
        with open(self.fileName, 'a') as file:
            json.dump(data, file)
            file.write('\n')


    def update(self):
        pass

    def set_score(self, score):
        self.score = score

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.add_score(self.input_text.text)
                    self.running = False
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text.set_text(self.input_text.text[:-1])
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
                else:
                    self.input_text.set_text(self.input_text.text + event.unicode)
      
    def draw(self):
        self.input_text.draw()

    def __str__(self):
        text = ''
        with open(self.fileName, 'r') as file:
            scores = [json.loads(line) for line in file.readlines()]
            top_scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:5]
            for idx, score in enumerate(top_scores, start=1):
                text += f"{idx}. {score['date']}\n    Name: {score['name']}\n    Score: {score['score']}\n-----------------------------\n"
        text += 'Aperte ENTER para proseguir para o jogo'
        return text
