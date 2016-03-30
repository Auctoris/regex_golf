from __future__ import print_function
import re

def words(text): 
    return set(text.split())

animal = words('''alligator ant bear bee bird camel cat cheetah chicken chimpanzee cow crocodile deer dog dolphin duck eagle elephant fish fly fox frog giraffe goat goldfish
                hamster hippopotamus horse kangaroo kitten lion lobster monkey octopus owl panda pig puppy rabbit rat scorpion seal shark sheep snail snake spider squirrel
                tiger turtle wolf zebra''')
                
mineral = words('''agate alexandrite amethyst aquamarine aventurine azurite basalt calcite carnelian citrine coal diamond dolomite emerald feldspar fluorite garnet gold 
                 granite gypsum hematite howlite jade jasper jet kunzite labradorite limestone magnetite malachite mica nephrite obsidian opal peridot pumice pyrite quartz
                 ruby salt sandstone sapphire sard silica soapstone sodalite talc topaz tourmaline tsavorite turquoise unakite wairakite yeatmanite zircon zoisite''')
                 
vegetable = words('''artichoke asparagus avocado bamboo basil bean broccoli capers carrot cauliflower celeriac celery chard chestnut cabbage chives cress cucumber fennel garlic ginger
                    gourd kale kohlrabi leek lentils lettuce maize okra olive onion parsley parsnip pea pepper potato pumpkin radicchio radish rhubarb rocket romaine rutabaga
                    seaweed shallot sorrel spinach sprouts salsify squash succotash tomato turnip watercress yam zucchini''')
                    
# These should all be empty sets - if there are no diplicates...

# print (animal & vegetable)
# print (vegetable & mineral)
# print (mineral & animal)

def mistakes(regex, first_set, second_set, third_set):
    "The set of mistakes mades by the regex in classifying things in the first_set from the second_set and the third_set"
    return ({"Should have matched: " + F
        for F in first_set if not re.search(regex, F)} |
        
        {"Should not have matched: " + S
            for S in second_set if re.search(regex, S)} |
        
        {"Should not have matched: " + T
            for T in third_set if re.search(regex, T)})
        
long_animal = "^a(ll|n)|^b(i|ee|ear)|^c(h(ee|i(c|m))|ro|ow|a(m|t))|^d(e|u|o(g|lp))|^e[al]|^f(i|o|r|ly)|^g(ir|o(a|ldf))|^h(a|i|or)|^k(an|i)|^l(io|o)|^mo|^o[cw]|^p(an|i|up)|^ra[bt]|^s(c|eal|h(ar|ee)|n|qui|pid)|^t(i|urt)|^wo|^ze"
long_vegetable = "^a(r|s|vo)|^b(r|a(m|si)|ean)|^c(a(b|p|u|rr)|el|h(a|iv|es)|re|u)|^fen|^g(arl|in|ou)|^k(al|o)|^le|^mai|^o[kln]|^p(ar|e(a|p)|o|ump)|^r(ad|h|o|ut)|^s(eaw|hal|or|als|p(in|r)|qua|u)|^t(urn|om)|^wat|^ya|^zu"

re_animal = "be(e|ar)|nk|^ow|ige|ark|ors|tte|ide|ant|ly|roo|ig|pan|pus|o(x|g|w|at|lf)$|lio|ppo|qui|rtl|ee[rtp]|ken|fish|ppy|ird|ebr|[cr]a[mt]|eal|ff|ake|bit|uck|pio|ms|ail|gl|bst|cod|hin$"
re_vegetable = "ess|ok|bba|ya|[pe]k|llo|iz|iac|ut|cc|rro|voc|bean|urd|ppe|ves|ea$|(r|le|f)y$|agu|nac|low|ve$|orr|[ts]uc|i[pc]$|mai|rh|ock|ato$|boo|uas|til|eed|cha|nn|ing|lr|kal|oni|ers|umb|asi|dis"
re_mineral = "ire|ite|ise|(r|l)ine|ian|one|[at]z|pal|ic[ae]|^j|sum|sar|con|alt|gold$|net|agat|ys|by|alc|ond|oal|dsp|rid|ald"

def verify (re_a, re_m, re_v, animals, minerals, vegetables):
    assert not (mistakes(re_a, animals, minerals, vegetables) | mistakes(re_m, minerals, vegetables, animals) | mistakes(re_v, vegetables, animals, minerals))
    return True 

#print(mistakes(re_animal, animal, mineral, vegetable))
#print(mistakes(re_vegetable, vegetable, mineral, animal))
#print(mistakes(re_mineral, mineral, animal, vegetable))

verify (re_animal, re_mineral, re_vegetable, animal, mineral, vegetable)
