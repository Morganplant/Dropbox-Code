execute as @p in minecraft:overworld run tp ~ ~ ~
tp @p @e[sort=nearest,limit=1,tag=last_pos]
forceload remove ~ ~
kill @e[tag=last_pos]