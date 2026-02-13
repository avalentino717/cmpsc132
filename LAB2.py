# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import math

# -------- SECTION 1
class Instructor:
    '''
        >>> t1= Instructor('John Doe')
        >>> t1.get_name()
        'John Doe'
        >>> t1.get_courses()
        []
        >>> t1.add_course('MATH140')
        >>> t1.get_courses()
        ['MATH140']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH141')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH140')
        >>> t1.get_courses()
        ['STAT100']
    '''

    def __init__(self, name):
        #--- YOUR CODE STARTS HERE
        self.name = name
        self.courses = []
        pass

    def get_name(self):
        #--- YOUR CODE STARTS HERE
        return self.name
        pass

    def set_name(self, new_name):
        #--- YOUR CODE STARTS HERE
        if isinstance(new_name, str) and len(new_name) > 0:
            self.name = new_name
        pass

    def get_courses(self):
        #--- YOUR CODE STARTS HERE
        return self.courses
        pass

    def remove_course(self, course):
        #--- YOUR CODE STARTS HERE
        if course in self.courses:
            self.courses.remove(course)
        pass
        
    def add_course(self,course):
        #--- YOUR CODE STARTS HERE
        if course not in self.courses:
            self.courses.append(course)
        pass


# -------- SECTION 2      
class Pantry:
    """"
        >>> sara_pantry = Pantry()                
        >>> sara_pantry.stock_pantry('Bread', 2)
        'Pantry Stock for Bread: 2.0'
        >>> sara_pantry.stock_pantry('Cookies', 6) 
        'Pantry Stock for Cookies: 6.0'
        >>> sara_pantry.stock_pantry('Chocolate', 4) 
        'Pantry Stock for Chocolate: 4.0'
        >>> sara_pantry.stock_pantry('Pasta', 3)     
        'Pantry Stock for Pasta: 3.0'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 3.0}
        >>> sara_pantry.get_item('Pasta', 2)     
        'You have 1.0 of Pasta left'
        >>> sara_pantry.get_item('Pasta', 6) 
        'Add Pasta to your shopping list!'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry = Pantry()                    
        >>> ben_pantry.stock_pantry('Cereal', 2)
        'Pantry Stock for Cereal: 2.0'
        >>> ben_pantry.stock_pantry('Noodles', 5) 
        'Pantry Stock for Noodles: 5.0'
        >>> ben_pantry.stock_pantry('Cookies', 9) 
        'Pantry Stock for Cookies: 9.0'
        >>> ben_pantry.stock_pantry('Cookies', 8) 
        'Pantry Stock for Cookies: 17.0'
        >>> ben_pantry.get_item('Pasta', 2)       
        "You don't have Pasta"
        >>> ben_pantry.get_item('Cookies', 2.5) 
        'You have 14.5 of Cookies left'
        >>> sara_pantry.transfer(ben_pantry, 'Cookies')
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Rice')
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
    """

    def __init__(self):
        self.items = {}
    
    def __repr__(self):
        #--- YOUR CODE STARTS HERE
        return f"I am a Pantry object, my current stock is {self.items}"
        pass

    def stock_pantry(self, item, qty):
        #--- YOUR CODE STARTS HERE
        if item in self.items:
            self.items[item] += float(qty)
        else:
            self.items[item] = float(qty)
        
        return f"Pantry Stock for {item}: {self.items[item]}"
        pass


    def get_item(self, item, qty):
        #--- YOUR CODE STARTS HERE
        if item not in self.items:
            return f"You don't have {item}"
        
        current_stock = self.items[item]

        if qty >= current_stock:
            self.items[item] = 0.0
            return f"Add {item} to your shopping list!"
        
        else:
            self.items[item] -= float(qty)
            return f"You have {self.items[item]} of {item} left"
        pass
    
    def transfer(self, other_pantry, item):
        #--- YOUR CODE STARTS HERE
        if item in other_pantry.items and other_pantry.items[item] > 0:
            transfer_qty = other_pantry.items[item]
            
            self.stock_pantry(item, transfer_qty)
            
            other_pantry.items[item] = 0.0
        pass


# -------- SECTION 3
class Player:
    """
        >>> p1 = Player('Susy')
        >>> print(p1)
        No game records for Susy
        >>> p1.update_loss()
        >>> p1
        *Game records for Susy*
        Total games: 1
        Games won: 0
        Games lost: 1
        Best game: None
        >>> p1.update_win(5)
        >>> p1.update_win(2)
        >>> p1
        *Game records for Susy*
        Total games: 3
        Games won: 2
        Games lost: 1
        Best game: 2 attempts
    """
    def __init__(self, name):
        #--- YOUR CODE STARTS HERE
        self.name = name
        self.wins = 0
        self.losses = 0
        self.best_game = None
        pass

    def update_win(self, att):
        #--- YOUR CODE STARTS HERE
        self.wins += 1
        if self.best_game is None or att < self.best_game:
            self.best_game = att
        pass
    
    def update_loss(self):
        #--- YOUR CODE STARTS HERE
        self.losses += 1
        pass
    

    def __str__(self):
        #--- YOUR CODE STARTS HERE
        total_games = self.wins + self.losses
        if total_games == 0:
            return f"No game records for {self.name}"
        
        best_display = f"{self.best_game} attempts" if self.best_game is not None else "None"
        
        return (f"*Game records for {self.name}*\n"
                f"Total games: {total_games}\n"
                f"Games won: {self.wins}\n"
                f"Games lost: {self.losses}\n"
                f"Best game: {best_display}")
        pass


    __repr__=__str__

class Wordle:
    """
        >>> p1 = Player('Susy')
        >>> p2 = Player('Taylor')
        >>> w1 = Wordle(p1, 'water')
        >>> w2 = Wordle(p2, 'cloud')
        >>> w3 = Wordle(p1, 'jewel')
        >>> w1.play('camel')
        '_A_E_'
        >>> w1.play('ranes')
        'rA_E_'
        >>> w1.play('baner')
        '_A_ER'
        >>> w1.play('pacer')
        '_A_ER'
        >>> w1.play('water')
        'You won the game'
        >>> w1.play('rocks')
        'Game over'
        >>> w1.play('other')
        'Game over'
        >>> w3.play('beast')
        '_E___'
        >>> w3.play('peace')
        '_E__e'
        >>> w3.play('keeks')
        '_Ee__'
        >>> w3.play('jewel')
        'You won the game'
        >>> w2.play('classes')
        'Guess must be 5 letters long'
        >>> w2.play('cs132')
        'Guess must be all letters'
        >>> w2.play('audio')
        '_ud_o'
        >>> w2.play('kudos')
        '_udo_'
        >>> w2.play('would')
        '_oulD'
        >>> w2.play('bound')
        'The word was cloud'
        >>> w2.play('cloud')
        'Game over'
        >>> p1
        *Game records for Susy*
        Total games: 2
        Games won: 2
        Games lost: 0
        Best game: 4 attempts
        >>> p2
        *Game records for Taylor*
        Total games: 1
        Games won: 0
        Games lost: 1
        Best game: None
    """
    max_attempts = 6

    def __init__(self, player, word):
        #--- YOUR CODE STARTS HERE
        self.player = player
        self.word = word.lower()
        self.current_attempts = 0
        self.is_finished = False
        pass
    

    def process_guess(self, guess):
        #--- YOUR CODE STARTS HERE
        if len(guess) != 5:
            return "Guess must be 5 letters long"
        if not guess.isalpha():
            return "Guess must be all letters"
        
        guess = guess.lower()
        feedback = ""
        for i in range(5):
            if guess[i] == self.word[i]:
                feedback += guess[i].upper()
            elif guess[i] in self.word:
                feedback += guess[i].lower()
            else:
                feedback += "_"
        return feedback
        pass


    def play(self, guess):
        #--- YOUR CODE STARTS HERE
        if self.game_over:
            return "Game over"

        # 1. Validate format first (do not count as an attempt)
        if len(guess) != 5:
            return "Guess must be 5 letters long"
        if not guess.isalpha():
            return "Guess must be all letters"

        # 2. Valid format? Increment attempts
        self.attempts_taken += 1
        
        # 3. Check for Win
        if guess.lower() == self.word:
            self.game_over = True
            self.user.update_win(self.attempts_taken)
            return "You won the game"

        # 4. Check for Loss (Ran out of attempts)
        if self.attempts_taken >= Wordle.num_attempts:
            self.game_over = True
            self.user.update_loss()
            return f"The word was {self.word}"

        # 5. Otherwise return feedback
        return self.process_guess(guess)
        pass
       



# -------- SECTION 4
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = line1*4
        >>> line3
        y = 1.825x + 15.1
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> Point2D(45,3) in line5
        False
        >>> Point2D(34,-204) in line5
        True
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
        >>> Point2D(9,5) in line7
        True
        >>> Point2D(89,5) in line7
        True
        >>> Point2D(12,8) in line7
        False
        >>> (9,5) in line7
        False
    '''
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    @property
    def getDistance(self):
        # d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
        dist = math.sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
        return round(dist, 3)

    @property
    def getSlope(self):
        # m = (y2 - y1) / (x2 - x1)
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y
        if dx == 0:
            return float('inf')
        return round(dy / dx, 3)

    @property
    def _getIntercept(self):
        m = self.getSlope
        if m == float('inf'):
            return None
        # b = y - mx
        b = self.p1.y - (m * self.p1.x)
        return round(b, 3)

    def __str__(self):
        m = self.getSlope
        if m == float('inf'):
            return "Undefined"
        
        b = self._getIntercept
        if m == 0:
            return f"y = {float(b)}"
        
        # Handle sign of b for the string representation
        if b == 0:
            return f"y = {m}x"
        sign = "+" if b > 0 else "-"
        return f"y = {m}x {sign} {abs(b)}"

    def __repr__(self):
        # The prompt examples show __repr__ returning the equation string
        return self.__str__()

    def __mul__(self, other):
        if not isinstance(other, int):
            return None
        
        # Create new points with scaled coordinates
        new_p1 = Point2D(self.p1.x * other, self.p1.y * other)
        new_p2 = Point2D(self.p2.x * other, self.p2.y * other)
        return Line(new_p1, new_p2)

    def __contains__(self, point):
        # Ensure 'point' is actually a Point2D instance
        if not isinstance(point, Point2D):
            return False
        
        m = self.getSlope
        if m == float('inf'):
            return False
            
        b = self._getIntercept
        # Check if y is close to mx + b
        return math.isclose(point.y, (m * point.x) + b)



def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Pantry with the name of the class you want to test
    #doctest.run_docstring_examples(Pantry, globals(), name='LAB2',verbose=True)

if __name__ == "__main__":
    run_tests()