class LandscaperGame():
    tools_data = [
        {
            'tool': 'teeth',
            'price': 0,
            'profit':1,
            'limit': 'unlimited',
            'owned': True,
            'next_tool': 'scissors'
        },
        {
            'tool': 'scissors',
            'price': 5,
            'profit': 5,
            'limit': 'unlimited',
            'owned': False,
            'next_tool': 'lawnmower'
        },
        {
            'tool': 'lawnmower',
            'price': 25,
            'profit': 50,
            'limit': 'unlimited',
            'owned': False,
            'next_tool':'fancy_lawnmower'
        },
        {
            'tool': 'fancy_lawnmower',
            'price': 250,
            'profit': 100,
            'limit': 'unlimited',
            'owned': False,
            'next_tool': 'starving_students'
        },
        {
            'tool': 'starving_students',
            'price': 500,
            'profit': 250,
            'limit': 'unlimited',
            'owned': False,
            'next_tool': False
        }
    ]
        

    def __init__(self, name = 'Teyo'):
        self.name = name
        self.tools = ['teeth']
        self.current_tool = 'teeth'
        self.money = 0
    
    def make_purchase(self, tool_name):
        for tool in LandscaperGame.tools_data:
            if(tool['tool'] == tool_name):
                if(tool['owned']):
                    print(f'You already own a {tool_name}')
                    return
                elif(self.money >= tool['price']):
                    self.money -= tool['price']
                    tool['owned'] = True
                    self.tools.append(tool_name)
                    self.current_tool = tool_name
                    print(f'You have purchased {tool_name}!You have ${self.money} left\n')
                    return
                else:
                    print(f'You do not have enough money for {tool_name}')
                    return
        print(f'No tool exists with the name of {tool_name}\n')
    
    def do_work(self, tool_name):
        for tool in LandscaperGame.tools_data:
            if(tool['tool'] == tool_name):
                if(tool['owned'] == True):
                    self.current_tool = tool_name
                    print(f'Cutting grass with {tool_name}...\n')
                    self.money += tool['profit']
                    print(f"You earned ${tool['profit']} today!\n")
                    return
                else:
                    print(f'You do not currently own {tool_name}')
                    return
        print(f'No {tool_name} in inventory. Not available for purchase.\n')


    def show_owned_tools(self):
        print('Currently owned tools: \n')
        for tool in LandscaperGame.tools_data:
            if tool['owned']:
                print(tool['tool'])
        print('Tools available to buy: \n')
        for tool in LandscaperGame.tools_data:
            if tool['owned'] == False:
                print(tool['tool'])


    def display_instructions(self):
        print("""
Welcome to Landscaper!

In this LandscaperGame, you will start your journey as a budding landscaper with nothing but your teeth. The aim of the LandscaperGame is to make enough money to eventually hire a team of starving students and reach a total of $1000.

Here are your steps to grow your landscaping empire:

1. Initially, you only have your teeth to cut grass. You spend the day cutting lawns and earn $1. You can do this as much as you want.

2. Once you've earned enough, you can buy a pair of rusty scissors for $5. With the scissors, you can cut lawns and earn $5 per day.

3. When you've made enough money using the scissors, you can buy an old-timey push lawnmower for $25. This allows you to earn $50 per day cutting lawns.

4. As you progress and save more money, you can buy a fancy battery-powered lawnmower for $250. This increases your earnings to $100 per day.

5. Finally, when you have enough money while using the battery-powered lawnmower, you can hire a team of starving students for $500. Now you're able to make $250 per day.

Remember, you can only purchase an item once and when you have enough money for it. The more advanced your tool or team, the more money you make per day.

Your goal is to reach $1000 while having a team of starving students. Once you achieve this, you have won the LandscaperGame. Good luck with your landscaping business!
""")
    
    
    def play_game(self):
        res = ''
        while(self.money < 1000 or self.current_tool != 'starving_students'):
            res = input(f'It is a new day! Cut lawns with {self.current_tool}? Type Y for yes and N for no if you need rest: ')
            print('\n')
            while(res.lower() != 'y'):
                res = input(f'It is a new day! Cut lawns with {self.current_tool}? Type Y for yes and N for no if you need rest: ')
                print('\n')
            self.do_work(self.current_tool)

            #check for possible purchase

            for tool in LandscaperGame.tools_data:
                if tool['tool'] == self.current_tool:
                    next_tool_name = tool['next_tool']

                    #if false, starving students have been hired
                    if(next_tool_name == False):
                        print("There's no next tool to purchase. Keep hustling with your current equipment to reach your goal!\n")
                        break
                    
                    for next_tool in LandscaperGame.tools_data:
                        if next_tool['tool'] == next_tool_name:
                            if self.money >= next_tool['price']:
                                res = input(f'Good work! You have enough money to buy {next_tool_name}. Would you like to purchase it? Type Y for yes and N for no: ')
                                print('\n')
                                if res.lower() == 'y':
                                    self.make_purchase(next_tool_name)
                            break
                    break
        print("Well done! You now have accumulated over $1000 and own a team of starving students! Winner!\n")

            

    

game_flag = True        
while(game_flag):
    game = LandscaperGame()
    game.display_instructions()
    game.play_game()
    play_again = input('Play again? Type Y for yes and N for no.\n')
    game_flag = True if play_again.lower() == 'y' else False
