{
    "Begin" : {
        "description":  "This is the place. This is where I can finally fulfill my wish. I step into the entrance of \n\nthe square building and close the door behind me. A loud voice blares from a hidden \n\nspeaker in the room. WELCOME, PLAYER NUMBER...uh...406468645, TO THE \n\nPLACE WHERE YOU MAY OR MAY NOT DIE! \n\nONLY TIME WILL TELL! WE'RE ASSUMING YOU CAME BECAUSE YOU HEARD THE \n\nRUMORS ABOUT HOW WE CAN HELP ANYONE WITH THEIR MOST OUTLANDISH WISHES AND DREAMS, \n\nBUT WE FEEL WE OUGHT TO TELL YOU ABOUT WHAT'S REALLY HAPPENING. \n\nWE JUST SPREAD THOSE RUMORS SO DESPERATE PEOPLE LIKE YOU WOULD COME AND ENTERTAIN US! \n\nHOWEVER, WE'VE GOTTEN A LITTLE TIRED OF THIS WHOLE THING, SO IF YOU ANSWER ALL OF THE QUESTIONS, \n\nWE'LL GIVE YOU WHATEVER YOU WANT! WE'RE CURIOUS TO SEE WHAT PEOPLE LIKE YOU WANT BAD ENOUGH TO COME HERE! \n\nIF YOU WANT TO LEAVE, THOUGH, YOU KNOW WHERE THE EXIT IS! \n\nI will:",
        "options": [
            {
                "option": "Continue forward",
                "goto": "continue_forward"
                },
            {
                "option": "Leave",
                "goto": "Death"
                }
            ]
        },
    "continue_forward": {
        "description": "I can't stop now. I need to make my wish come true no matter the risk.\n\nI open the bright red door in front of me and step into the next room. An odd sound comes \n\nfrom behind me and I look back to see the door I just came through and see it sinking into  \n\nthe wall. There are two other doors, one red with the word Canada on it, the other blue \n\ndisplaying Germany. The hidden speaker kicks up again, the voice sounding more like a \n\nmachine instead of the person from the first room. \n\nHELLO. TO SURVIVE EACH ROOM \n\nYOU MUST LISTEN TO THE QUESTION I GIVE YOU AND ANSWER BY STEPPING \n\nTHROUGH THE DOOR WITH THE ANSWER YOU CHOOSE. AN INCORRECT ANSWER \n\nWILL CAUSE THE ROOM TO COLLAPSE AND KILL YOU. A CORRECT ANSWER WILL \n\nBRING YOU TO A NEW ROOM AND YOU WILL ANSWER ANOTHER QUESTION UNTIL \n\nYOU EITHER ANSWER ALL THE QUESTIONS OR YOU DIE. YOUR QUESTION IS: \n\nWHAT WAS THE FIRST COUNTRY TO USE DAYLIGHT SAVINGS TIME? \n\n I will: \n\n",
        "options": [
            {
                "option": "Choose the red door (Canada)",
                "goto": "Canada"
                },
            {
                "option": "Choose the blue door (Germany)",
                "goto": "Death"
                }
            ]
        },
    "Death" : {
        "description": "As I grab the doorknob, I hear a loud creaking coming from the walls. I try to run to \n\nthe other door to escape, but before I can take one step, all the walls implode. \n\nYOU DIED!",
        "options": []
    },
"Canada": {
    "description": "Going through the red door, I enter a room exactly like the last one. This time the red door has the number 2 \n\nand the blue door has the number 6. \n\n YOUR QUESTION IS: \n\nWHEN LAID ON THE GROUND, HOW MANY SIDES DOES A BOX HAVE? \n\nI will: \n\n",
    "options": [
        {
            "option": "Choose the red door(2)",
            "goto": "Death"
            },
        {
            "option" : "Choose the blue door(6)",
            "goto": "Six"
            }
        ]
    },
"Six": {
    "description": "In the next room, the red door says 'Dayira' and the blue says 'Midan'. \n\nYOUR QUESTION IS: \n\nWHAT IS THE ARABIC WORD FOR SQUARE ACCORDING TO GOOGLE TRANSLATE? \n\nI will: \n\n",
    "options": [
        {
            "option" : "Choose the red door (Dayira)",
            "goto": "Death"
            },
        {
            "option": "Choose the blue door (Midan)",
            "goto": "Midan"
            }
        ]
    },
 "Midan": {
     "description": "As I enter the next room, I look around and see a bit of blood in the corners of the room. \n\nIt's probably from the past players who didn't make it past this room. The red door says Yellow dwarf, the blue says Red giant. \n\nYOUR QUESTION IS: \n\nWHAT KIND OF STAR IS EARTH'S SUN? \n\nI will: \n\n",
     "options": [
         {
             "option" : "Choose the red door (Yellow dwarf)",
             "goto": "Dwarf"
             },
         {
             "option": "Choose the blue door (Red giant)",
             "goto": "Death"
             }
         ]
     },
 "Dwarf": {
     "description": "There is a puddle of blood in the next room with some dripping off the walls. \n\nThe next red door displays the words Geiger theory while the blue door has The \n\nCopenhagen interpretation written on it. \n\nYOUR QUESTION IS: \n\nTHE SCHRODINGER'S CAT THOUGHT EXPERIMENT WAS MADE TO ILLUSTRATE WHICH THEORY? \n\nI will: \n\n",
     "options": [
         {
             "option": "Choose the red door (Geiger theory)",
             "goto": "Death"
             },
         {
             "option": "Choose the blue door (The Copenhagen interpretation)",
             "goto": "Copenhagen"
             }
         ]
     },
 "Copenhagen": {
     "description": "On to the next room. There is slightly more blood in this room than in the \n\nprevious rooms. The red door says a bush and the blue door says a sleuth. \n\nYOUR QUESTION IS: \n\n WHAT IS A GROUP OF BEARS CALLED? \n\nI will: \n\n",
     "options": [
         {
             "option": "Choose the red door (bush)",
             "goto": "Death"
             },
         {
             "option": "Choose the blue door (sleuth)",
             "goto": "Sleuth"
             }
         ]
     },
 "Sleuth": {
     "description": "The sight that greets me makes me stop for a few seconds in the doorway to the next room. \n\nI see someone's severed hand sitting in a corner, surrounded by a massive amount of blood. \n\nThe now bloody doors display Mozart on the red door and Chopin on the blue. \n\nYOUR QUESTION IS: \n\nWHICH COMPOSER WROTE NOCTURNE OP.9 NO.2? \n\nI will: \n\n",
     "options": [
         {
             "option": "Choose the red door (Mozart)",
             "goto": "Death"
             },
         {
             "option": "Choose the blue door(Chopin)",
             "goto": "Chopin"
             }
         ]
     },
 "Chopin": {
     "description": "I enter the next room expecting to find even more blood and gore but find none. \n\nThis room is in pristine condition. The red door says hope and the blue door says love. \n\nCONGRATULATIONS. YOU HAVE MADE IT TO THE FINAL ROOM. \n\nANSWER THIS LAST QUESTION AND YOU WILL HAVE SURVIVED. YOUR QUESTION IS: \n\nIN THE MYTH OF PANDORA'S BOX, WHAT WAS LEFT AFTER EVERYTHING WAS RELEASED? \n\nI will: \n\n",
     "options": [
         {
             "option" : "Choose the red door (hope)",
             "goto": "Hope"
             },
         {
             "option": "Choose the blue door (love)",
             "goto": "Death"
             }
         ]
     },
 "Hope": {
     "description": "Once I open the door, I am greeted with applause. An entire crowd of people smile at me. \n\nSomeone, whose voice I recognize as the voice from the first room, suddenly appears in front of me, yelling in my face. \n\nCONGRATULATIONS, YOU HAVE SURVIVED THE GAME! \n\nSORRY ABOUT THE MESS ON THE WAY HERE, NO ONE IS WILLING TO CLEAN UP THE BLOOD LEFT BEHIND AFTER SOMEONE FAILS! \n\nWELL, AS PROMISED, YOU GET TO HAVE YOUR WISH OR DREAM OR WHATEVER GRANTED! JUST FOLLOW ME \n\nAND WE'LL GET EVERYTHING SORTED OUT!",
     "options": []
     }
    }


            
