import unittest
from solution import *


class IsPalindromeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
    
    def test_1(self) -> None:
        lst = LinkedList(['t', 'a', 'c', 'o', 'c', 'a', 't'])
        self.assertTrue(self.sol.is_palindrome(lst))
    
    def test_2(self) -> None:
        lst = LinkedList(['n', 'o', 'l', 'e', 'm', 'o', 'n', 'n', 'o', 'm', 'e', 'l', 'o', 'n'])
        self.assertTrue(self.sol.is_palindrome(lst))
    
    def test_3(self) -> None:
        lst = LinkedList(['y', 'a', 'l', 'i', 'k', 'e', 'j', 'a', 'z', 'z', '?'])
        self.assertFalse(self.sol.is_palindrome(lst))
        """
        o+/:----.------------------......---........-:/o+:------...--......--:::::::::::
        o+/:-.--.-------------........```````.........-:/:----------.......--:::::::::::
        o+/--..------------......``````````````````````......------.......---:::::::::::
        oo/:-.--.-------...`````````````````````````````````..............----::::::::::
        oo/:-......-.....`````````````````````````````````````..........................
        so/:---.--......````....-------...````````````````````..........................
        oo/:--.--.........-:/osssyyyysssoo+/:-..```````..-/++/-.........................
        so/:--..........-/syhhhhhhhhhhhhhhhyyysoo+/:/++oyyhhyso-...........-------------
        so/:-..........-+yhhhhhhhhhhhhhhhhhhhhddddhhhdhhho:-:/++-..-:/+osossyyyyyyyyyyyy
        so+:--.-....``./hhhhhhyyhhhhhhhhhhdddddddhdhddddh+/ohdddy/+yhhyo//+osyyhhddddddh
        so+/:-----..``-ohhhhyyssssoooooooossssss+/ohdddddddddddddyyyo/:-----://+osyyhhhy
        yyysoooo++/-.`:ydhhhs+///++++/++//////:::/ohdddddddddddmms/:-...........--:/+oso
        ssssssssssyo.`:hdhyssyyssssyyhhhdddddhhyyyhhddddddddddddmh:..........----::///++
        ......---:sy-`-ydhysoosyyo+//:/+syyhhddhyyhhdddddddddddddmo..-.......----::::::.
        ``````...:yy:.-ydhhysosdmdyo+:..-+hdddyysyhhddhysyhddddddms---......-----://++/.
        ````...-+hhs:.-ydhhyyysshhhysoosydNNmdhysyhhdds/--:+shdddd+--.......-----/oyhy/`
        -:/+ossyhyso/.-hdhhhyyhhhhhyyyhdddddhhhhyhhddhso+/:/sysshs---.......----:+yhs:`/
        yyhhhhhyo++++:/hddhhyssyhhhhhhhhhhhhddhhhhdddhyhhhddNNdo::--.......-----:oys:./y
        hhhhhhyso+/+++sdddhhyssssyyhhhhhhhhddhhhhdddddhhdddmmh/-..........------:oyyyyyh
        hhyyhhyso+++++ohddhhyssssyyyssyyhhhhhhhyyhddddddhddmh/............------/osyyyyy
        hyoyhhyys++++++shdhhysossyhhs+syyhhhhhhyssyddddddddds-............------/osssyyy
        yo+yhhyys++++oo+shdhyyssyyhhho+osyyhhhhhhhhddddddddy:............------:+ossssss
        s++yhhyyso++++oooshhhysssyyyhhso+ossyhhdddddddddddh+-............------:+ossssss
        o/+ydhhyyso++ooooosyhyyssssyyyhyssoooosyyhhhhhhhdh+-.............------:+ooossss
        o//ohhhhhhs++ooooooosyysssssssyhhhyyyyys++yhhhhhs/-...............-----/+ooooooo
        s::/shhhhdyo+ooooooooosssssssssyyyhhhhhhhhhhhhs+-.................-----/+ooooooo
        s/::/shhhdho+oooooooooosssssssssyyyyhhhhhhyo+/-...................-----/oooooooo
        s+---:ohhddso+ooooooooosssyyyyssssyyyysoo/:-......................----:/oooooooo
        os/---:ohhdyo++oooossssyyhhhhhhhhhhhs:--..........................----:+oooooooo
        sso/---:shdhooooossyyyhhhhhhhhhddhyo:-.-..........................----:++ooooooo
        ysoo+:--/hhhyssssyyhhhhhhhhhhhhhyo+:--.-...........................---:+++oooooo
        yys+o+:.-ohdhhhhyyhhhhhhhhhhhyso++:---.............................---/++++++ooo
        yyys+oo/--+hdhhhhhhhhhhysso++++oo:--...............................--:/++++oo+++
        yyyyso++o+:+hhhhhhhhhhhhyysooos+:-.`.-.............`...............--:/+++++++++
        yyyyyyso++++oyhhhhhhhhhysyhyo++::-``.---...........................--:/+++++++++
        yyyyyysssoo++osyhhhhhhhsoyyo:-:/:----::/:.........``..............---:/+++++++++
        yyyyyyssssyyssssyhhhhhhyosso+/-::::::::///:----...................---:/+++++++++
        yyyyyysssyyyyyyyyyhhysoo+/::-.``..-----:::::--....`````...........---//+++++++++
        sssssssssssyyyssso+/-.........```````````.........................--://+++++++++
        .-:/+++o++++/:--..................`````````````````...............--:///////////
        """
    
    def test_4(self) -> None:
        lst = LinkedList(['a'])
        self.assertTrue(self.sol.is_palindrome(lst))
    
    def test_5(self) -> None:
        lst = LinkedList([])
        self.assertTrue(self.sol.is_palindrome(lst))