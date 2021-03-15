#########################################
##### Name: yuanfeng wu             #####
##### Uniqname: yuanfenw            #####
#########################################

import unittest
import hw5_cards_ec1
import copy

class Testhand(unittest.TestCase):

    def test_q1_construct_hand(self):
        '''test construction of hand

        test if the hand construct properly

        Parameters
        -------------------
        None

        Returns
        -------
        None
        '''
        c1 = hw5_cards_ec1.Card(0,1)
        c2 = hw5_cards_ec1.Card(2,10)
        c3 = hw5_cards_ec1.Card(3,13)
        init_cards = [c1, c2, c3]
        h1 = hw5_cards_ec1.Hand(init_cards)  

        self.assertIsInstance(h1.init_card, list)   # test the attribute init_card of hand is list 
        self.assertEqual(h1.init_card, [c1, c2, c3])  # test the value of attribute init_card  
        self.assertEqual(','.join([c.__str__() for c in h1.init_card]),
                         "Ace of Diamonds,10 of Hearts,King of Spades")

    def test_q2_add_remove(self):
        '''test add and remove method

        test that add_card( ) and remove_card( ) behave properly.

        Parameters
        -------------------
        None

        Returns
        -------
        None
        '''
        c1 = hw5_cards_ec1.Card(0,1)
        c2 = hw5_cards_ec1.Card(2,10)
        c3 = hw5_cards_ec1.Card(3,13)
        init_cards = [c1, c2, c3]
        h1 = hw5_cards_ec1.Hand(init_cards)

        c4 = hw5_cards_ec1.Card(2,10)
        c5 = hw5_cards_ec1.Card(3,10)
        c6 = hw5_cards_ec1.Card(1,5)

        h2 = copy.deepcopy(h1)
        h2.add_card(c4)
        self.assertIsInstance(h2, hw5_cards_ec1.Hand)  # test add: silently fails if the card is already in the hand
        self.assertEqual(','.join([c.__str__() for c in h2.init_card]),
                         "Ace of Diamonds,10 of Hearts,King of Spades") 
        self.assertEqual(len(h2.init_card), 3)

        h2.add_card(c5)
        self.assertIsInstance(h2, hw5_cards_ec1.Hand)  # test add
        self.assertEqual(','.join([c.__str__() for c in h2.init_card]), 
                         "Ace of Diamonds,10 of Hearts,King of Spades,10 of Spades")  
        self.assertEqual(len(h2.init_card), 4) 

        h3 = copy.deepcopy(h1)
        self.assertIsNone(h3.remove_card(c6))  # test remove: return None if the card was not in the Hand
        self.assertIsInstance(h3.remove_card(c4), hw5_cards_ec1.Card)  # test remove: return the card
        self.assertEqual(len(h3.init_card), 2) 

        h4 = copy.deepcopy(h1)
        self.assertEqual(h4.remove_card(c4).__str__(), c4.__str__())  # test remove: return the card

    def test_q3_draw(self):
        '''test draw method

        test that draw( ) behaves properly.

        Parameters
        -------------------
        None

        Returns
        -------
        None
        '''

        c1 = hw5_cards_ec1.Card(0,1)
        c2 = hw5_cards_ec1.Card(2,10)
        c3 = hw5_cards_ec1.Card(3,6)
        init_cards = [c1, c2, c3]
        h1 = hw5_cards_ec1.Hand(init_cards)
        d1 = hw5_cards_ec1.Deck()
        d2 = hw5_cards_ec1.Deck()
        c4 = d2.deal_card()
        h1.draw(d1)
        self.assertEqual(len(h1.init_card), 4)      # test the increasing of hands' length after draw()
        self.assertEqual(len(d1.cards), 51)     # test the side effect
        self.assertEqual(','.join([c.__str__() for c in h1.init_card]),
                         "Ace of Diamonds,10 of Hearts,6 of Spades,King of Spades")


if __name__=="__main__":
    unittest.main()
