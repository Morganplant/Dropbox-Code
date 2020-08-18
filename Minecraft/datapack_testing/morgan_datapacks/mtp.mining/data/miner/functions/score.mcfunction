scoreboard players add @a clock 1
execute if score @a[limit=1] clock matches 800 run scoreboard players reset @a clock
execute if score @a[limit=1] clock matches 799 run kill @e[type=minecraft:armor_stand,nbt={CustomName:'{"text":"Miner"}'}]