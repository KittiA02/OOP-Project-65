class User:
    users = {}
    def __init__(self, username, password, email, user_id):
        self._username = username
        self._password = password
        self._email = email
        self._user_id = user_id
        self._payment_method = []
        self._purchase_history = []
        User.users[self._user_id] = self

    def set_username(self,username):
        self._username = username

    def set_password(self,password):
        self._password = password

    def set_email(self,email):
        self._email = email 

class Admin(User):
    def __init__(self, username, password, email, user_id):
        super().__init__(username, password, email, user_id)

    def add_game(self, name, price, fullprice, discount, discount_end, refund_type, developer, publisher, 
    platform, release_date, feature, edition, specification, description, poster, gameplay_preview):
        #admin adding game to game list
        Game(name, price, fullprice, discount, discount_end, refund_type, developer, publisher,
        platform, release_date, feature, edition, specification, description, poster, gameplay_preview)

    def delete_game(self, game_name):
        del Game.games[game_name]

    def add_user(self, username, password, email, user_id):
        User(username, password, email, user_id)
    
    def delete_user(self, user_id):
        del User.users[user_id]
    
class Game:
    games = {}
    def __init__(self,name, price, fullprice, discount, discount_end, refund_type, developer, publisher, 
    platform, release_date, feature, edition, specification, description, poster, gameplay_preview):
        self._name = name
        self._price = price
        self._fullprice = fullprice
        self._discount = discount
        self._discount_end = discount_end
        self._refund_type = refund_type
        self._developer = developer
        self._publisher = publisher
        self._platform = platform
        self._release_date = release_date
        self._feature = feature
        self._edition = edition
        self._specification = specification
        self._description = description
        self._poster = poster
        self._gameplay_preview = gameplay_preview

        Game.games[self._name] = self

    def set_fullprice(self, fullprice):
        self._fullprice = fullprice

    def set_discount(self, discount):
        self._discount = discount
        self._price = self._fullprice - discount

    def set_discount_end(self, discount_end):
        self._discount_end = discount_end

    def set_refund_type(self, refund_type):
        self._refund_type = refund_type

    def set_developer(self, developer):
        self._developer = developer

    def set_publisher(self, publisher):
       self._publisher = publisher

    def set_platform(self, platform):
        self._platform = platform

    def set_release_date(self, release_date):
       self._release_date = release_date

    def set_feature(self, feature):
        self._feature = feature

    def set_edition(self, edition):
        self._edition = edition

    def set_specification(self,specification):
        self._specification = specification

    def set_description(self, description):
        self._description = description

    def set_poster(self, poster):
        self._poster = poster

    def set_gameplay_preview(self, gameplay_preview):
        self._gameplay_preview = gameplay_preview

class Purchase:
    _purchase_status = False
    def __init__(self, cart):
        self._games = cart._games
        self._total_price = cart.calculate_total()

    def purchase(self):
        if Purchase._purchase_status == False:
            Purchase._purchase_status = True
            print(f"Purchase completed - Total price: ${self._total_price}")

class CreditCard(Purchase):
    def __init__(self, cart, card_number, expiration, cvv, save_status):
        super().__init__(cart)
        self._card_number = card_number
        self._expiration = expiration
        self._cvv = cvv
        self._save_status = save_status

class Paypal(Purchase):
    def __init__(self, cart, save_status):
        super().__init__(cart)
        self._save_status = save_status

class RazorGoldWallet(Purchase):
    def __init__(self, cart):
        super().__init__(cart)
        
class Cart:
    def __init__(self):
        self._games = []

    def add_item(self, game):
        self._games.append(game)

    def remove_item(self, game):
        self._games.remove(game)

    def calculate_total(self):
        total = 0
        for game in self._games:
            total += game._price
        return total
    
class Wishlist:
    def __init__(self):
        self._favs = []

    def add_fav(self, game):
        self._favs.append(game)

    def remove_fav(self, game):
        self._favs.remove(game)

    def add_to_cart(self, cart, game):
        cart.add_item(game)

class Share:
    def __init__(self, media):
        self._media = media

    def share(self):
        print('Share to {}'.format(self._media))

class Report:
    def __init__(self):
        self._report_status = False
    
    def report(self):
        if self._report_status == False:
            self._report_status = True
