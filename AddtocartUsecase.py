class Game:
    def __init__(self, name, price, detail):
        self._name = name
        self._price = price
        self._detail = detail

class GameList:
    def __init__(self):
        self._list = []

    def add_to_list(self, game):
        self._list.append(game)

    def __str__(self):
        return '\n'.join(game._name for game in self._list)
    
    def __getitem__(self, index):
        return self._list[index]

class Cart:
    def __init__(self):
        self._cart = []

    def add_game(self, game):
        self._cart.append(game)
        print(f"Added {game._name} to cart.")

    def remove_game(self, game):
        if game in self._cart:
            self._cart.remove(game)
        else:
            print("404 not found")

    def view_cart(self):
        if len(self._cart) == 0:
            print("Your cart is empty.")
        else:
            for game in self._cart:
                print(f"{game._name} - {game._price:.2f} Baht")

    def total_price(self):
        return sum(game._price for game in self._cart)

    
class User:
    def __init__(self, username, password, email):
        self._username = username
        self._password = password
        self._email = email



game1 = Game('Hogwart', 1500, 'Single-player game')
game2 = Game('Skyrim', 1400, 'Single-player game')
game3 = Game('Destiny', 900, 'Multi-player game')

list1 = GameList()

list1.add_to_list(game1)
list1.add_to_list(game2)
list1.add_to_list(game3)

print(list1)

cart1 = Cart()

cart1.add_game(list1[0])
cart1.add_game(list1[1])
cart1.add_game(list1[2])

cart1.remove_game(list1[0])

cart1.view_cart()

print(cart1.total_price())

# sdojgoadhgohe;a
# user1 = User('John', 1234, 'John@gmail.com')
# user2 = User('Tom', 5678, 'Tom@gmail.com')




