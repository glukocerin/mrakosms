import menu
import commands as cmd
# import player
import message as mg

main_menu = menu.Menu([
    menu.MenuItem(1, mg.new_game.ret(), cmd.define_player),
    menu.MenuItem(2, mg.load_game.ret(), cmd.load_game),
    menu.MenuItem(0, mg.exit_game.ret(), cmd.exit_game)
])

new_game = menu.Menu([
    menu.MenuItem(1, '- Nev ujrairasa', cmd.define_player),
    menu.MenuItem(2, '- Tovabb', cmd.set_start),
    menu.MenuItem(3, '- Mentes', cmd.save),
    menu.MenuItem(0, '- Kilepes a menubol(egy szinttel feljebb)', cmd.quit_menu)
])

roll_menu = menu.Menu([
    menu.MenuItem(1, 'Ujrasorsolas', cmd.set_start),
    menu.MenuItem(2, 'Tovabb', cmd.continue_reroll),
    menu.MenuItem(3, 'Mentes', cmd.save),
    menu.MenuItem(0, 'Kilepes a menubol(egy szinttel feljebb)', cmd.quit_menu)
])

quit_menu = menu.Menu([
    menu.MenuItem(1, '- Save and Quit', cmd.save_and_quit),
    menu.MenuItem(2, '- Quit without save', cmd.quit_wo_save),
    menu.MenuItem(3, '- Resume', cmd.resume)
])

potion_menu = menu.Menu([
    menu.MenuItem(1, '- ' + mg.potion_of_health.ret(), cmd.set_potion, mg.potion_of_health.ret()),
    menu.MenuItem(2, '- ' + mg.potion_of_dexterity.ret(), cmd.set_potion, mg.potion_of_dexterity.ret()),
    menu.MenuItem(3, '- ' + mg.potion_of_luck.ret(), cmd.set_potion, mg.potion_of_luck.ret())
    ])

potion_submenu = menu.Menu([
    menu.MenuItem(1, '- Reselect the Potion', cmd.continue_reroll),
    menu.MenuItem(2, '- Continue', cmd.begin),
    menu.MenuItem(3, '- Quit', cmd.resume)
    ])
