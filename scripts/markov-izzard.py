import os
from random import choice


class BotOrDeath():

    @staticmethod
    def read_eddie():
        # izzard_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "izzard.txt")
        text_file = open(izzard_file, 'r')
        chain_dict = BotOrDeath.word_chains(text_file)
        random_text = BotOrDeath.make_random(chain_dict) #[:140]
        text_file.close()
        
        print random_text

    @staticmethod
    def word_chains(source_text):
        content_list = source_text.read().split()

        izzard_dict = {}

        for i in range(len(content_list) - 2):
            izzard_key = (content_list[i], content_list[i + 1])
            next_word = content_list[i + 2]

            if izzard_key not in izzard_dict:
                izzard_dict[izzard_key] = []

            izzard_dict[izzard_key].append(next_word)

        return izzard_dict

    @staticmethod
    def make_random(chains):
        words = []
        random_key = choice(chains.keys())
        words.append(random_key[0])
        words.append(random_key[1])

        while random_key in chains:
            following_word = choice(chains[random_key])

            words.append(following_word)

            random_key = (random_key[1], following_word)

        words_string = " ".join(words)

        return words_string



izzard_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "izzard.txt")

BotOrDeath.read_eddie()
