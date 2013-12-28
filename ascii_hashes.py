#!/usr/bin/env python

import sys
import string


ascii_art = {}
# http://www.retrojunkie.com/asciiart/animals/otters.htm
ascii_art['O'] = """

         .-'"'-.
        /      o\\
       |    o   0).-.
       |       .-;(_/     .-.
        \\     /  /)).---._|  `\\   ,
         '.  '  /((       `'-./ _/|
           \\  .'  )        .-.;`  /
            '.             |  `\\-'
              '._        -'    /
                 ``''--`------`
"""
# http://www.retrojunkie.com/asciiart/vehicles/rockets.htm
ascii_art['R'] = """
                      *     .--.
                           / /  '
          +               | |
                 '         \\ \\__,
             *          +   '--'  *
                 +   /\\
    +              .'  '.   *
           *      /======\\      +
                 ;:.  _   ;
                 |:. (_)  |
                 |:.  _   |
       +         |:. (_)  |          *
                 ;:.      ;
               .' \\:.    / '.
              / .-'':._.''-. \\
              |/    /||\\    \\|
            _..--'''(())'''--.._
      _.-'''                    '''-._
    -'                                '-
"""
# Saxophone from patorjk.com
ascii_art['S'] = """
     _,-----,____g===;,
    <'.._____,-------g  ;
                       \\   \\,
                         q   q,
                          q    q,
                         [='     q
                           `;  O  p
                             k  O  p -{0
                              l  O  p -o
                              ,i     p
                               P  O   |
                             q:|   O| |BD
                                [   | P b
                                |   |  |____________
                              [ |   |  |\\         /
                              | '   |  P :       ;
                              | [   0   Q:  ( )  ;
                               [ P  ( )  |;  ( ) ;
                               :Q  ( )  V        p
                                \\   [           ;
                                 \\',     O    /
                                   ' ; _ . '
    """



# Doh font from http://www.patorjk.com/software/taag/#p=display&h=0&v=0&f=Blocks&t=c

ascii_letters = {}
ascii_letters['A'] = """
               AAA               
              A:::A              
             A:::::A             
            A:::::::A            
           A:::::::::A           
          A:::::A:::::A          
         A:::::A A:::::A         
        A:::::A   A:::::A        
       A:::::A     A:::::A       
      A:::::AAAAAAAAA:::::A      
     A:::::::::::::::::::::A     
    A:::::AAAAAAAAAAAAA:::::A    
   A:::::A             A:::::A   
  A:::::A               A:::::A  
 A:::::A                 A:::::A 
AAAAAAA                   AAAAAAA
"""
ascii_letters['B'] = """
BBBBBBBBBBBBBBBBB   
B::::::::::::::::B  
B::::::BBBBBB:::::B 
BB:::::B     B:::::B
  B::::B     B:::::B
  B::::B     B:::::B
  B::::BBBBBB:::::B 
  B:::::::::::::BB  
  B::::BBBBBB:::::B 
  B::::B     B:::::B
  B::::B     B:::::B
  B::::B     B:::::B
BB:::::BBBBBB::::::B
B:::::::::::::::::B 
B::::::::::::::::B  
BBBBBBBBBBBBBBBBB   
"""
ascii_letters['C'] = """
        CCCCCCCCCCCCC
     CCC::::::::::::C
   CC:::::::::::::::C
  C:::::CCCCCCCC::::C
 C:::::C       CCCCCC
C:::::C              
C:::::C              
C:::::C              
C:::::C              
C:::::C              
C:::::C              
 C:::::C       CCCCCC
  C:::::CCCCCCCC::::C
   CC:::::::::::::::C
     CCC::::::::::::C
        CCCCCCCCCCCCC
"""
ascii_letters['D'] = """
DDDDDDDDDDDDD        
D::::::::::::DDD     
D:::::::::::::::DD   
DDD:::::DDDDD:::::D  
  D:::::D    D:::::D 
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D     D:::::D
  D:::::D    D:::::D 
DDD:::::DDDDD:::::D  
D:::::::::::::::DD   
D::::::::::::DDD     
DDDDDDDDDDDDD        
"""
ascii_letters['E'] = """
EEEEEEEEEEEEEEEEEEEEEE
E::::::::::::::::::::E
E::::::::::::::::::::E
EE::::::EEEEEEEEE::::E
  E:::::E       EEEEEE
  E:::::E             
  E::::::EEEEEEEEEE   
  E:::::::::::::::E   
  E:::::::::::::::E   
  E::::::EEEEEEEEEE   
  E:::::E             
  E:::::E       EEEEEE
EE::::::EEEEEEEE:::::E
E::::::::::::::::::::E
E::::::::::::::::::::E
EEEEEEEEEEEEEEEEEEEEEE
"""
ascii_letters['F'] = """
FFFFFFFFFFFFFFFFFFFFFF
F::::::::::::::::::::F
F::::::::::::::::::::F
FF::::::FFFFFFFFF::::F
  F:::::F       FFFFFF
  F:::::F             
  F::::::FFFFFFFFFF   
  F:::::::::::::::F   
  F:::::::::::::::F   
  F::::::FFFFFFFFFF   
  F:::::F             
  F:::::F             
FF:::::::FF           
F::::::::FF           
F::::::::FF           
FFFFFFFFFFF           
"""
ascii_letters['G'] = """
        GGGGGGGGGGGGG
     GGG::::::::::::G
   GG:::::::::::::::G
  G:::::GGGGGGGG::::G
 G:::::G       GGGGGG
G:::::G              
G:::::G              
G:::::G    GGGGGGGGGG
G:::::G    G::::::::G
G:::::G    GGGGG::::G
G:::::G        G::::G
 G:::::G       G::::G
  G:::::GGGGGGGG::::G
   GG:::::::::::::::G
     GGG::::::GGG:::G
        GGGGGG   GGGG
"""
ascii_letters['H'] = """
HHHHHHHHH     HHHHHHHHH
H:::::::H     H:::::::H
H:::::::H     H:::::::H
HH::::::H     H::::::HH
  H:::::H     H:::::H  
  H:::::H     H:::::H  
  H::::::HHHHH::::::H  
  H:::::::::::::::::H  
  H:::::::::::::::::H  
  H::::::HHHHH::::::H  
  H:::::H     H:::::H  
  H:::::H     H:::::H  
HH::::::H     H::::::HH
H:::::::H     H:::::::H
H:::::::H     H:::::::H
HHHHHHHHH     HHHHHHHHH
"""
ascii_letters['I'] = """
IIIIIIIIII
I::::::::I
I::::::::I
II::::::II
  I::::I  
  I::::I  
  I::::I  
  I::::I  
  I::::I  
  I::::I  
  I::::I  
  I::::I  
II::::::II
I::::::::I
I::::::::I
IIIIIIIIII
"""
ascii_letters['J'] = """
          JJJJJJJJJJJ
          J:::::::::J
          J:::::::::J
          JJ:::::::JJ
            J:::::J  
            J:::::J  
            J:::::J  
            J:::::j  
            J:::::J  
JJJJJJJ     J:::::J  
J:::::J     J:::::J  
J::::::J   J::::::J  
J:::::::JJJ:::::::J  
 JJ:::::::::::::JJ   
   JJ:::::::::JJ     
     JJJJJJJJJ       
"""
ascii_letters['K'] = """
KKKKKKKKK    KKKKKKK
K:::::::K    K:::::K
K:::::::K    K:::::K
K:::::::K   K::::::K
KK::::::K  K:::::KKK
  K:::::K K:::::K   
  K::::::K:::::K    
  K:::::::::::K     
  K:::::::::::K     
  K::::::K:::::K    
  K:::::K K:::::K   
KK::::::K  K:::::KKK
K:::::::K   K::::::K
K:::::::K    K:::::K
K:::::::K    K:::::K
KKKKKKKKK    KKKKKKK
"""
ascii_letters['L'] = """
LLLLLLLLLLL             
L:::::::::L             
L:::::::::L             
LL:::::::LL             
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L               
  L:::::L         LLLLLL
LL:::::::LLLLLLLLL:::::L
L::::::::::::::::::::::L
L::::::::::::::::::::::L
LLLLLLLLLLLLLLLLLLLLLLLL
"""
ascii_letters['M'] = """
MMMMMMMM               MMMMMMMM
M:::::::M             M:::::::M
M::::::::M           M::::::::M
M:::::::::M         M:::::::::M
M::::::::::M       M::::::::::M
M:::::::::::M     M:::::::::::M
M:::::::M::::M   M::::M:::::::M
M::::::M M::::M M::::M M::::::M
M::::::M  M::::M::::M  M::::::M
M::::::M   M:::::::M   M::::::M
M::::::M    M:::::M    M::::::M
M::::::M     MMMMM     M::::::M
M::::::M               M::::::M
M::::::M               M::::::M
M::::::M               M::::::M
MMMMMMMM               MMMMMMMM
"""
ascii_letters['N'] = """
NNNNNNNN        NNNNNNNN
N:::::::N       N::::::N
N::::::::N      N::::::N
N:::::::::N     N::::::N
N::::::::::N    N::::::N
N:::::::::::N   N::::::N
N:::::::N::::N  N::::::N
N::::::N N::::N N::::::N
N::::::N  N::::N:::::::N
N::::::N   N:::::::::::N
N::::::N    N::::::::::N
N::::::N     N:::::::::N
N::::::N      N::::::::N
N::::::N       N:::::::N
N::::::N        N::::::N
NNNNNNNN         NNNNNNN
"""
ascii_letters['O'] = """
     OOOOOOOOO     
   OO:::::::::OO   
 OO:::::::::::::OO 
O:::::::OOO:::::::O
O::::::O   O::::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O:::::O     O:::::O
O::::::O   O::::::O
O:::::::OOO:::::::O
 OO:::::::::::::OO 
   OO:::::::::OO   
     OOOOOOOOO     
"""
ascii_letters['P'] = """
PPPPPPPPPPPPPPPPP   
P::::::::::::::::P  
P::::::PPPPPP:::::P 
PP:::::P     P:::::P
  P::::P     P:::::P
  P::::P     P:::::P
  P::::PPPPPP:::::P 
  P:::::::::::::PP  
  P::::PPPPPPPPP    
  P::::P            
  P::::P            
  P::::P            
PP::::::PP          
P::::::::P          
P::::::::P          
PPPPPPPPPP          
"""
ascii_letters['Q'] = """
     QQQQQQQQQ      
   QQ:::::::::QQ    
 QQ:::::::::::::QQ  
Q:::::::QQQ:::::::Q 
Q::::::O   Q::::::Q 
Q:::::O     Q:::::Q 
Q:::::O     Q:::::Q 
Q:::::O     Q:::::Q 
Q:::::O     Q:::::Q 
Q:::::O     Q:::::Q 
Q:::::O  QQQQ:::::Q 
Q::::::O Q::::::::Q 
Q:::::::QQ::::::::Q 
 QQ::::::::::::::Q  
   QQ:::::::::::Q   
     QQQQQQQQ::::QQ 
             Q:::::Q
              QQQQQQ
"""
ascii_letters['R'] = """
RRRRRRRRRRRRRRRRR   
R::::::::::::::::R  
R::::::RRRRRR:::::R 
RR:::::R     R:::::R
  R::::R     R:::::R
  R::::R     R:::::R
  R::::RRRRRR:::::R 
  R:::::::::::::RR  
  R::::RRRRRR:::::R 
  R::::R     R:::::R
  R::::R     R:::::R
  R::::R     R:::::R
RR:::::R     R:::::R
R::::::R     R:::::R
R::::::R     R:::::R
RRRRRRRR     RRRRRRR
"""
ascii_letters['S'] = """
   SSSSSSSSSSSSSSS 
 SS:::::::::::::::S
S:::::SSSSSS::::::S
S:::::S     SSSSSSS
S:::::S            
S:::::S            
 S::::SSSS         
  SS::::::SSSSS    
    SSS::::::::SS  
       SSSSSS::::S 
            S:::::S
            S:::::S
SSSSSSS     S:::::S
S::::::SSSSSS:::::S
S:::::::::::::::SS 
 SSSSSSSSSSSSSSS   
"""
ascii_letters['T'] = """
TTTTTTTTTTTTTTTTTTTTTTT
T:::::::::::::::::::::T
T:::::::::::::::::::::T
T:::::TT:::::::TT:::::T
TTTTTT  T:::::T  TTTTTT
        T:::::T        
        T:::::T        
        T:::::T        
        T:::::T        
        T:::::T        
        T:::::T        
        T:::::T        
      TT:::::::TT      
      T:::::::::T      
      T:::::::::T      
      TTTTTTTTTTT      
"""
ascii_letters['U'] = """
UUUUUUUU     UUUUUUUU
U::::::U     U::::::U
U::::::U     U::::::U
UU:::::U     U:::::UU
 U:::::U     U:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U:::::D     D:::::U 
 U::::::U   U::::::U 
 U:::::::UUU:::::::U 
  UU:::::::::::::UU  
    UU:::::::::UU    
      UUUUUUUUU      
"""
ascii_letters['V'] = """
VVVVVVVV           VVVVVVVV
V::::::V           V::::::V
V::::::V           V::::::V
V::::::V           V::::::V
 V:::::V           V:::::V 
  V:::::V         V:::::V  
   V:::::V       V:::::V   
    V:::::V     V:::::V    
     V:::::V   V:::::V     
      V:::::V V:::::V      
       V:::::V:::::V       
        V:::::::::V        
         V:::::::V         
          V:::::V          
           V:::V           
            VVV            
"""
ascii_letters['W'] = """
WWWWWWWW                           WWWWWWWW
W::::::W                           W::::::W
W::::::W                           W::::::W
W::::::W                           W::::::W
 W:::::W           WWWWW           W:::::W 
  W:::::W         W:::::W         W:::::W  
   W:::::W       W:::::::W       W:::::W   
    W:::::W     W:::::::::W     W:::::W    
     W:::::W   W:::::W:::::W   W:::::W     
      W:::::W W:::::W W:::::W W:::::W      
       W:::::W:::::W   W:::::W:::::W       
        W:::::::::W     W:::::::::W        
         W:::::::W       W:::::::W         
          W:::::W         W:::::W          
           W:::W           W:::W           
            WWW             WWW            
"""
ascii_letters['X'] = """
XXXXXXX       XXXXXXX
X:::::X       X:::::X
X:::::X       X:::::X
X::::::X     X::::::X
XXX:::::X   X:::::XXX
   X:::::X X:::::X   
    X:::::X:::::X    
     X:::::::::X     
     X:::::::::X     
    X:::::X:::::X    
   X:::::X X:::::X   
XXX:::::X   X:::::XXX
X::::::X     X::::::X
X:::::X       X:::::X
X:::::X       X:::::X
XXXXXXX       XXXXXXX
"""
ascii_letters['Y'] = """
YYYYYYY       YYYYYYY
Y:::::Y       Y:::::Y
Y:::::Y       Y:::::Y
Y::::::Y     Y::::::Y
YYY:::::Y   Y:::::YYY
   Y:::::Y Y:::::Y   
    Y:::::Y:::::Y    
     Y:::::::::Y     
      Y:::::::Y      
       Y:::::Y       
       Y:::::Y       
       Y:::::Y       
       Y:::::Y       
    YYYY:::::YYYY    
    Y:::::::::::Y    
    YYYYYYYYYYYYY    
"""
ascii_letters['Z'] = """
ZZZZZZZZZZZZZZZZZZZ
Z:::::::::::::::::Z
Z:::::::::::::::::Z
Z:::ZZZZZZZZ:::::Z 
ZZZZZ     Z:::::Z  
        Z:::::Z    
       Z:::::Z     
      Z:::::Z      
     Z:::::Z       
    Z:::::Z        
   Z:::::Z         
ZZZ:::::Z     ZZZZZ
Z::::::ZZZZZZZZ:::Z
Z:::::::::::::::::Z
Z:::::::::::::::::Z
ZZZZZZZZZZZZZZZZZZZ
"""


ascii_letters['1'] = """
  1111111   
 1::::::1   
1:::::::1   
111:::::1   
   1::::1   
   1::::1   
   1::::1   
   1::::l   
   1::::l   
   1::::l   
   1::::l   
   1::::l   
111::::::111
1::::::::::1
1::::::::::1
111111111111
"""
ascii_letters['2'] = """
 222222222222222    
2:::::::::::::::22  
2::::::222222:::::2 
2222222     2:::::2 
            2:::::2 
            2:::::2 
         2222::::2  
    22222::::::22   
  22::::::::222     
 2:::::22222        
2:::::2             
2:::::2             
2:::::2       222222
2::::::2222222:::::2
2::::::::::::::::::2
22222222222222222222
"""
ascii_letters['3'] = """
 333333333333333   
3:::::::::::::::33 
3::::::33333::::::3
3333333     3:::::3
            3:::::3
            3:::::3
    33333333:::::3 
    3:::::::::::3  
    33333333:::::3 
            3:::::3
            3:::::3
            3:::::3
3333333     3:::::3
3::::::33333::::::3
3:::::::::::::::33 
 333333333333333   
"""
ascii_letters['4'] = """
       444444444  
      4::::::::4  
     4:::::::::4  
    4::::44::::4  
   4::::4 4::::4  
  4::::4  4::::4  
 4::::4   4::::4  
4::::444444::::444
4::::::::::::::::4
4444444444:::::444
          4::::4  
          4::::4  
          4::::4  
        44::::::44
        4::::::::4
        4444444444
"""
ascii_letters['5'] = """
555555555555555555 
5::::::::::::::::5 
5::::::::::::::::5 
5:::::555555555555 
5:::::5            
5:::::5            
5:::::5555555555   
5:::::::::::::::5  
555555555555:::::5 
            5:::::5
            5:::::5
5555555     5:::::5
5::::::55555::::::5
 55:::::::::::::55 
   55:::::::::55   
     555555555     
"""
ascii_letters['6'] = """
        66666666   
       6::::::6    
      6::::::6     
     6::::::6      
    6::::::6       
   6::::::6        
  6::::::6         
 6::::::::66666    
6::::::::::::::66  
6::::::66666:::::6 
6:::::6     6:::::6
6:::::6     6:::::6
6::::::66666::::::6
 66:::::::::::::66 
   66:::::::::66   
     666666666     
"""
ascii_letters['7'] = """
77777777777777777777
7::::::::::::::::::7
7::::::::::::::::::7
777777777777:::::::7
           7::::::7 
          7::::::7  
         7::::::7   
        7::::::7    
       7::::::7     
      7::::::7      
     7::::::7       
    7::::::7        
   7::::::7         
  7::::::7          
 7::::::7           
77777777            
"""
ascii_letters['8'] = """
     888888888     
   88:::::::::88   
 88:::::::::::::88 
8::::::88888::::::8
8:::::8     8:::::8
8:::::8     8:::::8
 8:::::88888:::::8 
  8:::::::::::::8  
 8:::::88888:::::8 
8:::::8     8:::::8
8:::::8     8:::::8
8:::::8     8:::::8
8::::::88888::::::8
 88:::::::::::::88 
   88:::::::::88   
     888888888     
"""
ascii_letters['9'] = """
     999999999     
   99:::::::::99   
 99:::::::::::::99 
9::::::99999::::::9
9:::::9     9:::::9
9:::::9     9:::::9
 9:::::99999::::::9
  99::::::::::::::9
    99999::::::::9 
         9::::::9  
        9::::::9   
       9::::::9    
      9::::::9     
     9::::::9      
    9::::::9       
   99999999        
"""
ascii_letters['0'] = """
     000000000     
   00:::::::::00   
 00:::::::::::::00 
0:::::::000:::::::0
0::::::0   0::::::0
0:::::0     0:::::0
0:::::0     0:::::0
0:::::0     0:::::0
0:::::0     0:::::0
0:::::0     0:::::0
0:::::0     0:::::0
0::::::0   0::::::0
0:::::::000:::::::0
 00:::::::::::::00 
   00:::::::::00   
     000000000     
"""


