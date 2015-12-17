import menu
import commands as cmd
import player
import game
import message as mg

class MenuItem:
    def __init__(self, num, description, command, arg = None):
        self.num = num
        self.description = description
        self.command = command
        self.arg = arg

    def __repr__(self):
        return '{} {}'.format(self.num, self.description)

### Menu Items ###
main_menu = menu.Menu([
    MenuItem(1, mg.new_game.ret(), player.user.new_player),
    MenuItem(2, mg.load_game.ret(), cmd.load_game),
    MenuItem(3, mg.exit_game.ret(), cmd.exit_game)
])

new_game = menu.Menu([
    MenuItem(1, mg.reenter_name.ret(), player.user.new_player),
    MenuItem(2, mg.continue_.ret(), player.user.roll_stats),
    MenuItem(3, mg.save.ret(), cmd.save),
    MenuItem(4, mg.quit.ret(), cmd.quit_menu)
])

load_game = menu.Menu([
    MenuItem(1, 'Load game', cmd.load_game),
    MenuItem(2, mg.resume.ret(), menu.resume),
    MenuItem(3, mg.quit.ret(), cmd.quit_menu),
])

save_game = menu.Menu([
    MenuItem(1, mg.add_new_item.ret(), player.user.add_item),
    MenuItem(2, mg.resume.ret(), menu.resume),
    MenuItem(3, mg.quit.ret(), cmd.quit_menu),
])

roll_menu = menu.Menu([
    MenuItem(1, mg.reroll_stats.ret(), player.user.roll_stats),
    MenuItem(2, mg.continue_.ret(), cmd.continue_to_potion),
    MenuItem(3, mg.save.ret(), cmd.save),
    MenuItem(4, mg.quit.ret(), cmd.quit_menu)
])

potion_menu = menu.Menu([
    MenuItem(1,
        mg.potion_of_health.ret(),
        player.user.set_potion,
        mg.potion_of_health.ret()
        ),
    MenuItem(2,
        mg.potion_of_dexterity.ret(),
        player.user.set_potion,
        mg.potion_of_dexterity.ret()
        ),
    MenuItem(3,
        mg.potion_of_luck.ret(),
        player.user.set_potion,
        mg.potion_of_luck.ret())
    ])

potion_submenu = menu.Menu([
    MenuItem(1, mg.reselect_potion.ret(), cmd.continue_to_potion),
    MenuItem(2, mg.continue_.ret(), player.user.get_character_stats),
    MenuItem(3, mg.quit.ret(), cmd.quit_menu)
    ])

potion_begin_menu = menu.Menu([
    MenuItem(1, mg.begin.ret(), game.game.start),
    MenuItem(2, mg.save.ret(), cmd.save),
    MenuItem(3, mg.quit.ret(), cmd.quit_menu)
    ])

figth_menu = menu.Menu([
    MenuItem(1, mg.strike.ret(), game.game.strike),
    MenuItem(2, mg.retreat.ret(), cmd.no_work),
    MenuItem(3, mg.quit.ret(), cmd.quit_menu)
    ])

strike_menu = menu.Menu([
    MenuItem(1, mg.continue_.ret(), game.game.continue_fight),
    MenuItem(2, mg.try_luck.ret(), game.game.try_luck),
    MenuItem(3, mg.retreat.ret(), cmd.no_work),
    MenuItem(4, mg.quit.ret(), cmd.quit_menu)
    ])

quit_menu = menu.Menu([
    MenuItem(1, mg.save_and_quit.ret(), cmd.save_and_quit),
    MenuItem(2, mg.save_wo_quit.ret(), cmd.quit_wo_save),
    MenuItem(3, mg.resume.ret(), menu.resume)
])
