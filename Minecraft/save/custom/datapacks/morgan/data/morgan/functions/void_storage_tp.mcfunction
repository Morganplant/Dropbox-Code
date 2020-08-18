summon minecraft:armor_stand ~ ~ ~ {Tags:["last_pos"],Invisible:1b}
forceload add ~ ~


execute in minecraft:void run tp 0 ~ 0
tp @p @e[type=minecraft:armor_stand,tag=platform,limit=1]