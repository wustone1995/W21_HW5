#########################################
##### Name: yuanfeng wu             #####
##### Uniqname: yuanfenw            #####
#########################################

import unittest
import hw5_cards_ec2
import copy

class Testhand(unittest.TestCase):

    def test_q1_remove_pairs(self):
        '''test remove_pairs()

        test that remove_pairs work properly

        Parameters
        -------------------
        None

        Returns
        -------
        None
        '''

        c1 = hw5_cards_ec2.Card(0,1)
        c2 = hw5_cards_ec2.Card(2,10)
        c3 = hw5_cards_ec2.Card(3,13)
        c4 = hw5_cards_ec2.Card(1,1)
        c5 = hw5_cards_ec2.Card(2,5)
        c6 = hw5_cards_ec2.Card(0,13)
        c7 = hw5_cards_ec2.Card(2,1)


        init_cards = [c1, c2, c3]       # test remove pairs when no pairs in hands
        h1 = hw5_cards_ec2.Hand(init_cards)
        h1.remove_pairs()   
        X = h1.init_card
        Y = [c1, c2, c3]
        self.assertIsInstance(X, list)
        self.assertEqual(len(X), len(Y))
        self.assertEqual(','.join([c.__str__() for c in X]),
                         ','.join([c.__str__() for c in Y]))
        

        init_cards = [c1, c2, c3, c4]       # test remove pairs when 1 pairs in hands, 2 of a kind
        h1 = hw5_cards_ec2.Hand(init_cards)
        h1.remove_pairs()
        X = h1.init_card
        Y = [c2, c3]
        self.assertIsInstance(X, list)
        self.assertEqual(len(X), len(Y))
        self.assertEqual(','.join([c.__str__() for c in X]),
                         ','.join([c.__str__() for c in Y]))  

        init_cards = [c1, c2, c3, c4, c7]       # test remove pairs when 1 pairs in hands, 3 of a kind
        h1 = hw5_cards_ec2.Hand(init_cards)
        h1.remove_pairs()
        X = h1.init_card
        Y = [c2, c3, c7]
        self.assertIsInstance(X, list)
        self.assertEqual(len(X), len(Y))
        self.assertEqual(','.join([c.__str__() for c in X]),
                         ','.join([c.__str__() for c in Y]))  

        init_cards = [c1, c3, c4, c6]       # test remove pairs when 2 pairs in hands, 2 of a kind
        h1 = hw5_cards_ec2.Hand(init_cards)  
        h1.remove_pairs()
        X = h1.init_card
        Y = []
        self.assertIsInstance(X, list)
        self.assertEqual(len(X), len(Y))
        self.assertEqual(X, [])  

        init_cards = [c1, c3, c4, c6, c7]       # test remove pairs when 2 pairs in hands, 2 of a kind, 3 of a kind
        h1 = hw5_cards_ec2.Hand(init_cards)  
        h1.remove_pairs()
        X = h1.init_card
        Y = [c7]
        self.assertIsInstance(X, list)
        self.assertEqual(len(X), len(Y))
        self.assertEqual(','.join([c.__str__() for c in X]),
                         ','.join([c.__str__() for c in Y]))

    def test_q2_deal(self):
        '''test deal()

        test that add_card( ) and remove_card( ) behave properly.

        Parameters
        -------------------
        None

        Returns
        -------
        None
        '''

        d1 = hw5_cards_ec2.Deck()
        hands_list = d1.deal(1, -1)           # test: one hand, deal all the cards
        self.assertEqual(len(d1.cards), 0) 
        self.assertEqual(len(hands_list), 1)
        cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = hw5_cards_ec2.Card(suit,rank)
                cards.append(card)
        cards0 = cards[::-1]
        self.assertEqual(len(hands_list[0]), 52)
        self.assertEqual(','.join([c.__str__() for c in hands_list[0]]),
                         ','.join([c.__str__() for c in cards0]))

        d1 = hw5_cards_ec2.Deck()
        hands_list = d1.deal(2, -1)         # test: 2 hands, deal all the cards
        self.assertEqual(len(d1.cards), 0)  
        self.assertEqual(len(hands_list), 2)
        
        cards1 = cards[26:][::-1]
        self.assertEqual(len(hands_list[0]), 26)
        self.assertEqual(','.join([c.__str__() for c in hands_list[0]]),
                         ','.join([c.__str__() for c in cards1]))
        cards2 = cards[:26][::-1]
        self.assertEqual(','.join([c.__str__() for c in hands_list[1]]),
                         ','.join([c.__str__() for c in cards2]))
        
        d1 = hw5_cards_ec2.Deck()
        hands_list = d1.deal(3, -1)         # test: 3 hands, deal all the cards
        self.assertEqual(len(d1.cards), 0)  
        self.assertEqual(len(hands_list), 3)
        cards3 = cards[35:][::-1]
        self.assertEqual(len(hands_list[0]), 17)
        self.assertEqual(','.join([c.__str__() for c in hands_list[0]]),
                         ','.join([c.__str__() for c in cards3]))
        cards4 = cards[18:35][::-1]
        self.assertEqual(len(hands_list[1]), 17)
        self.assertEqual(','.join([c.__str__() for c in hands_list[1]]),
                         ','.join([c.__str__() for c in cards4]))
        cards5 = cards[:18][::-1]
        self.assertEqual(len(hands_list[2]), 18)
        self.assertEqual(','.join([c.__str__() for c in hands_list[2]]),
                         ','.join([c.__str__() for c in cards5]))

        d1 = hw5_cards_ec2.Deck()
        hands_list = d1.deal(3, 3)         # test: 3 hands, 3 cards per hands
        self.assertEqual(len(d1.cards), 43)  
        self.assertEqual(len(hands_list), 3)
        cards3 = cards[49:][::-1]
        self.assertEqual(len(hands_list[0]), 3)
        self.assertEqual(','.join([c.__str__() for c in hands_list[0]]),
                         ','.join([c.__str__() for c in cards3]))
        cards4 = cards[46:49][::-1]
        self.assertEqual(len(hands_list[1]), 3)
        self.assertEqual(','.join([c.__str__() for c in hands_list[1]]),
                         ','.join([c.__str__() for c in cards4]))
        cards5 = cards[43:46][::-1]
        self.assertEqual(len(hands_list[2]), 3)
        self.assertEqual(','.join([c.__str__() for c in hands_list[2]]),
                         ','.join([c.__str__() for c in cards5]))
                    
        d1 = hw5_cards_ec2.Deck()
        hands_list = d1.deal(3, 18)         # test: 3 hands, 18 cards per hands
        self.assertEqual(len(d1.cards), 0)  
        self.assertEqual(len(hands_list), 3)
        cards3 = cards[34:][::-1]
        self.assertEqual(len(hands_list[0]), 18)
        self.assertEqual(','.join([c.__str__() for c in hands_list[0]]),
                         ','.join([c.__str__() for c in cards3]))
        cards4 = cards[16:34][::-1]
        self.assertEqual(len(hands_list[1]), 18)
        self.assertEqual(','.join([c.__str__() for c in hands_list[1]]),
                         ','.join([c.__str__() for c in cards4]))
        cards5 = cards[:16][::-1]
        self.assertEqual(len(hands_list[2]), 16)
        self.assertEqual(','.join([c.__str__() for c in hands_list[2]]),
                         ','.join([c.__str__() for c in cards5]))

if __name__=="__main__":
    unittest.main()


