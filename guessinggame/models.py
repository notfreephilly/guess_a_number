from django.db import models



# models is a built in ORM feature which django provides
# in this file we created two classes that have different data sets regarding the game

class Player(models.Model):
    username = models.CharField(max_length=100)
    email =  models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    

class GameSession(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    correct_answer = models.IntegerField()
    user_guess = models.IntegerField()
    won = models.BooleanField(default=False)
    attempts = models.IntegerField(default=0)
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Game for {self.player.username} on {self.played_at}"
    




