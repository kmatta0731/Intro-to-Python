
>>> from hw4 import *

##### WordGame #####

>>> wg = WordGame('APPLE')
>>> wg.getState(), wg.getHint(), wg.getRight(), wg.getWrong()
('playing', '?????', '', '')
>>> wg.guess('P')
>>> wg.getState(), wg.getHint(), wg.getRight(), wg.getWrong()
('playing', '?PP??', 'P', '')
>>> wg.guess('Q')
>>> wg.getState(), wg.getHint(), wg.getRight(), wg.getWrong()
('playing', '?PP??', 'P', 'Q')
>>> wg.guess('R')
>>> wg.getState(), wg.getHint(), wg.getRight(), wg.getWrong()
('playing', '?PP??', 'P', 'QR')
>>> wg.guess('L')
>>> wg.getState(), wg.getHint(), wg.getRight(), wg.getWrong()
('playing', '?PPL?', 'PL', 'QR')
>>> wg.guess('L')
>>> wg.getState(), wg.getHint(), wg.getRight(), wg.getWrong()
('playing', '?PPL?', 'PL', 'QR')
>>> wg.guess('A')
>>> wg.getState(), wg.getHint(), wg.getRight(), wg.getWrong()
('playing', 'APPL?', 'PLA', 'QR')
>>> wg.guess('E')
>>> wg.getState(), wg.getHint(), wg.getRight(), wg.getWrong()
('won', 'APPLE', 'PLAE', 'QR')
>>> wg.guess('X')
>>> wg.getState(), wg.getHint(), wg.getRight(), wg.getWrong()
('won', 'APPLE', 'PLAE', 'QR')
>>> wg = WordGame('RAILROAD')
>>> [(letter,wg.guess(letter), wg.getState(), wg.getHint(), wg.getRight(), wg.getWrong()) for letter in 'RQQOASFOYYUYUIRAILTRE']
[('R', None, 'playing', 'R???R???', 'R', ''), ('Q', None, 'playing', 'R???R???', 'R', 'Q'), ('Q', None, 'playing', 'R???R???', 'R', 'Q'), ('O', None, 'playing', 'R???RO??', 'RO', 'Q'), ('A', None, 'playing', 'RA??ROA?', 'ROA', 'Q'), ('S', None, 'playing', 'RA??ROA?', 'ROA', 'QS'), ('F', None, 'playing', 'RA??ROA?', 'ROA', 'QSF'), ('O', None, 'playing', 'RA??ROA?', 'ROA', 'QSF'), ('Y', None, 'playing', 'RA??ROA?', 'ROA', 'QSFY'), ('Y', None, 'playing', 'RA??ROA?', 'ROA', 'QSFY'), ('U', None, 'playing', 'RA??ROA?', 'ROA', 'QSFYU'), ('Y', None, 'playing', 'RA??ROA?', 'ROA', 'QSFYU'), ('U', None, 'playing', 'RA??ROA?', 'ROA', 'QSFYU'), ('I', None, 'playing', 'RAI?ROA?', 'ROAI', 'QSFYU'), ('R', None, 'playing', 'RAI?ROA?', 'ROAI', 'QSFYU'), ('A', None, 'playing', 'RAI?ROA?', 'ROAI', 'QSFYU'), ('I', None, 'playing', 'RAI?ROA?', 'ROAI', 'QSFYU'), ('L', None, 'playing', 'RAILROA?', 'ROAIL', 'QSFYU'), ('T', None, 'lost', 'RAILROA?', 'ROAIL', 'QSFYUT'), ('R', None, 'lost', 'RAILROA?', 'ROAIL', 'QSFYUT'), ('E', None, 'lost', 'RAILROA?', 'ROAIL', 'QSFYUT')]
>>> wg = WordGame('RAILROAD')
>>> [(letter,wg.guess(letter), wg.getState(), wg.getHint(), wg.getRight(), wg.getWrong()) for letter in 'RQQOASFOYYUYUIRAILDTRE']
[('R', None, 'playing', 'R???R???', 'R', ''), ('Q', None, 'playing', 'R???R???', 'R', 'Q'), ('Q', None, 'playing', 'R???R???', 'R', 'Q'), ('O', None, 'playing', 'R???RO??', 'RO', 'Q'), ('A', None, 'playing', 'RA??ROA?', 'ROA', 'Q'), ('S', None, 'playing', 'RA??ROA?', 'ROA', 'QS'), ('F', None, 'playing', 'RA??ROA?', 'ROA', 'QSF'), ('O', None, 'playing', 'RA??ROA?', 'ROA', 'QSF'), ('Y', None, 'playing', 'RA??ROA?', 'ROA', 'QSFY'), ('Y', None, 'playing', 'RA??ROA?', 'ROA', 'QSFY'), ('U', None, 'playing', 'RA??ROA?', 'ROA', 'QSFYU'), ('Y', None, 'playing', 'RA??ROA?', 'ROA', 'QSFYU'), ('U', None, 'playing', 'RA??ROA?', 'ROA', 'QSFYU'), ('I', None, 'playing', 'RAI?ROA?', 'ROAI', 'QSFYU'), ('R', None, 'playing', 'RAI?ROA?', 'ROAI', 'QSFYU'), ('A', None, 'playing', 'RAI?ROA?', 'ROAI', 'QSFYU'), ('I', None, 'playing', 'RAI?ROA?', 'ROAI', 'QSFYU'), ('L', None, 'playing', 'RAILROA?', 'ROAIL', 'QSFYU'), ('D', None, 'won', 'RAILROAD', 'ROAILD', 'QSFYU'), ('T', None, 'won', 'RAILROAD', 'ROAILD', 'QSFYU'), ('R', None, 'won', 'RAILROAD', 'ROAILD', 'QSFYU'), ('E', None, 'won', 'RAILROAD', 'ROAILD', 'QSFYU')]
>>> 


>>> root = Tk()
>>> WordGameGUI("APPLE",root).pack()
>>> root.destroy()
>>> 
>>> 
>>> WordGameGUI("ORANGE").pack()
>>> 
