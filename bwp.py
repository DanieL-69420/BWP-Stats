import requests
# https://api.voxyl.net/


key = 'uqVsFpDkfhlxqSQQl6Z6qMBoRZFMXWdb'





mode = input("(1) Overall Player Stats\n(2) Player Game Stats\n(3) Guild Stats\n(4) Guild Leaderboard\n> ")

if mode == '1':
    player = input("Player > ")
    a = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}').json()
    uuidunformatted = a['id']
    a = []
    for letter in uuidunformatted:
        a += letter
    uuid = a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+'-'+a[8]+a[9]+a[10]+a[11]+'-'+a[12]+a[13]+a[14]+a[15]+'-'+a[16]+a[17]+a[18]+a[19]+'-'+a[20]+a[21]+a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]+a[29]+a[30]+a[31]
    params = {'api': key}
    generalstats = requests.get(f'https://api.voxyl.net/player/stats/overall/{uuid}', params=params).json()
    
    level = generalstats['level']
    exp = generalstats['exp']
    weightedwins = generalstats['weightedwins']
    print(f"\nLevel > {level}\nEXP > {exp}\nWeighted Wins > {weightedwins}")
    close = input("\nPress enter to exit...")
    
    
elif mode == '2':
    player = input("Player > ")
    a = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}').json()
    uuidunformatted = a['id']
    a = []
    for letter in uuidunformatted:
        a += letter
    uuid = a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+'-'+a[8]+a[9]+a[10]+a[11]+'-'+a[12]+a[13]+a[14]+a[15]+'-'+a[16]+a[17]+a[18]+a[19]+'-'+a[20]+a[21]+a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]+a[29]+a[30]+a[31]
    params = {'api': key}

    games = requests.get(f'https://api.voxyl.net/player/stats/game/{uuid}', params=params).json()
    gamelist = games['stats']
    for game in gamelist:
        wins = gamelist[game]['wins']
        kills = gamelist[game]['kills']
        print(f"Mode > {game} Wins > {wins} Kills > {kills}")
    close = input("\nPress enter to close...")
    
    
elif mode == '3':
    guildtag= input("Guild Tag > ")
    params = {'api': key}
    guildstats = requests.get(f'https://api.voxyl.net/guild/info/{guildtag}', params=params).json()
    name = guildstats['name']
    description = guildstats['desc']
    xp = guildstats['xp']
    
    
    params = {'api': key, 'num': '1000'}
    guildlist = requests.get(f'https://api.voxyl.net/guild/top', params=params).json()
    for guild in guildlist['guilds']:
        if guild['tag'].lower() == guildtag.lower():
            position = guild['placing']
    print(f"Name > {name}\nDescription > {description}\nXP > {xp}\nPosition > {position}")
    
    
elif mode == '4':
    lbrange = input("Range (1,000 max) > ")
    params = {'api': key, 'num': lbrange}
    guildlist = requests.get(f'https://api.voxyl.net/guild/top', params=params).json()
    for guild in guildlist['guilds']:
        name = guild['name']
        tag = guild['tag']
        position = guild['placing']
        xp = guild['xp']
        
        print(f"#{position} Name > {name}XP > {xp}")
else:
    close = input("Invalid Response! Press enter to exit...")