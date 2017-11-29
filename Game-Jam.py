import json, sys
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

with open ('C_dict.py') as json_data:
    world = json.load(json_data)
    
def get_response (response):
    try:
        return int(response)-1
    except ValueError:
        return -1

def print_response(count, responses):
    return str(count +1)

def check_quit (response):
    response = str(response)
    if response.lower() == 'q' or response.lower == 'quit':
        return True
    return False



Running = True
location = "Begin"
while Running:
    #get the current location
            current = world[location]
            # print out the description of the current location
            print(current['description'])
            #print out the options
            if current['options'] == []:
                Running = False
                continue
            for count,option in enumerate(current['options']):
                print('[' + print_response(count,current['options']) + '] ' + option['option'])
            print('[q] to quit')
            #get user response
            response = input('\n\nWhat say you?'  )
            #see if we need to quit
            if check_quit(response):
                Running = False
                continue
            #normalize response, convert to int
            response = get_response(response)
            #check response against options
            for count,option in enumerate(current['options']):
                if (response == count):
                    location = option['goto']
                    
                 
                
print("\n\nHow did you do? Die too quickly? Get your wish? Go ahead...Try again! \n\n")
