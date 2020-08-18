execute as @e[type=armor_stand, tag=portal] at @s run tp @s ~ ~ ~ ~5 ~

execute at @e[type=armor_stand, tag=portal] run particle minecraft:flame ^.5 ^.2 ^ 0.3 0.3 0.3 0 0 force
execute at @e[type=armor_stand, tag=portal] run particle minecraft:soul_fire_flame ^-.5 ^.2 ^ 0.3 0.3 0.3 0 0 force

execute at @e[type=armor_stand, tag=portal] run particle minecraft:totem_of_undying ^.8 ^2 ^ 0.3 0.3 0.3 0 0 force
execute at @e[type=armor_stand, tag=portal] run particle minecraft:totem_of_undying ^-.8 ^2 ^ 0.3 0.3 0.3 0 0 force


execute at @e[tag=miner] run fill ^ ^ ^ ^ ^1 ^ air destroy
execute as @e[tag=miner] at @s run tp ^ ^ ^-.1
