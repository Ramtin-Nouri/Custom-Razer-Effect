import json
import os

configFile = json.loads(open(os.path.dirname(__file__)+"/config.json",'r').read())

COLOR_BG = configFile["Background"]
COLOR_REACT = configFile["React"]
REACTIVE_TIME = configFile["Length"]

KEY_MAPPING = { "key.esc" : (0, 1),
                "key.f1" : (0, 3),
                "key.f2" : (0, 4),
                "key.f3" : (0, 5),
                "key.f4" : (0, 6),
                "key.f5" : (0, 7),
                "key.f6" : (0, 8),
                "key.f7" : (0, 9),
                "key.f8" : (0, 10),
                "key.f9" : (0, 11),
                "key.f10" : (0, 12),
                "key.f11" : (0, 13),
                "key.f12" : (0, 14),
                "key.print_screen" : (0,15),
                "key.scroll_lock" : (0,16),
                "key.pause" : (0,17), #TODO: Doesnt work
                "<269025041>" : (0,21), #TODO: Doesnt work
                "<269025043>" : (0,21), #TODO: Doesnt work
                "['^']" : (1,1),
                "°" : (1,1), #TODO: Doesnt work
                "'1'" : (1,2), 
                "'2'" : (1,3),
                "'3'" : (1,4),
                "'4'" : (1,5),
                "'5'" : (1,6),
                "'6'" : (1,7),
                "'7'" : (1,8),
                "'8'" : (1,9),
                "'9'" : (1,10),
                "'0'" : (1,11),
                "'ß'" : (1,12),
                "['´']" : (1, 13),
                "'!'" : (1,2),
                "'\"'" : (1,3),
                "'§'" : (1,4),
                "'$'" : (1,5),
                "'%'" : (1,6),
                "'&'" : (1,7),
                "'/'" : (1,8),
                "'('" : (1,9),
                "')'" : (1,10),
                "'='" : (1,11),
                "'?'" : (1,12),
                "['`']" : (1, 13),

                "key.backspace" : (1,14),
                "key.insert": (1,15),
                "key.home": (1,16),
                "key.page_up": (1,17),

                "key.tab" : (2,1),
                "'q'" : (2,2), 
                "'w'" : (2,3),
                "'e'" : (2,4),
                "'r'" : (2,5),
                "'t'" : (2,6),
                "'z'" : (2,7),
                "'u'" : (2,8),
                "'i'" : (2,9),
                "'o'" : (2,10),
                "'p'" : (2,11),
                "'ü'" : (2,12),
                "'+'" : (2,13),
                "'*'" : (2,13),
                "key.delete": (2,15),
                "key.end": (2,16),
                "key.page_down": (2,17),

                "key.caps_lock" : (3,1),
                "'a'" : (3,2),
                "'s'" : (3,3),
                "'d'" : (3,4),
                "'f'" : (3,5),
                "'g'" : (3,6),
                "'h'" : (3,7),
                "'j'" : (3,8),
                "'k'" : (3,9),
                "'l'" : (3,10),
                "'ö'" : (3,11),
                "'ä'" : (3,12),
                "'#'" : (3,13),
                '"\'"' : (3,13),

                "key.shift" : (4,1),
                "'<'" : (4,2),
                "'y'" : (4,3),
                "'x'" : (4,4),
                "'c'" : (4,5),
                "'v'" : (4,6),
                "'b'" : (4,7),
                "'n'" : (4,8),
                "'m'" : (4,9),
                "','" : (4,10),
                "'.'" : (4,11),
                "'-'" : (4,12),
                ";,'" : (4,10),
                "':'" : (4,11),
                "'_'" : (4,12),
                "key.shift_r" : (4,14),

                "key.up" : (4,16),
                "key.ctrl" : (5,1),
                "key.cmd" : (5,2),
                "key.alt" : (5,3),
                "key.space" : (5,7),
                "<65027>" : (5,11),
                "key.menu" : (5,13),
                "key.left" : (5,15),
                "key.down" : (5,16),
                "key.right" : (5,17),
                "key.ctrl_r" : (5,14),
                "key.enter": (3,14),

                "Numpad-1":(4,18),
                "Numpad-2":(4,19),
                "Numpad-3":(4,20),
                "Numpad-4":(3,18),
                "<65437>":(3,19),
                "Numpad-6":(3,20),
                "Numpad-7":(2,18),
                "Numpad-8":(2,19),
                "Numpad-9":(2,20),
                "Numpad-0":(5,19),
                "Numpad-/":(1,19),
                "Numpad-*":(1,20),
                "Numpad--":(1,21),
                "Numpad-+":(2,21),
                "<65439>":(5,20),
                # TODO: numpad enter , recognised as usual enter
                "key.num_lock": (1,18)
}