class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}!"

    def __str__(self):
        return self.name

    def on_take(self, player_name):
        print(
            f"{player_name} has taken {self.name}! It is a {self.description}. What a find!")

    def on_drop(self, player_name):
        print(
            f"{player_name} has dropped {self.name} onto the floor. Oh well.")

# the child CONSUMES the parent


class LightSource(Item):
    def __init__(self):
        self.name = 'Lamp'  # overriding the default values for name
        # overriding the default values for description
        self.description = 'A bright lamp.'

    def on_drop(self, player_name):
        print(
            f"{player_name} dropped the Lamp. Remember, it's not wise to drop your source of light!")
